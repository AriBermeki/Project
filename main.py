from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from model import Account
from passlib.hash import bcrypt




app = FastAPI()
oauth = OAuth2PasswordBearer(tokenUrl='token')
Account_Pydantic   = pydantic_model_creator(Account, name='Account')
AccountIn_Pydantic = pydantic_model_creator(Account, name='AccountIn', exclude_readonly=True)   
register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models':['model']},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.post('/account', response_model= Account_Pydantic) # Account_Pydantic is the Output
async def create_account(account: AccountIn_Pydantic): # account is the Input
    account_obj = Account(
        first_name = account.first_name,
        last_name = account.last_name,
        birth_data = account.birth_date,
        address = account.address,
        city = account.city,
        email = account.email,
        username = account.username,
        is_admin = account.is_admin,
        is_active = account.is_active,
        is_staff = account.is_staff,
        is_superuser = account.is_superuse,
        password = bcrypt.hash(account.password),
        confirm_password = bcrypt.hash(account.confirm_password)
    )
    await account_obj.save()
    return await Account_Pydantic.from_tortoise_orm(account_obj)



@app.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return{'access_token': form_data.username}

@app.get('/')
async def index(token: str = Depends(oauth)):
    return {'the_token', token}
