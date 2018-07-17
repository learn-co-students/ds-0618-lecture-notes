import pdb
from package.models import *
from package import server

@server.route('/')
def show():
    customer = Customer.query.get(1)
    return customer.name

def customer_orders():
    # customers = Customer.query.all().names
    customers = Customer.query.all()
    customer_names = [customer.name for customer in customers]
    number_of_orders_per_customer = [customer.orders.count() for customer in customers]
    # number_of_orders_per_customer = pass

    return {'x': customer_names, 'y': number_of_orders_per_customer, 'name': 'number of orders', 'type': 'bar'}
