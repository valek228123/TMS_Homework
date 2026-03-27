import uuid
from src.models import *
from src.db_conector import engine, session

Base.metadata.create_all(engine)

list_of_products = [
    Products(name="Banana", cost=5, count=10),
    Products(name="Apple", cost=2, count=30),
    Products(name="Pear", cost=3, count=20),
    Products(name="Orange", cost=8, count=8),
    Products(name="Lemon", cost=6, count=13)
]

session.add_all(list_of_products)


def create_str_uuid():
    return str(uuid.uuid4())


list_of_tickets = []
for i in range(20):
    list_of_tickets.append(Tickets(uuid=create_str_uuid()))

session.add_all(list_of_tickets)
session.commit()
