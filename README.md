# shopX
Repo for the Ecommerece Project (https://github.com/abhibansal60/backend-mentorship)

## shopX: A Marketplace for Gen AI Apps


# Table Of Contents

[Setting up your dev environment](#setting-up-your-dev-environment)

## Setting up your dev environment

1. Clone the project
2. Open the path/to/project/shopx
3. Configure the location of your MongoDB database:
    `export MONGODB_URL="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"`

    For Powershell:
    ` $env:MONGODB_URL="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"`
4. Run the following commands to run the app
   `pip install -r requirements.txt`
   `python -m uvicorn main:main --reload`
5. Your app should be running on http://127.0.0.1:8000 



### ShopX Models

1. **Apps**: Gen AI Apps or products sold on shopX
   1. /apps [GET] - A catalog of all the published Apps
   2. /apps/{id} [GET] - A particular app details by app id

**_Note:_** All our apps are paid apps on ShopX 

```shell
{
  "_id": {
    "$oid": "65621dfb717ca4ecc190571e"
  },
  "name": "Backend GPT",
  "author": ["John Doe", "Jane Doe"],
  "price": 4.99,
  "description": "This Gen AI app helps you answer your Backend Development questions",
  "version": "0.0.1",
  "rating":0,
  "downloads":0
}
```
1. **Author** : A person using the shopX
   1. /authors/apps [GET] - Get all the apps by an author
   2. /authors/app - [POST] - Create or submit a new app by author
   3. /authors/{appid} - [DELETE] - Delete an app by id, query param of author id

```shell
{
  "_id": {
    "$oid": "65622239717ca4ecc1905720"
  }, 
  "name": "John Doe",
  "emailId": "john@shopx.com",
  "password": "#hashedU$ERP@ss",
  "apps": [],
  "vpa": "john@upi"
  
}
```

1. **Customer** : A person purchasing the apps:
   1. /customer - [POST] - Add a customer 
   2. /customer/orders - [GET] - Details about customers previous orders
   3. /customer/order -[POST] - A customer placing the order

```shell
{
  "_id": {
    "$oid": "65622ab21536a5c470f57099"
  },
  "name": "Jack Sparrow",
  "emailId": "jack@abc.com",
  "password": "#hashedpw",
  "orders": []
}
```
   
2. **Order** : A static collection containing orders by customers
   1. /order/{id} - [GET] - Get order ID

```shell
{
  "_id": {
    "$oid": "65622d2a1536a5c470f570aa"
  },
  "sellerId": "<seller-id>",
  "buyerId": "<buyer-id>",
  "itemId": "<app-id>",
  "buyerVpa": "user@upi",
  "timestamp": "datetime.now()"
}
```

## Containerizing the App with Docker

1. Created the [Dockerfile](/Dockerfile) with python:3.11 base image.
2. Building the docker image 
   `docker build -t shopx .`
3. Running the container locally
   `docker run -dp 127.0.0.1:8000:8000 -e $MONGODB_URL shopx`
4. Pushing the container to the Docker Registry
   ```shell
   MONGODB_URL="mongodb+srv://<username>:<username>@<cluster>.mongodb.net/"
   docker run -dp 0.0.0.0:8000:8000 -e MONGODB_URL=$MONGODB_URL abhibansal999/shopx:2023-12-02--24-34
   ```
5. You can optionally deploy your app on a free instance of [Play with Docker Labs](https://labs.play-with-docker.com/)

## Contributors

- Anthony Clinton 
- Sumukha
- Siddharta Shandilya
- Abhinav Bansal


