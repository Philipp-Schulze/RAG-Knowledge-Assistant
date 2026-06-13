from fastapi import APIRouter

from shared.schemas import ChatConversation
from services.backend.chat_conversations import (
    create_chat_conversation,
    get_chat_conversations,
    save_chat_conversation,
)

router = APIRouter()


@router.post("/chat-conversations", response_model=ChatConversation)
def post_chat_conversation():
    return create_chat_conversation()


@router.get("/chat-conversations", response_model=list[ChatConversation])
def get_all_chat_conversations():
    return get_chat_conversations()


@router.put("/chat-conversations/{conversation_id}")
def put_chat_conversation(
    conversation_id: str,
    chat_conversation: ChatConversation
):
    save_chat_conversation(chat_conversation)