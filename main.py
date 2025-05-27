api_key = ""

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from agents.code_fix_agent import get_fix_suggestions
from agents.code_gen_agent import generate_code
from agents.retrieval_agent import retrieve_similar_examples
from agents.prompt_gen_agent import generate_prompt
from agents.validator_agent import validate_code
import warnings
warnings.filterwarnings("ignore")


MAX_ITERATIONS = 10
BASE_DIR = "code_db"
BUGGY_DIR = os.path.join(BASE_DIR, "buggy_code")
FIXED_DIR = os.path.join(BASE_DIR, "fixed_code")
TEMP_DIR = os.path.join(BASE_DIR, "temp_code")
TESTING_DIR = os.path.join(BASE_DIR, "testing_code")

def read_code(path):
    with open(path, "r") as f:
        return f.read()

def write_code(path, code):
    with open(path, "w") as f:
        f.write(code)
def run_single_file(llm, buggy_file, test_file):
    code = read_code(buggy_file)
    feedback = ""
    passed = False

    for _ in range(MAX_ITERATIONS):
        fixes = get_fix_suggestions(llm, code, feedback)
        context = retrieve_similar_examples(llm, fixes)
        prompt = generate_prompt(llm, code, context)
        new_code = generate_code(llm, code, prompt, fixes)

        temp_path = os.path.join(TEMP_DIR, os.path.basename(buggy_file))
        write_code(temp_path, new_code)

        passed, feedback = validate_code(llm, temp_path, test_file)

        if passed:
            final_path = os.path.join(FIXED_DIR, os.path.basename(buggy_file))
            write_code(final_path, new_code)
            return True

        code = new_code

    return False

def run():
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-05-20", api_key=api_key)
    buggy_files = sorted(os.listdir(BUGGY_DIR))
    success_count = 0
    total = len(buggy_files)

    for buggy_fname in buggy_files:
        buggy_path = os.path.join(BUGGY_DIR, buggy_fname)
        test_path = os.path.join(TESTING_DIR, "test_" + buggy_fname)

        if not os.path.exists(test_path):
            print(f"Test file missing for {buggy_fname}, skipping...")
            continue

        success = run_single_file(llm, buggy_path, test_path)
        print(f"{buggy_fname}: {'PASSED' if success else 'FAILED'}")
        success_count += int(success)

    print(f"\nSummary: {success_count}/{total} programs fixed successfully")
    print(f"Accuracy: {success_count / total * 100:.2f}%")

if __name__ == "__main__":
    run()
