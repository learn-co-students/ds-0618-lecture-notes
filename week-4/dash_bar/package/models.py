from package import db

class Bartender(db.Model):
    __tablename__ = 'bartenders'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    hometown = db.Column(db.String(100))
    birthyear = db.Column(db.Integer)
    customers = db.relationship("Customer", secondary="orders", back_populates="bartenders")

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), default=None)
    customer = db.relationship('Customer', back_populates="orders")
    bartender_id = db.Column(db.Integer, db.ForeignKey('bartenders.id'))

    drink_id = db.Column(db.Integer, db.ForeignKey('drinks.id'))

class Drink(db.Model):
    __tablename__ = 'drinks'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    calories = db.Column(db.Text)
    price = db.Column(db.Text)
    alcoholic = db.Column(db.Boolean)

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    hometown = db.Column(db.Text)
    birthyear = db.Column(db.Integer)
    orders = db.relationship(Order, back_populates="customer", lazy="dynamic")
    bartenders = db.relationship("Bartender", secondary="orders", back_populates="customers")
