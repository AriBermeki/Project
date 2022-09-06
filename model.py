from tortoise.models import Model
from tortoise import fields
from typing import Optional
from datetime import datetime


class Account(Model):
    id                                   = fields.IntField(pk=True)
    first_name                           = fields.CharField(80)
    last_name                            = fields.CharField(80)
    birth_date                           = fields.DateField()
    address                              = fields.CharField(80)
    city                                 = fields.CharField(20)                  
    email                                = fields.CharField(255)          
    username                             = fields.CharField(100, unique= True)       
    is_admin                             = fields.BooleanField()
    is_active                            = fields.BooleanField()
    is_staff                             = fields.BooleanField()
    is_superuse                          = fields.BooleanField() 
    password                             = fields.CharField(128)
    confirm_password                     = fields.CharField(128)
    

    @classmethod
    async def get_account(cls, username):
        return cls.get(username=username)
    
   
    def verify_password(self, password):
        return True