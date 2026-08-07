from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_plan(name, role, skills, weak_topics):

    prompt = f"""
    You are an expert interview coach.

    Student Name: {name}
    Target Role: {role}

    Skills:
    {skills}

    Weak Topics:
    {weak_topics}

    Create a personalized 7-day interview preparation plan.

    Format:
    Day 1:
    Day 2:
    ...
    Day 7:
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text