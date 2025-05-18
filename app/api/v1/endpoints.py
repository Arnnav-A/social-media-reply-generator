from fastapi import APIRouter, HTTPException
from app.models.schemas import ReplyRequest, ReplyResponse
from app.services.reply_generator import generate_reply
from app.db.crud import save_reply

router = APIRouter()

@router.post("/reply", response_model=ReplyResponse)
async def generate_reply_endpoint(payload: ReplyRequest):
    """
    Route to generate replies to a social media post
    """
    try:
        replies = generate_reply(payload.platform, payload.post_text)
        save_reply(payload.platform, payload.post_text, replies)
        return {"generated_replies": replies}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
