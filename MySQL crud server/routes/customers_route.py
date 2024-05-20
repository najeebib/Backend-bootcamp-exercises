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
def add_customer(customer: customer_model, db: Session = Depends(get_db)):
    try:
        query = text("""
            INSERT INTO `customers` 
            (customerName, contactLastName, contactFirstName, phone, addressLine1, 
            addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit) 
            VALUES 
            (:customerName, :contactLastName, :contactFirstName, :phone, :addressLine1, 
            :addressLine2, :city, :state, :postalCode, :country, :salesRepEmployeeNumber, :creditLimit)
        """)
        db.execute(
            query,
            {
                "customerName": customer.customerName,
                "contactLastName": customer.contactLastName,
                "contactFirstName": customer.contactFirstName,
                "phone": customer.phone,
                "addressLine1": customer.addressLine1,
                "addressLine2": customer.addressLine2,
                "city": customer.city,
                "state": customer.state,
                "postalCode": customer.postalCode,
                "country": customer.country,
                "salesRepEmployeeNumber": customer.salesRepEmployeeNumber,
                "creditLimit": customer.creditLimit
            }
        )
        db.commit()
        return {"msg": "Customer created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create customer")

@router.put('/customers/{number}')
def edit_customer( number:int, customer: customer_model, db: Session = Depends(get_db)):
    result = db.execute(text(f"SELECT * FROM `customers` WHERE customerNumber = {number}")).fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="Customer not found")
    try:
        query = text("""
            UPDATE `customers` SET
            customerName = :customerName, 
            contactLastName = :contactLastName, 
            contactFirstName = :contactFirstName, 
            phone = :phone, 
            addressLine1 = :addressLine1, 
            addressLine2 = :addressLine2, 
            city = :city, 
            state = :state, 
            postalCode = :postalCode, 
            country = :country, 
            salesRepEmployeeNumber = :salesRepEmployeeNumber, 
            creditLimit = :creditLimit 
            WHERE customerNumber = :customerNumber

        """)
        db.execute(
            query,
            {
                "customerNumber": number,
                "customerName": customer.customerName,
                "contactLastName": customer.contactLastName,
                "contactFirstName": customer.contactFirstName,
                "phone": customer.phone,
                "addressLine1": customer.addressLine1,
                "addressLine2": customer.addressLine2,
                "city": customer.city,
                "state": customer.state,
                "postalCode": customer.postalCode,
                "country": customer.country,
                "salesRepEmployeeNumber": customer.salesRepEmployeeNumber,
                "creditLimit": customer.creditLimit
            }
        )
        db.commit()
        return {"msg": "Customer updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to update customer")
    

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
