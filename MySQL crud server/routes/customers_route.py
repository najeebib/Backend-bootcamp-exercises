from fastapi import APIRouter, WebSocket,WebSocketDisconnect, Depends
from models.customer_model import customer_model
router = APIRouter()

@router.get('/customers')
def get_customers():
    pass

@router.get('/customers/{id}')
def get_customer(id: int):
    pass

@router.post('/customers')
def add_customer(customer: customer_model):
    pass

@router.put('/school/students/{id}')
def edit_customer( id:int, customer: customer_model):
    pass

@router.delete('/school/students/{id}')
def delete_customer( id: int):
    pass
