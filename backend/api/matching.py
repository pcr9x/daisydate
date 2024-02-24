from fastapi import APIRouter, HTTPException
from zodb_utils import get_zodb_storage

router = APIRouter()

user_storage = "users.fs"
root = get_zodb_storage(user_storage)


def user_screening(user):
    pref_age = user.preferences.age
    filtered_user = [
        p
        for p in user
        if pref_age[0] <= p.age <= pref_age[1] and user.preferences.gender == p.gender
    ]
    return filtered_user

def user_searching(user, search):
    pass


def user_swiping(current_user, user, liked):
    if liked:
        message_key = current_user.id + user.id
    
    return message_key