
# Automated Code Correction System

This project implements a multi-agent system using LangChain and Gemini LLMs to repair buggy Python programs from the QuixBugs benchmark automatically. The system iteratively generates, validates, and fixes buggy code using LLM agents.

## Features

- Defect detection and fix suggestion using an LLM
- Code generation using prompt and fix suggestions
- Retrieval of similar examples from a case base
- Prompt engineering with context and prior examples
- Test-based validation agent using subprocess execution
- Iterative code repair loop with log tracking

## Directory Structure

```

code\_db/
├── buggy\_code/                          # Input buggy Python files
├── fixed\_code/                          # Final fixed files after validation
├── temp\_code/                           # Intermediate outputs during iterations
├── correct\_python\_programs/            # For validation and Testing
├── json\_testcases/                      # Testcases to judge the accuracy
├── tester.py                             # Run this to compare Correct and Fixed Codes over Testcases

log.txt                                   # Logs for validation attempts
main.py                                   # Entry point

agents/
├── code\_fix\_agent.py                   # Detects the bugs and suggests line-by-line fixes
├── code\_gen\_agent.py                   # Generates the fixed code as suggested by fix_agent with dynamic prompting
├── prompt\_gen\_agent.py                 # Dynamic Prompt Generator based on Output by Validator
├── retrieval\_agent.py                   # Retrieves JSON map to check for suggested fixes of all 14 defects
├── validator\_agent.py                   # Uses Subprocess to Execute Python Files and test.
├── defect\_map.py                        # Acts as a Database for storing defects, fixes, and examples.

````

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Celestial317/automated-code-correction
cd automated-code-correction
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Minimum required packages:

```
langchain
langchain-google-genai
subprocess
```

### 3. Prepare dataset

Add buggy code to `code_db/buggy_code/` and test files to `code_db/testing_code/`.

Example:

* `code_db/buggy_code/bubble_sort.py`
* `code_db/testing_code/test_bubble_sort.py`

## Running the System

Set your Gemini key inside `main.py`:

```python
api_key = "your-api-key-here"
```

Run the system:

```bash
python main.py
```

The system will iterate through all files in `buggy_code/`, attempt to fix them, create a buffer of files at `temp_code/` till it validates the output, and write the final results to `fixed_code/` if all tests by `validator_agent.py` are passed.

## Output and Logs

* Fixed code will be saved in `code_db/fixed_code/`
* Intermediate iterations are stored in a Buffer named `temp_code/`
* Validation logs, including feedback and attempt count, are saved in `log.txt`

Example `log.txt` entries:

```
------------------------------------------------------------
Validation Attempt: 1
Fixed Code Path: code_db\temp_code\find_first_in_sorted.py
Agent Output:
File "C:\CodeVSCSummers\code_gen_check\code_db\temp_code\find_first_in_sorted.py", line 1
    ```python
    ^
SyntaxError: invalid syntax
------------------------------------------------------------
------------------------------------------------------------
Validation Attempt: 1
Fixed Code Path: code_db\temp_code\find_first_in_sorted.py
Agent Output:
Correct Code! hehe
------------------------------------------------------------
```

## Configuration

You can adjust maximum iterations in `main.py`:

```python
MAX_ITERATIONS = 10
```

This controls how many repair attempts the system makes before giving up on a file.

## Notes

* The validator uses Python execution to run test scripts safely and capture output/errors.
* Each agent runs independently and is coordinated by a single loop in `main.py`.

## Author

**Soumya Sourav Das**

[Portfolio](https://soumya-sourav-portfolio.vercel.app/) | [GitHub](https://github.com/Celestial317) | [LinkedIn](https://www.linkedin.com/in/soumyasouravdas/)


---
