from pydantic import BaseModel, Field
from typing import List, Optional


class Author(BaseModel):
    id: str
    name: str
    emailId: str
    password: str
    apps: List[str]
    vpa: str

class Authors(BaseModel):
    apps: List[Author]

class Customer(BaseModel):
    _id: str
    name: str
    emailId: str
    password: str
    orders: List[str]
