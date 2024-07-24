from settings import settings
import databases
import sqlalchemy
from sqlalchemy import create_engine


DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


#Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
products = sqlalchemy.Table( 
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key = True),
    sqlalchemy.Column("title", sqlalchemy.String(32), nullable = False),
    sqlalchemy.Column("description", sqlalchemy.String(128), nullable = True),
    sqlalchemy.Column("price", sqlalchemy.Float, nullable = False),
)

#  id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль
users = sqlalchemy.Table( 
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key = True),
    sqlalchemy.Column("name", sqlalchemy.String(32), nullable = False),
    sqlalchemy.Column("surname", sqlalchemy.String(32), nullable = False),
    sqlalchemy.Column("email", sqlalchemy.String(128), nullable = True),
    sqlalchemy.Column("password", sqlalchemy.String(32), nullable = False)
)

#Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
orders = sqlalchemy.Table(  
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key = True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable = False),
    sqlalchemy.Column("products_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('products.id'), nullable = False),
    sqlalchemy.Column("date_of_submission", sqlalchemy.DateTime),
    sqlalchemy.Column("status", sqlalchemy.Boolean)
)





engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)