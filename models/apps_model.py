from pydantic import BaseModel, Field, BeforeValidator
from typing import List, Optional
from typing_extensions import Annotated


PyObjectId = Annotated[str, BeforeValidator(str)]


class App(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str
    author: List[str]
    price: float
    description: str
    version: str
    rating: int
    downloads: int

class Apps(BaseModel):
    apps: List[App]

