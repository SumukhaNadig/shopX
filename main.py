import uvicorn
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI, HTTPException
from models.user_model import Customer, Author
from models.apps_model import App, Apps
from models.order_model import Order
from mongodb.database import find_document, insert_one, update_one, validate_object_id, db
from bson import ObjectId

app = FastAPI()


@app.get("/")
def read_root():
    return {"Welcome to ShopX"}


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
    

@app.post("/app")
async def create_app(app: App):
    try:
        document = jsonable_encoder(app, exclude=["id"])
        document["authors"] = [ObjectId(author) for author in document["authors"]]
        result = await db['apps'].insert_one(document)
        if not result:
            raise HTTPException(status_code=400, detail="App could not be created")
        return {"App": f"{result.inserted_id} id created successfully!"}
    
    except Exception as e:
        return {e}

@app.post("/user/author")
async def create_author(author: Author):
    try:
        document = jsonable_encoder(author, exclude=["id"])
        document["apps"] = [ObjectId(app) for app in document["apps"]]
        result = await db['authors'].insert_one(document)
        if not result:
            raise HTTPException(status_code=400, detail="Author could not be created")
        return {"Author": f"{result.inserted_id} id created successfully!"}
    except Exception as e:
        return {"message": str(e)}
   

@app.get("/authors")
async def get_authors() -> list[Author]:
    try:
        documents: list = await find_document(collection_name="authors",
                                       query={},
                                     multiple=True)
        if documents:
            for document in documents:
                document['id'] = str(document['_id'])
                del[document['_id']]
                document["apps"] = [str(app) for app in document["apps"]]

            return documents
        return {"message": "No Authors, please check back later"}
    except Exception as e:
        return {e}


@app.get("/users/author/{author_id}")
async def get_app(author_id:str):
    try:
        document = await find_document(collection_name="authors",
                                       query={"_id": ObjectId(author_id)},
                                       multiple=False)
        if document is not None:
            document['id'] = str(document['_id'])
            del[document['_id']]
            document['apps'] = [str(app) for app in document['apps']]
            return document
        return {"message": "No Author found for id"}
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

# API endpoints for order collection
@app.get("/orders/{order_id}")
async def get_order(order_id: str) -> dict:
    try:
        validated_order_id = await validate_object_id(order_id)
        print(validated_order_id)
        document = await find_document(collection_name="order",
                                query={"_id": validated_order_id},
                                multiple=False)
        
        if document:
            document["_id"] = str(document["_id"])
            return document
        return {"message": "Document was not found"}
    except Exception as e:
        return {}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
