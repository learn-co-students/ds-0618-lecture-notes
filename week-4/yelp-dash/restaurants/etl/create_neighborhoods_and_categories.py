import pandas as pd
from restaurants import db
from restaurants.models import Neighborhood, Category

yelp_url = 'https://raw.githubusercontent.com/ledeprogram/courses/master/foundations/mapping/tilemill/yelp-lunch-nyc.csv'
records = pd.read_csv(yelp_url)
restaurants = records.to_dict('records')
neighborhoods = list(set(list(map(lambda restaurant: restaurant['City'],restaurants))))
for neighborhood in neighborhoods:
    n = Neighborhood(name=neighborhood)
    db.session.add(n)
db.session.commit()

categories = list(set(list(map(lambda restaurant: restaurant['Category'],restaurants))))
for category in categories:
    c = Category(name=category)
    db.session.add(c)
db.session.commit()
