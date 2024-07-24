from fastapi import APIRouter
from db import users, products, orders, database
from typing import List
from models import User, UserIn, ProductIn, Product, OrderIn, Order
import datetime

router = APIRouter()

@router.get("/")
async def home():
    return {"Home": "Home"}

@router.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)

@router.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(**user.dict())
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)

@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}

@router.get("/products/", response_model=List[Product])
async def read_products():
    query = products.select()
    return await database.fetch_all(query)

@router.post("/products/", response_model=Product)
async def create_product(prod: ProductIn):
    query = products.insert().values(**prod.dict())
    last_record_id = await database.execute(query)
    return {**prod.dict(), "id": last_record_id}

@router.get("/products/{prod_id}", response_model=Product)
async def read_product(prod_id: int):
    query = products.select().where(products.c.id == prod_id)
    return await database.fetch_one(query)

@router.put("/products/{prod_id}", response_model=Product)
async def update_product(prod_id: int, new_prod: ProductIn):
    query = products.update().where(products.c.id == prod_id).values(**new_prod.dict())
    await database.execute(query)
    return {**new_prod.dict(), "id": prod_id}

@router.delete("/products/{prod_id}")
async def delete_product(prod_id: int):
    query = products.delete().where(products.c.id == prod_id)
    await database.execute(query)
    return {'message': 'product deleted'}

@router.get("/orders/", response_model=List[Order])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)

@router.post("/orders/", response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(**order.dict())
    last_record_id = await database.execute(query)
    return {**order.dict(), "id": last_record_id}

@router.get("/orders/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)

@router.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict(), "id": order_id}

@router.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.update().where(orders.c.id == order_id).values(status=False)
    await database.execute(query)
    return {'message': 'the order is closed'}




