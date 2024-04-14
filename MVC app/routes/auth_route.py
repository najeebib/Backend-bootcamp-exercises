from fastapi import APIRouter, HTTPException, Depends
from models.auth_model import Auth_Model


router = APIRouter()

@router.post('/sign_in')
async def sign_in(body:Auth_Model):
    return {"msg": "res"}

@router.options('/sign_in')  # Add route to handle OPTIONS requests
async def options_sign_in():
    return {"msg": "options"}
