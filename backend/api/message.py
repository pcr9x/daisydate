from fastapi import APIRouter, HTTPException
from zodb_utils import get_zodb_storage

router = APIRouter()

messages_storage = "messages.fs"
root = get_zodb_storage(messages_storage)


@router.post("/messages/{message_key}")
def messages(message_key):
    pass