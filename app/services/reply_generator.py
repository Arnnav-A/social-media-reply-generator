from typing import Literal, List

from app.core.logger import logger
from app.utils.nlp_tools import decide_tone, generate_reply_tool

def generate_reply(platform: Literal["linkedin", "twitter", "insta"], post_text: str) -> List[str]:
    """
    Identify the tone of a social media post and generate a human-like reply
    """
    logger.info(f"Generating replies for {platform}")
    tone = decide_tone(platform, post_text)
    responses = generate_reply_tool(platform, post_text, tone)

    return responses
