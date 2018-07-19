from restaurants import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    url = db.Column(db.String(100))
    neighborhood_id = db.Column(db.Integer, db.ForeignKey("neighborhoods.id"))
    neighborhood = db.relationship("Neighborhood", back_populates="restaurants")
    rating = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship("Category", back_populates="restaurants")

class Neighborhood(db.Model):
    __tablename__ = 'neighborhoods'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    restaurants = db.relationship("Restaurant", back_populates="neighborhood", lazy="dynamic")

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    restaurants = db.relationship("Restaurant", back_populates="category", lazy="dynamic")
