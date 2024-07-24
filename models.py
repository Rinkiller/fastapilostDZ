from datetime import datetime
from pydantic import BaseModel, Field


class UserIn(BaseModel):   #  id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль
    name: str = Field(..., min_length=2, max_length=32, title="name")
    surname: str = Field(..., min_length=2, max_length=32, title="surname")
    email: str = Field(..., max_length=128, title="email")
    password: str = Field(..., min_length=6, title="password")

class User(UserIn):
    id: int

#Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
class ProductIn(BaseModel):  
    title : str = Field(...,min_length=2, max_length=32)             
    description : str = Field(..., min_length=2, max_length = 128)      
    price: float = Field(...)     

class Product(ProductIn):
    id: int

#Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
class OrderIn(BaseModel):  
    user_id : int = Field(...)
    products_id : int = Field(...)
    date_of_submission : datetime = datetime.utcnow
    status : bool = True

class Order(OrderIn):
    id: int
