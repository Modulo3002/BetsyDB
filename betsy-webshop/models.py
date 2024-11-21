# Models go here
from peewee import *

db = SqliteDatabase('betsy.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = CharField()
    address = TextField()
    billing_info = TextField()

class Product(BaseModel):
    user = ForeignKeyField(User, backref='products')
    name = CharField(index=True)  # Addedthe index to name
    description = TextField(index=True)  # Added index to the description
    price = DecimalField(decimal_places=2, auto_round=True, constraints=[Check('price > 0')])
    quantity = IntegerField(constraints=[Check('quantity >= 0')])

    class Meta:
        indexes = (
            (('name', 'description'), False),
        )

class Tag(BaseModel):
    name = CharField(unique=True)

class ProductTag(BaseModel):
    product = ForeignKeyField(Product, backref='tags')
    tag = ForeignKeyField(Tag, backref='products')

class Transaction(BaseModel):
    buyer = ForeignKeyField(User, backref='purchases')
    product = ForeignKeyField(Product, backref='transactions')
    quantity = IntegerField()
    total_price = DecimalField(max_digits=10, decimal_places=2)
    date = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

def initialize_database():
    db.connect()
    db.create_tables([User, Product, Tag, ProductTag, Transaction], safe=True)