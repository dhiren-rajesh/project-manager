import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from google.generativeai import genai

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

prompt_temmplate = ChatPromptTemplate("""Generate a detailed project plan for the following project: {project_details}. 
                                Return a small description of the plan followed by the split in a tabular format. 
                                The split should include the tasks side by side with the estimated time for each task.""")

def generate_project_plan(project_details: str) -> str:
    # Placeholder function to simulate AI-generated project plan
    prompt = prompt_temmplate.format(project_details=project_details)
    