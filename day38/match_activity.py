from langchain_groq import ChatGroq
from pydantic import BaseModel, Field


llm = ChatGroq(model="openai/gpt-oss-20b")


def choose_best_activity(user_activity, intensity, candidates):
    if not candidates:
        return "NO_MATCH"
    candidate_names = [item["name"] for item in candidates]

    prompt = f"""
You are helping match a user's exercise to an exercise returned by a calorie API.

User exercise:
{user_activity}

User intensity:
{intensity}

Available API activities:
{candidate_names}

Choose the API activity that is the closest semantic match to the user's exercise.

IMPORTANT:
- Do not assume two exercises are the same just because they contain similar words.
- Prefer an exact or very close exercise match.
- Consider intensity when choosing.
- If none of the candidates is a reasonable match, return "NO_MATCH".

Return only one of the available activity names or "NO_MATCH".
"""

    result = llm.invoke(prompt)

    best_match = result.content.strip()

    for candidate in candidates:
        if candidate["name"] == best_match:
            return candidate

    return None