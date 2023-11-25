# shopX
Repo for the Ecommerece Project (https://github.com/abhibansal60/backend-mentorship)

## shopX: A Marketplace for Gen AI Apps


### ShopX Models

1. Products catalogue:
   1. /apps [GET] - A Catalogue of Apps
   2. /apps/{id} [GET] - Look for a particular app by app id

Product Document: **All our apps are paid apps on ShopX** 
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
1. Author : A person using the ShopX
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

1. Customer : A person purchasing the apps:
   1. /customer - [POST] - Add a customer 
   2. /customer/orders - [GET] - Details about customers previous orders
   3. /customer/order -[POST] - A customer placing the order
   
1. Order : A static collection containing orders by customers
   1. /order/{id} - [GET] - Get order ID