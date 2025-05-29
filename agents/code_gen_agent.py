from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

template = """
You are an expert Python code repair assistant. Your task is to rewrite the following buggy code using the provided suggestions and prompt guidance.

Original buggy code:
{code}

Context and prompt:
{prompt}

Fix suggestions:
{fixes}

Generate the repaired code using minimal but correct changes. Make sure the final code is functional, readable, and logically correct.
Return only the fully fixed code, preserving the original logic and style.

use following format to return the code:
Return the python code as a string, enclosed in triple quotes or double quotes, without any additional text or comments.
such as:
Output:
"def example_function():
    print('Hello, World!')"

Do NOT do like this:
```python
codeline1 or whatever

the first line of <```python> is not needed as it gives error in validation,
just return the code as a string. NO additional comments or explanations.
do not mention it is python code or something, do not use any backtick

just USE triple quotes or double quotes to return the code.
"""

prompt_template = PromptTemplate(
    input_variables=["code", "prompt", "fixes"],
    template=template,
)

def generate_code(llm, code, prompt, fixes):
    try:
        fixes_lines = []
        for fix in fixes:
            defect_type = fix[0]
            fix_line = fix[1]
            reason = fix[2]
            fixes_lines.append("Defect Type: " + defect_type)
            fixes_lines.append("Fix: " + fix_line)
            fixes_lines.append("Reason: " + reason)
            fixes_lines.append("")  
        fixes_text = "\n".join(fixes_lines)

        chain = LLMChain(llm=llm, prompt=prompt_template)
        fixed_code = chain.run(code=code, prompt=prompt, fixes=fixes_text).strip()

        if (fixed_code.startswith('"') and fixed_code.endswith('"')) or \
       (fixed_code.startswith("'''") and fixed_code.endswith("'''")) or \
       (fixed_code.startswith('"""') and fixed_code.endswith('"""')):
            fixed_code = fixed_code.strip('"').strip("'")


        return fixed_code
    except Exception as e:
        return f'"""ERROR: Exception occurred during code generation - {str(e)}"""'
