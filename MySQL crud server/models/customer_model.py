from pydantic import BaseModel
class customer_model(BaseModel):
    customerName: str
    contactLastName: str
    contactFirstName: str
    phone: str
    addressLine1: str
    addressLine2: str = None
    city: str
    state: str = None
    postalCode: str = None
    country: str
    salesRepEmployeeNumber: int = None
    creditLimit: float = None

