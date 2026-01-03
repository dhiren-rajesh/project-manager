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
user_input = "id=4, To Kill a Mockingbird"

prompt_search = f"""
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

response_stock = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=[
        f"Library database:\n{db_text}",
        prompt_stock
    ]
)

response_search = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=[
        f"Library database:\n{db_text}",
        prompt_search
    ]
)

print("Stock: \n", response_stock.text)
print("Search:\n ", response_search.text)

