from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_question(role):

    prompt = f"""
    You are a technical interviewer.

    Ask ONE interview question for a {role}.

    Do not provide the answer.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text