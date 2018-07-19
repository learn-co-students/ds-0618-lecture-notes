import dash
import dash_core_components as dcc
import dash_html_components as html
from restaurants import app
from restaurants.routes import neighborhoods as get_neighborhoods

neighborhoods = get_neighborhoods()

app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type='text'),
    dcc.Dropdown(
        id='neighborhood-dropdow'
        options=neighborhoods,
        multi=True
    )
])
