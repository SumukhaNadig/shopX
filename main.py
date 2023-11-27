
from fastapi import FastAPI
from models.user_model import Customer, Author
from models.apps_model import App
from models.order_model import Order
from mongodb.database import find_document, insert_one, update_one

app = FastAPI()

@app.get("/")
def read_root():
    return {"App is working"}


@app.post("/users/author/")
async def create_user(user: Author):
    pass


@app.post("/apps/")
async def create_product(app_details: App):
    pass

# below contains all the api endpoints related to customer 
@app.post("/users/customer/add_customer")
async def create_user(user: Customer):
    try:
        documnet_customer = await insert_one(
                collection_name="customer",
                new_data=user
            )
        if documnet_customer.acknowledged:
            return  { "message":"customer was inserted"}
        return { "message":"customer was not inserted"}
    except Exception as e:
        return { "message":"error occured during insertion"}

@app.post("/users/customer/add_order")
async def insert_order(customer_email_id: str, order: Order) -> dict:
    try:
        documnet_order = await insert_one(
            collection_name="order",
            new_data=order
        )
        if documnet_order.acknowledged:
            documnet_customer = await update_one(
                collection_name="customer",
                filter_query={"emailId": customer_email_id},
                updated_data={
                    '$push': {
                        'orders': order.itemId
                        }
                        }
            )
            if documnet_customer.acknowledged:
                return  { "message":"Order was updated"}
        return { "message":"Order was not updated"}
    except Exception as e:
        return { "message":"error occured during insertion"}

@app.get("/users/customer/previous_orders")
async def get_order_list(customer_email_id: str) -> list[Order]|dict:
    try:
        document = await find_document(collection_name="customer",
                                query={"emailId": customer_email_id},
                                multiple=False)
        if document.items():
            order_list = []
            for order_item_id in document["orders"]:
                orders = await find_document(collection_name="order",
                                query={"itemId": order_item_id},
                                multiple=False)
                order_list.append(orders)
            return order_list
        return {"message": "Document was not found"}
    except Exception as e:
        return {}
