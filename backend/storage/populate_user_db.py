from models import user
import ZODB
from ZODB.FileStorage import FileStorage
import transaction, uuid
from api import user as u
from pydantic import EmailStr
from datetime import datetime
from passlib.context import  CryptContext

root = u.root
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

user1 = user.UserInfo(
    name="user1",
    email=EmailStr("user1@gmail.com"),
    phone_number="797097979",
    password= pwd_context.hash("pass1"),
    date_of_birth=datetime(2000, 2, 28, 12, 0, 0).replace(year=1999, month=1, day=1),
    age=20,
    id=str(uuid.uuid4())
)

user2 = user.UserInfo(
    name="user2",
    email=EmailStr("user2@gmail.com"),
    phone_number="397097979",
    password= pwd_context.hash("pass2"),
    date_of_birth=datetime(2000, 2, 28, 12, 0, 0).replace(year=1998, month=1, day=1),
    age=20,
    id=str(uuid.uuid4())
)

user3 = user.UserInfo(
    name="user3",
    email=EmailStr("user3@gmail.com"),
    phone_number="797097279",
    password= pwd_context.hash("pass3"),
    date_of_birth=datetime(2000, 2, 28, 12, 0, 0).replace(year=1997, month=1, day=1),
    age=20,
    id=str(uuid.uuid4())
)

user4 = user.UserInfo(
    name="user4",
    email=EmailStr("user4@gmail.com"),
    phone_number="797091279",
    password= pwd_context.hash("pass4"),
    date_of_birth=datetime(2000, 2, 28, 12, 0, 0).replace(year=1996, month=1, day=1),
    age=20,
    id=str(uuid.uuid4())
)

root[user1.id] = user1
root[user2.id] = user2
root[user3.id] = user3
root[user4.id] = user4

transaction.commit()