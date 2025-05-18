from groq import Groq
from typing import List, Literal

from app.core.config import GROQ_ACCESS_TOKEN
from app.core.config import MODEL

client = Groq(
    api_key = GROQ_ACCESS_TOKEN
)

# Temperatures used for generating multiple replies
temperatures = [0.2, 0.5]

def query_llm(system_prompt: str, post_text: str, temp: float):
    """
    Query the LLM API
    """
    response = client.chat.completions.create(
        model = MODEL,
        temperature = temp,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": post_text
            }
        ],
    )

    return response.choices[0].message.content

def decide_tone(platform: Literal["linkedin", "twitter", "insta"], post_text: str) -> str:
    """
    Given the text of a social media post, decide the tone of the post.
    """
    system_prompt = f"Given the text of a {platform} post, decide if the post is formal, casual, friendly or neutral. Only reply with the decided tone."
    response = query_llm(system_prompt, post_text, 1)

    return response if response else "neutral"

def generate_reply_tool(platform:  Literal["linkedin", "twitter", "insta"], post_text: str, tone: str) -> List[str]:
    """
    Given the text of a social media post, generate a human-like reply.
    """
    if platform == "linkedin":
        system_prompt = "Your job is to respond only with a human-like reply to the linkedin post provided by the user."
    elif platform == "twitter":
        system_prompt = "Your job is to respond only with a human-like reply to the twitter post provided by the user."
    elif platform == "insta":
        system_prompt = "Your job is to respond only with a human-like reply to the instagram post provided by the user."
    responses = []

    system_prompt += f" The tone of the reply should be {tone}."

    for temp in temperatures:
        responses.append(query_llm(system_prompt, post_text, temp))
    return responses
