import subprocess
import json
from pathlib import Path
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_core.language_models import BaseLanguageModel
from langchain_core.tools import Tool


def subprocess_run_code(input_str: str) -> str:
    try:
        data = json.loads(input_str)
        fixed_code_path = data.get("fixed_code_path")

        if not fixed_code_path:
            return "Error: fixed_code_path is required."

        fixed_path = Path(fixed_code_path).resolve()

        if not fixed_path.exists():
            return f"Error: File does not exist at {fixed_path}"

        result = subprocess.run(
            ["python", str(fixed_path)],
            capture_output=True,
            text=True,
            timeout=10,
        )

        output = (result.stdout.strip() + "\n" + result.stderr.strip()).strip()
        return output

    except Exception as e:
        return f"Exception occurred: {str(e)}"


validate_code_tool = Tool.from_function(
    name="run_code",
    description=(
        '''Runs Python code file via subprocess to check validation if the output is correct or not. 
        Input: JSON string with key 'fixed_code_path'. 
        Output: stdout and stderr combined.'''
    ),
    func=subprocess_run_code,
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

    def validate_code(fixed_code_path: str):
        attempt_count = 1
        try:
            input_json = json.dumps({
                "fixed_code_path": fixed_code_path,
            })

            output = agent_executor.run(input_json)
            log_entry = (
                f"{'-'*60}\n"
                f"Validation Attempt: {attempt_count}\n"
                f"Fixed Code Path: {fixed_code_path}\n"
                f"Agent Output:\n{'Correct Code! hehe' if not output.strip() else output.strip()}\n"
                f"{'-'*60}\n"
            )
            with open("log.txt", "a") as log_file:
                log_file.write(log_entry)

            lowered = output.lower()
            if ("traceback" not in lowered
                and "error" not in lowered
                and "fail" not in lowered
                and "exception" not in lowered):
                return True, "Code ran successfully."
            else:
                return False, output.strip()

        except Exception as e:
            error_log = (
                f"{'!'*60}\n"
                f"Exception During Validation\n"
                f"Attempt: {attempt_count}\n"
                f"Fixed Code Path: {fixed_code_path}\n"
                f"Error: {str(e)}\n"
                f"{'!'*60}\n"
            )
            with open("log.txt", "a") as log_file:
                log_file.write(error_log)
            return False, f"Agent validation crashed: {str(e)}"

    return validate_code
