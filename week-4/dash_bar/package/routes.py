import pdb
from package.models import *
from package import app

@app.route('/')
def show():
    customer = Customer.query.get(1)
    return customer.name
