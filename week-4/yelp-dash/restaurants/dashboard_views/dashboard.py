import dash
import dash_core_components as dcc
import dash_html_components as html
from restaurants import app
import dash_core_components as dcc
import pdb
from restaurants.routes import (neighborhoods as get_neighborhoods,
categories as get_categories,
rating_histogram, restaurants_dictionaries)
import dash_table_experiments as dt


neighborhoods = get_neighborhoods()
categories = get_categories()
restaurant_keys = list(restaurants_dictionaries()[0].keys())


app.layout = html.Div([
    html.H2('Neighborhoods'),
    dcc.Dropdown(
        id='neighborhood-dropdown',
        options=neighborhoods,
        multi=True
    ),
    html.H2('Categories'),
    dcc.Dropdown(
        id='category-dropdown',
        options=categories,
        multi=True
    ),
    dcc.Graph(
        id="star-histogram",
        figure=rating_histogram()

    ),
    dt.DataTable(
        rows=restaurants_dictionaries(),
        columns=restaurant_keys,
        row_selectable=True,
        sortable=True,
        selected_row_indices=[],
        id='datatable-restaurants'
    )
])


@app.callback(
    dash.dependencies.Output('star-histogram', 'figure'),
    [dash.dependencies.Input('neighborhood-dropdown', 'value'),
    dash.dependencies.Input('category-dropdown', 'value')
    ])
def update_histogram(neighborhood_values, category_values):
    hist = rating_histogram(neighborhood_values=neighborhood_values, category_values=category_values)
    return hist

@app.callback(
    dash.dependencies.Output('datatable-restaurants', 'rows'),
    [dash.dependencies.Input('neighborhood-dropdown', 'value'),
    dash.dependencies.Input('category-dropdown', 'value')
    ])
def update_datatable(neighborhood_values, category_values):
    return restaurants_dictionaries(neighborhood_values, category_values)
