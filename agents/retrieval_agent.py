import json
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

with open("agents\defect_map.json", "r") as file:
    DEFECT_MAP = json.load(file)

retrieval_prompt_template = PromptTemplate(
    input_variables=["defect_type", "buggy_code", "fixed_code", "description"],
    template="""
Defect Type:
{defect_type}

Problem:
{description}

Buggy Code:
{buggy_code}

Fixed Code:
{fixed_code}

Summarize this example as helpful context for fixing other code with the same defect.
"""
)

def retrieve_similar_examples(llm, fixes):
    all_contexts = []

    for defect_type, _, _ in fixes:
        key = defect_type.strip().lower().replace(" ", "_")

        if key not in DEFECT_MAP:
            continue

        defect_type = DEFECT_MAP[key]

        chain = LLMChain(llm=llm, prompt=retrieval_prompt_template)
        result = chain.run({
            "defect_type": defect_type,
            "buggy_code": defect_type["buggy_code"],
            "fixed_code": defect_type["fixed_code"],
            "description": defect_type["problem"]
        })

        all_contexts.append(result.strip())

    return "\n\n---\n\n".join(all_contexts)
