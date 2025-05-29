from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

DEFECT_TYPES = """
1. Off-by-one errors
2. Wrong loop range or condition
3. Incorrect comparison operators
4. Misused data structures
5. Wrong base case in recursion
6. Uninitialized variables
7. Missing return statements
8. Wrong function calls
9. Misplaced or extra conditions
10. Incorrect index usage
11. Wrong math or logic expression
12. Loop termination too early or late
13. Incomplete condition coverage
14. Incorrect updates in loop body
"""

template = """
You are an expert at repairing buggy Python code by identifying the most likely single-line defects.

Here are common bug categories:
{defect_types}

Buggy Code:
{code}

Last Feedback:
{feedback}

Analyze and identify the most probable defect types while preserving the original logic.
Propose minimal single-line fixes with explanations.

Respond in the following format:

Defect Type: <Predicted Type>
Fix:
<modified_line>
Reason:
<explanation_of_the_defect_and_fix>
"""

prompt_template = PromptTemplate(
    input_variables=["code", "feedback", "defect_types"],
    template=template,
)

def get_fix_suggestions(llm, code, feedback=""):
    try:
        chain = LLMChain(llm=llm, prompt=prompt_template)
        response = chain.run(
            code=code,
            feedback=feedback,
            defect_types=DEFECT_TYPES
        ).strip()

        suggestions = []
        blocks = response.split("\n\n")

        for block in blocks:
            defect, fix, reason = "", "", ""
            lines = block.strip().splitlines()
            for line in lines:
                if line.startswith("Defect Type:"):
                    defect = line[len("Defect Type:"):].strip()
                elif line.startswith("Fix:"):
                    fix = line[len("Fix:"):].strip()
                elif line.startswith("Reason:"):
                    reason = line[len("Reason:"):].strip()
            if defect or fix or reason:
                suggestions.append([defect, fix, reason])

        return suggestions

    except Exception as e:
        return [["Error", "", f"Exception during suggestion generation: {str(e)}"]]
