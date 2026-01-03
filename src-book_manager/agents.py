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
    "3. Do it in a tabular format."
    "4. Do not create books which are not in the DB."
)

prompt_search = "Return all the books which include the users input."

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
