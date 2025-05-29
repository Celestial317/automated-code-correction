from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

prompt_generation_template = PromptTemplate(
    input_variables=["code", "context", "logs"],
    template="""
You are a helpful AI programmer assistant. Your task is to guide the regeneration of a buggy Python function using suggestions, context, and testing feedback.

Original Code:
{code}

Related Examples and Context:
{context}

Previous Logs and Feedback of iterations:
{logs}

Using all of the above, generate a focused repair prompt that will help regenerate the code with minimal and accurate changes. The prompt should be informative enough to assist in correcting the logic while keeping the structure intact.
"""
)

def generate_prompt(llm, code, context):
    try:
        try:
            with open("log.txt", "r") as log_file:
                logs = log_file.read().strip()
        except FileNotFoundError:
            logs = "No validation logs found."

        chain = LLMChain(llm=llm, prompt=prompt_generation_template)
        prompt = chain.run(code=code, context=context, logs=logs).strip()
        return prompt
    except Exception as e:
        return f"ERROR: Exception occurred during prompt generation - {str(e)}"
