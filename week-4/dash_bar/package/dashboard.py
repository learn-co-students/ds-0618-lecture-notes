import dash_html_components as html
import dash_core_components as dcc
from package import app
from package.routes import customer_orders

customer_orders_trace = customer_orders()

app.layout = html.Div(children=[
    dcc.Graph(id="our second graph", figure={
        'data': [customer_orders_trace],
        'layout': {
            'title': 'our second graph!'
            }
        })

    ])
