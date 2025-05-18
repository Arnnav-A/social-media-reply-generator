from datetime import datetime
from typing import List

from app.db.database import replies_collection

def save_reply(platform: str, post_text: str, generated_reply: List[str]):
    """
    Save a reply to the database
    """
    replies_collection.insert_one({
        "platform": platform,
        "post_text": post_text,
        "generated_reply": generated_reply,
        "timestamp": datetime.now()
    })
