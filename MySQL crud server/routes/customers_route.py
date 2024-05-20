from fastapi import APIRouter, Depends, HTTPException, status
from models.customer_model import customer_model
from sqlalchemy.orm import Session
from data.database import get_db
from sqlalchemy import text

router = APIRouter()

@router.get('/customers')
def get_customers(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM `customers`")).fetchall()
    customers = []
    for row in result:
        customers.append(row._mapping)
    return customers

@router.get('/customers/{number}')
def get_customer(number: int, db: Session = Depends(get_db)):
    result = db.execute(text(f"SELECT * FROM `customers` WHERE customerNumber = {number}")).fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="Customer not found")
    return result._mapping

@router.post('/customers')
def add_customer(customer: customer_model):
    pass

@router.put('/customers{number}')
def edit_customer( number:int, customer: customer_model):
    pass

@router.delete('/customers/{number}')
def delete_customer( number: int, db: Session = Depends(get_db)):
    result = db.execute(text(f"SELECT * FROM `customers` WHERE customerNumber = {number}")).fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="Customer not found")
    try:
        db.execute(text(f"DELETE FROM `customers` WHERE customerNumber = {number}"))
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=409, detail="Cannot delete customer: associated orders exist")


    return {"msg": "Customer removed successfully"}
