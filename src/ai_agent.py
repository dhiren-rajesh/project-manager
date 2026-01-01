import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def generate_project_plan(project_details: str) -> str:
    # Placeholder function to simulate AI-generated project plan
    prompt = ChatPromptTemplate("""Generate a detailed project plan for the following project: {project_details}. 
                                Return a small description of the plan followed by the split in a tabular format. 
                                The split should include the tasks side by side with the estimated time for each task.""")