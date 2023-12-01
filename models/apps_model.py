from pydantic import BaseModel, Field, BeforeValidator
from typing import List, Optional, Union
from typing_extensions import Annotated
from models.user_model import PyObjectId
from bson import ObjectId

class App(BaseModel):
    id: Optional[PyObjectId] = Field(default=None)
    name: str
    authors: List[PyObjectId] = Field(default_factory=lambda: [ObjectId()])
    price: float
    description: str
    version: str
    rating: int
    downloads: int

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

class Apps(BaseModel):
    apps: List[App]

