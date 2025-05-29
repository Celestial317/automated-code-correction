import subprocess
from pathlib import Path
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_core.language_models import BaseLanguageModel
from langchain_core.tools import Tool

def validate_code(fixed_code_path: str, test_code_path: str = None) -> str:
    try:
        fixed_path = Path(fixed_code_path).resolve()
        test_path = Path(test_code_path).resolve()

        temp_script_path = Path("run_validation.py")
        with open(temp_script_path, "w") as f:
            f.write(
                "import sys\n"
                "import pytest\n"
                f"sys.path.append('{test_path.parent.as_posix()}')\n"
                f"exec(open('{fixed_path.as_posix()}').read())\n"
                f"exec(open('{test_path.as_posix()}').read())\n"
            )

        result = subprocess.run(
            ["python", str(temp_script_path)],
            capture_output=True,
            text=True,
            timeout=10,
        )

        output = result.stdout + "\n" + result.stderr
        return output.strip()

    except Exception as e:
        return f"Exception occurred: {str(e)}"

    finally:
        if Path("run_validation.py").exists():
            Path("run_validation.py").unlink()


validate_code_tool = Tool.from_function(
    name="validate_code",
    description="Validate fixed Python code against a test script using subprocess, it executes the Code. Takes fixed_code_path and test_code_path.",
    func=validate_code,
    return_direct=True,
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
                f"Validate the fixed Python code using the test file. "
                f"fixed_code_path: {fixed_code_path}, test_code_path: {test_code_path}"
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
