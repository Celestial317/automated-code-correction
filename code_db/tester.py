import os
import json
import copy
import pytest

CODE_DB_DIR = os.path.dirname(os.path.abspath(__file__))

FIXED_DIR = os.path.join(CODE_DB_DIR, "fixed_code")
CORRECT_DIR = os.path.join(CODE_DB_DIR, "correct_python_programs")
TESTCASE_DIR = os.path.join(CODE_DB_DIR, "json_testcases")

def load_function(version_dir, algo):
    module_path = f"{version_dir.replace(os.sep, '.')}.{algo}"
    try:
        module = __import__(module_path, fromlist=[algo])
    except ModuleNotFoundError as e:
        raise ImportError(f"Module not found: {module_path}") from e
    if not hasattr(module, algo):
        raise AttributeError(f"Module '{module_path}' has no attribute '{algo}'")
    return getattr(module, algo)

def load_testcases(algo):
    filepath = os.path.join(TESTCASE_DIR, f"{algo}.json")
    if not os.path.isfile(filepath):
        pytest.skip(f"No testcases for {algo}")
    with open(filepath, "r") as f:
        testcases = [json.loads(line) for line in f]
    return testcases

def get_algorithms():
    return [f[:-3] for f in os.listdir(FIXED_DIR) if f.endswith(".py")]

@pytest.mark.parametrize("algo", get_algorithms())
def test_fixed_vs_correct(algo):
    testcases = load_testcases(algo)

    fixed_func = load_function("fixed_code", algo)
    correct_func = load_function("correct_python_programs", algo)

    for inputs, expected in testcases:
        if not isinstance(inputs, (list, tuple)):
            inputs = [inputs]

        inputs_copy_for_fixed = copy.deepcopy(inputs)
        inputs_copy_for_correct = copy.deepcopy(inputs)

        try:
            fixed_out = fixed_func(*inputs_copy_for_fixed)
        except Exception as e:
            fixed_out = f"Exception: {e}"

        try:
            correct_out = correct_func(*inputs_copy_for_correct)
        except Exception as e:
            correct_out = f"Exception: {e}"

        assert fixed_out == correct_out, (
            f"\nAlgorithm: {algo}"
            f"\nInput: {inputs}"
            f"\nExpected (correct output): {correct_out}"
            f"\nFixed code output: {fixed_out}"
        )
