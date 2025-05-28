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
"Python Code Inside double quotes"
"""

prompt_template = PromptTemplate(
    input_variables=["code", "prompt", "fixes"],
    template=template,
)

def generate_code(llm, code, prompt, fixes):
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
    return fixed_code
