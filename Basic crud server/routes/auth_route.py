from fastapi import APIRouter, HTTPException, Depends
import utils.auth_functions as auth_fns
import utils.db_functions as db_fns
from models.auth_model import Auth_Model
from modules.logger import Logger

router = APIRouter()

@router.post('/auth/sign_up')
async def sign_up(body:Auth_Model, log = Depends(Logger.log_request)):
    # hash the user password and add them to db
    updated_db = auth_fns.prepare_new_user_data(body.password, body.username, body.is_admin)
    # save db to file
    db_fns.save_to_db(updated_db)
    if body.is_admin:
        auth_token = auth_fns.generate_jwt({"user role": "admin"})
    else:
        auth_token = auth_fns.generate_jwt({"user role": "guest"})
    return {"msg":"user created","token":auth_token}

@router.post('/auth/sign_in')
async def sign_in(body:Auth_Model, log = Depends(Logger.log_request)):
    try:
        stored_user = db_fns.find_user_in_db(body.username)
        if stored_user:
            stored_pass = stored_user["password"]
            is_admin = stored_user["is_admin"]
            # compare the request password to the password saved in file
            if auth_fns.verify_password(stored_pass, body.password):
                if is_admin:
                    auth_token = auth_fns.generate_jwt({"user role":"admin"})
                else:
                    auth_token = auth_fns.generate_jwt({"user role":"guest"})
                return {"msg":"user sign in successfully","token":auth_token}
            else:
                raise HTTPException(403, "Invalid credntials")
        else:
            raise HTTPException(404, "No user found")
    except FileNotFoundError as e:
        print(e)
        raise HTTPException(404, "No users db found")
