from datetime import datetime
from typing import Optional
from pydantic import BaseModel, BaseConfig, BaseSettings, EmailStr
from dataclasses import dataclass


@dataclass
class Account(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    birth_date: str
    address: str
    city:  Optional[str]
    profile_picture: Optional[str]
    bio:   Optional[str]
    email : EmailStr
    username : str
    date_joined: Optional[datetime.now]
    last_login: Optional[datetime.now]
    is_admin: bool
    is_active: bool
    is_staff: bool
    is_superuse: bool
    password: str
    confirm_password: str


user1 = {
    'id':'125',
    'first_name':'Malek', 
    'last_name':'Ali', 
    'birth_data':'20.01.1996', 
    'address':'Boxhagener Str. 58,10245', 
    'city':'Berlin', 
    'bio':'Ingenieur',  
    'avatar':'CTO',
    'email' :'ari.bermeki@icloud.com',
    'username':'ari.bermeki',								
    'is_admin'	:True,			
    'is_active'	:True,		
    'is_staff':True,			
    'is_superuser':True,			
    'password' :'323691Malek' ,             
    'confirm_password':'323691Malek'
}

ari = Account(**user1)
print(ari)

# @dataclass   
# class Connections(BaseModel):

#     sender_id: int
#     receiver_id: int




# @dataclass
# class Circle(BaseModel):

#     name: str
#     description: str
#     creator_id : int
#     members: str
#     image: str




# @dataclass
# class Message(BaseModel):
#     sender_id: int
#     receiver_id: int
#     nachricht: str




# @dataclass
# class Post(BaseModel):
#     circle_id: int
#     user_id: int
#     date: str #Optional[datetime]
#     time: str #Optional[datetime.utcnow]




# @dataclass
# class Reaction(BaseModel):
#     post_id: int
#     user_id: int
#     type: str




# @dataclass
# class Comment(BaseModel):
#     post_id: int
#     user_id: int
#     content: str
#     date: str #Optional[datetime]
#     time: str #Optional[datetime.utcnow]