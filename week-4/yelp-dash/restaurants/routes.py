from restaurants.models import Neighborhood, Category, Restaurant
from restaurants import db
from sqlalchemy import func



def neighborhoods():
    neighborhoods = Neighborhood.query.all()
    neighborhood_dicts = [{'label': neighborhood.name, 'value': neighborhood.id} for neighborhood in neighborhoods]
    return neighborhood_dicts

def categories():
    categories = Category.query.all()
    category_dicts = [{'label': category.name, 'value': category.id} for category in categories]
    return category_dicts

def category_values(neighborhood_values):
    category_ids = query(Restaurant.category_id).filter(Restaurant.neighborhood_id.in_(neighborhood_values))
    unique_category_ids = list(set(category_ids))
    categories = Category.filter(Category.id.in_(unique_category_ids))
    category_dicts = [{'label': category.name, 'value': category.id} for category in categories]
    return category_dicts


def filter_restaurants(query, neighborhood_values=None, category_values=None):
    if neighborhood_values:
        query = query.filter(Restaurant.neighborhood_id.in_(neighborhood_values))
    if category_values:
        query = query.filter(Restaurant.category_id.in_(category_values))
    return query

def restaurants_dictionaries(neighborhood_values=None, category_values=None):
    restaurants_query = db.session.query(Restaurant)
    filtered_restaurants = filter_restaurants(restaurants_query, neighborhood_values=neighborhood_values,category_values=category_values)
    restaurants = [{'name': restaurant.name, 'category': restaurant.category.name, 'neighborhood': restaurant.neighborhood.name} for restaurant in filtered_restaurants]
    return restaurants

def rating_histogram(neighborhood_values=None, category_values=None):
    ratings_query = db.session.query(Restaurant.rating, func.count(Restaurant.id)).group_by(Restaurant.rating)
    filtered_restaurants = filter_restaurants(ratings_query, neighborhood_values = neighborhood_values, category_values=category_values)
    ratings = filtered_restaurants.all()
    x_values = [rating[0] for rating in ratings]
    y_values = [rating[1] for rating in ratings]
    return {
        'data': [
            {
                'x': x_values,
                'y': y_values,
                'name': 'Trace 1',
                'type': 'bar'
            }
        ],
        'layout': {'xaxis': {'range': [0, 5]}}
    }
        # [(1, 1), (1.5, 9), (2, 33), (2.5, 138), (3, 400), (3.5, 1308), (4, 2596), (4.5, 1202), (5, 124)]
