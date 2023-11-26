from fastapi import FastAPI
from models.user_model import Customer, Author
from models.apps_model import App
from models.order_model import Order
from database import db

app = FastAPI()

@app.get("/")
def read_root():
    return {"App is working"}

@app.post("/users/")
async def create_user(user: Customer):
    pass

@app.post("/apps/")
async def create_product(app: App):
    pass
