from fastapi import APIRouter, HTTPException, Depends, Request
import utils.db_functions as db_fns
from fastapi.templating import Jinja2Templates
import utils.db_functions as db_fns

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get('/products')
async def sign_in(request: Request):
    products = db_fns.load_db("./data/products.json")
    return templates.TemplateResponse("products.html", {"request": request, "products": products})
