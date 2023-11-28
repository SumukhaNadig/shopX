import uvicorn
from fastapi import FastAPI
from models.user_model import Customer, Author
from models.apps_model import App, Apps
from models.order_model import Order
from mongodb.database import find_document, insert_one, update_one
from bson.objectid import ObjectId

app = FastAPI()


@app.get("/")
def read_root():
    return {"Welcome to ShopX"}


@app.post("/users/author/")
async def create_user(user: Author):
    pass


@app.get("/apps")
async def get_apps() -> Apps | None:
    try:
        documents: list = await find_document(collection_name="apps",
                                       query={},
                                       multiple=True)
        if documents:
            return Apps(apps = documents)
        return {"message": "No Apps are published, please check back later"}
    except Exception as e:
        return {e}


@app.get("/apps/{app_id}")
async def get_app(app_id:str):
    try:
        document = await find_document(collection_name="apps",
                                       query={"_id": ObjectId(app_id)},
                                       multiple=False)
        if document is not None:
            # This is not a neat solution, i will work on this , but for now it works
            document['id'] = str(document['_id'])
            del[document['_id']]
            return document
        return {"message": "No App found for id"}
    except Exception as e:
        return {e}


# below contains all the api endpoints related to customer


@app.post("/users/customer/add_customer")
async def create_user(user: Customer):
    try:
        document_customer = await insert_one(
            collection_name="customer",
            new_data=user
        )
        if document_customer.acknowledged:
            return {"message": "customer was inserted"}
        return {"message": "customer was not inserted"}
    except Exception as e:
        return {"message": "error occured during insertion"}


@app.post("/users/customer/add_order")
async def insert_order(customer_email_id: str, order: Order) -> dict:
    try:
        document_order = await insert_one(
            collection_name="order",
            new_data=order
        )
        if document_order.acknowledged:
            document_customer = await update_one(
                collection_name="customer",
                filter_query={"emailId": customer_email_id},
                updated_data={
                    '$push': {
                        'orders': order.itemId
                    }
                }
            )
            if document_customer.acknowledged:
                return {"message": "Order was updated"}
        return {"message": "Order was not updated"}
    except Exception as e:
        return {"message": "error occured during insertion"}


@app.get("/users/customer/previous_orders")
async def get_order_list(customer_email_id: str) -> list[Order] | dict:
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
