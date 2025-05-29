Here is the cleaned-up version of your `README.md` without emojis, credits, or license section:

---

### `README.md`

```markdown
# Multi-Agent Code Repair System for QuixBugs

This project implements a multi-agent system using LangChain and Gemini/OpenAI LLMs to automatically repair buggy Python programs from the QuixBugs benchmark. The system iteratively generates, validates, and fixes buggy code using LLM agents.

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
├── testing\_code/                        # Corresponding test files
    ├── correct\python\_programs/         # For validation and Testing
log.txt                                  # Logs for validation attempts
main.py                                   # Entry point
agents/
├── code\_fix\_agent.py
├── code\_gen\_agent.py
├── prompt\_gen\_agent.py
├── retrieval\_agent.py
├── validator\_agent.py

````

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your_username/multi-agent-code-repair.git
cd multi-agent-code-repair
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Minimum required packages:

```
langchain
langchain-google-genai
openai
pydantic<2
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

The system will iterate through all files in `buggy_code/`, attempt to fix them, and write the results to `fixed_code/` if the tests pass.

## Output and Logs

* Fixed code will be saved in `code_db/fixed_code/`
* Intermediate iterations are stored in `temp_code/`
* Validation logs, including feedback and attempt count, are saved in `log.txt`

Example `log.txt` entries:

```
Validation failed after 1 attempt(s). Feedback: AssertionError: Expected 5 but got 3
Validation succeeded after 2 attempt(s).
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
