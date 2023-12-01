from pydantic import BaseModel, Field, BeforeValidator
from typing import List, Optional,Annotated
from bson import ObjectId

PyObjectId = Annotated[str, BeforeValidator(str)]

class Author(BaseModel):
    id: Optional[PyObjectId] = Field(default=None)
    name: str
    emailId: str
    password: str
    apps: List[PyObjectId]
    vpa: str
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

class Customer(BaseModel):
    _id: str
    name: str
    emailId: str
    password: str
    orders: List[str]
