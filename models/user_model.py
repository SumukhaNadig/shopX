from pydantic import BaseModel
from typing import List

class Author(BaseModel):
    _id: str
    name: str
    emailId: str
    password: str
    apps: List[str]
    vpa: str
    
class Customer(BaseModel):
    _id: str
    name: str
    emailId: str
    password: str
    orders: List[str]
