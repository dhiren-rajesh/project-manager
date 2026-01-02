from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

client = genai.Client()

response_stock = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Maintain the stock of books in a library system and return it. Also mention Available or not based on stock."
)

response_input = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Return the books by the user input."
)