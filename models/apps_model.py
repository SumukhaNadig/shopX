from pydantic import BaseModel
from typing import List

class App(BaseModel):
    _id: str
    name: str
    author: List[str]
    price: float
    description: str
    version: str
    rating: int
    downloads: int

