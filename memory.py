import json
import os

FILE_NAME = "memory.json"

def save_user(name, role, skills, weak_topics):

    data = {
        "name": name,
        "role": role,
        "skills": skills,
        "weak_topics": weak_topics
    }

    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def load_user():

    if not os.path.exists(FILE_NAME):
        return None

    with open(FILE_NAME, "r") as f:
        return json.load(f)