from pydantic import BaseModel
from datetime import datetime

class Order(BaseModel):
    _id: str
    sellerId: str
    buyerId: str
    itemId: str
    buyerVpa: str
    timestamp: datetime
