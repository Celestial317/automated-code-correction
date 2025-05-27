import os
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.tools.riza.command import ExecPython
from pathlib import Path

os.environ["RIZA_API_KEY"] = ""

prompt_template = PromptTemplate(
    input_variables=["fixed_code", "test_code"],
    template="""
You are a Python code validator.

Given the fixed code below:

{fixed_code}

and the test code below:

{test_code}

Evaluate if the fixed code passes all the tests.

Respond exactly in one of the following formats:

If all tests pass, respond with:
PASS

If any test fails, respond with:
FAIL
<error message or failed test description>

Provide a brief explanation of the failure or success after the keyword.

Do not add any other text outside the specified format.
"""
)

def validate_code(llm, fixed_code_path, test_code_path):
    fixed_code = Path(fixed_code_path).read_text()
    test_code = Path(test_code_path).read_text()

    executor = ExecPython()
    exec_code = f"""{fixed_code} {test_code}"""
    result = executor.invoke(exec_code.strip())
    output = result.strip()

    chain = LLMChain(llm=llm, prompt=prompt_template)
    response = chain.run(fixed_code=fixed_code, test_code=test_code).strip()

    with open("agents/log.txt", "a") as log_file:
        log_file.write("VALIDATION RESULT:\n")
        log_file.write(f"{response}\n\n")
        log_file.write("RAW OUTPUT:\n")
        log_file.write(f"{output}\n\n")
        log_file.write("=" * 80 + "\n\n")

    if response.startswith("PASS"):
        passed = True
        feedback = ""
    elif response.startswith("FAIL"):
        passed = False
        split_response = response.split("\n", 1)
        if len(split_response) > 1:
            feedback = split_response[1].strip()
        else:
            feedback = "Test failed but no explanation was provided."
    else:
        passed = False
        feedback = "Response format not recognized."

    return passed, feedback
