from fastapi import APIRouter
from connections import ConnectionManager

router = APIRouter()
manager = ConnectionManager()

@router.get("/messages/count")
async def get_message_count():
    return {"total_messages": manager.total_messages}
