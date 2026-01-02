import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

prompt_template = ChatPromptTemplate.from_template(
    """
Generate a detailed project plan for the following project:

{project_details}

Return:
1. A short description of the project plan
2. A table with columns:
   - Task
   - Description
   - Estimated Time
"""
)


def generate_project_plan(project_details: str) -> str:
    # Placeholder function to simulate AI-generated project plan
    prompt = prompt_template.format_prompt(project_details=project_details)
    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model="llama-3.3-70b-versatile",
        temperature=0.3
    )

    response = llm.invoke(prompt)
    return response.content