import jwt
import json
import utils.db_functions as db_fns
import bcrypt
from dotenv import load_dotenv
import os
from base64 import b64decode as decode

load_dotenv()
secret_key = os.getenv("secret")

def hash_password(password: str) -> str:
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')

def verify_password(stored_pass,user_pass):
    return bcrypt.checkpw(user_pass.encode('utf-8'), stored_pass.encode('utf-8'))

def prepare_new_user_data(password,username, is_admin):
    hashed_password = hash_password(password)
    current_db = db_fns.load_db('./data/users.json')
    current_db[username] = {
        "username":username,
        "password": hashed_password,
        "is_admin": is_admin

    }
    return current_db

def generate_jwt(payload):
    encoded_jwt = jwt.encode(payload, secret_key, algorithm="HS256")   
    print('encoded_jwt: ', encoded_jwt)
    return encoded_jwt

def verify_jwt(user_jwt):
    try:
        data = jwt.decode(user_jwt, secret_key, algorithms="HS256")
        return data["user role"]
    except Exception as e:
        print('e: ', e)
        print("bad token")
        return False

def check_token(request):
        auth_header = request.headers.get('authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            try:
                if verify_jwt(token):
                    return request
            except Exception as e:
                raise e
        return


def check_token_if_admin(request):
        auth_header = request.headers.get('authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            try:
                if verify_jwt(token) == "admin":
                    return request
            except Exception as e:
                raise e
        return

