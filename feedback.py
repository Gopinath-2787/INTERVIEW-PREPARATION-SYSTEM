from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def evaluate_answer(question, answer):

    prompt = f"""
    You are an expert technical interviewer.

    Interview Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate the answer.

    Give the response in this format:

    Score: x/10

    ✅ Strengths
    - ...

    ❌ Improvements
    - ...

    📚 Correct Answer
    - ...

    Keep it concise and interview-focused.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text