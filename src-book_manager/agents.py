from google import genai
from google.genai import types
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

client = genai.Client()

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "db.json"
db_text = DB_PATH.read_text(encoding="utf-8")

prompt_stock = (
    "1. Maintain the stock of books in a library system and return it. "
    "2. Mention whether the book is available or not, based on stock."
    "3. Output must be in tabular format."
    "4. Do NOT create books which are not in the DB."
    "5. ONLY return the name, stock and available columns."
)

prompt_search = """
    ### User Input
    {user_input}

    ### Rules
    1. ONLY return books if the user input contains "id=<number>" exactly.
    2. If the rule is violated, return: "No book found".
    3. Match ONLY the given ID.
    4. Output must be in tabular format.
    5. Include all columns EXCEPT stock.
    6. Do NOT create books which are not in the DB.
    7. If user input is comma separted, return the EVERY book which satisfies ANY user inputs.
"""


def multi_agent_system(user_input):
    # Coordinator must run INSIDE the function
    coordinator_prompt = f"""
    You are a coordinator agent.

    Rules:
    1. If the user input has STOCK or AVAILABILITY, return EXACTLY:
       STOCK_AGENT
    2. If the user input has id=<number> or a book name, return EXACTLY:
       SEARCH_AGENT
    3. Return ONLY one term. No explanations.

    User Input:
    {user_input}
    """

    coordinator_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[coordinator_prompt]
    )

    decision = coordinator_response.text.strip()

    # Run ONLY the selected agent
    if decision == "STOCK_AGENT":
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                f"Library database:\n{db_text}",
                prompt_stock
            ]
        )
        return response.text

    elif decision == "SEARCH_AGENT":
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                f"Library database:\n{db_text}",
                prompt_search
            ]
        )
        return response.text

    else:
        return "Unable to route request"



if __name__ == "__main__":
    input_examples = [
        "id=4, To Kill a Mockingbird",
        "Show stock and availability",
        "id=10, Some Other Book",
    ]

    for user_input in input_examples:
        print("User Input:", user_input)
        result = multi_agent_system(user_input)
        print(result)
        print("\n" + "-"*50 + "\n")


