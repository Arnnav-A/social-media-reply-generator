from pydantic import BaseModel
from typing import Literal, List

class ReplyRequest(BaseModel):
    platform: Literal["twitter", "linkedin", "insta"]
    post_text: str

class ReplyResponse(BaseModel):
    generated_replies: List[str]
