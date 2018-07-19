import pandas as pd
from restaurants import db
from restaurants.models import Neighborhood, Category, Restaurant

yelp_url = 'https://raw.githubusercontent.com/ledeprogram/courses/master/foundations/mapping/tilemill/yelp-lunch-nyc.csv'
records = pd.read_csv(yelp_url)
restaurants = records.to_dict('records')

for restaurant in restaurants:
    category = Category.query.filter_by(name=restaurant["Category"]).first()
    category_id = category.id

    neighborhood = Neighborhood.query.filter_by(name=restaurant["City"]).first()
    neighborhood_id = neighborhood.id
    if Restaurant.query.filter_by(name=restaurant["Name"], neighborhood_id=neighborhood_id).count() == 0:
        restaurant = Restaurant(
            name=restaurant["Name"],
            url=restaurant["URL"],
            category=category,
            rating=restaurant["Rating"],
            neighborhood=neighborhood
        )
        db.session.add(restaurant)

db.session.commit()
