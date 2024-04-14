from fastapi import APIRouter, HTTPException, Depends
from models.auth_model import Auth_Model
import utils.db_functions as db_fns
import utils.auth_functions as auth_fns


router = APIRouter()


@router.post('/sign_in')
async def sign_in(body:Auth_Model):
    try:
        users_db = db_fns.load_db('./data/users.json')
        stored_user = auth_fns.find_user_in_db(body.email, users_db)
        if stored_user:
            stored_pass = stored_user["password"]
            # compare the request password to the password saved in file
            if auth_fns.verify_password(stored_pass, body.password):
                auth_token = auth_fns.generate_jwt({"user logged":"yes"})
                return {"msg":"user sign in successfully","token":auth_token}
            else:
                raise HTTPException(403, "Invalid credntials")
        else:
            # hash the user password and add them to db
            updated_db = auth_fns.prepare_new_user_data(body.password, body.email)
            # save db to file
            db_fns.save_to_db(updated_db, './data/users.json')
            auth_token = auth_fns.generate_jwt({"user logged":"yes"})
            return {"msg":"user created","token":auth_token}
    except FileNotFoundError as e:
        print(e)
        raise HTTPException(404, "No users db found")

@router.options('/sign_in')  # Add route to handle OPTIONS requests
async def options_sign_in():
    return {"msg": "options"}
