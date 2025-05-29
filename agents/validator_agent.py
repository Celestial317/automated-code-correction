from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_core.language_models import BaseLanguageModel
from langchain_experimental.tools import PythonREPLTool
from pathlib import Path

validate_code_tool = PythonREPLTool(
    name="validate_code",
    description="Tool to run internal Python tests using Python REPL. Used to validate fixed Python code against test scripts.",
)

def validate_code_agent(llm: BaseLanguageModel):
    agent_executor = initialize_agent(
        tools=[validate_code_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=10,
    )

    def validate_code(fixed_code_path: str, test_code_path: str = None):
        attempt_count = 1
        try:
            query = (
                "import sys\n"
                "sys.path.append('code_db/testing_code')\n"
                "import pytest\n"
                "pytest.use_correct = lambda *args, **kwargs: None\n"
                f"exec(open('{fixed_code_path}').read())\n"
                f"exec(open('{test_code_path}').read())"
            )

            result = agent_executor.run(query)

            if "Traceback" not in result and "error" not in result.lower() and "fail" not in result.lower():
                with open("log.txt", "a") as log_file:
                    log_file.write(f"Validation succeeded after {attempt_count} attempt(s).\n")
                return True, ""
            else:
                with open("log.txt", "a") as log_file:
                    log_file.write(f"Validation failed after {attempt_count} attempt(s). Output: {result}\n")
                return False, result.strip()

        except Exception as e:
            with open("log.txt", "a") as log_file:
                log_file.write(f"Agent validation crashed after {attempt_count} attempt(s): {str(e)}\n")
            return False, f"Agent validation crashed: {str(e)}"

    return validate_code
