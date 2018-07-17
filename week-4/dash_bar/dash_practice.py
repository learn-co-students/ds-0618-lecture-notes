import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H2('Hello'),
    html.H2('World'),
    dcc.Graph(id="our graph", figure={
        'data': [{'x': ['bart', 'lisa', 'homer'], 'y': [8, 11, 35], 'type': 'bar'}],
        'layout': {
            'title': 'our first graph!'
        }
    }),
    dcc.Graph(id="our second graph", figure={
        'data': [],
        'layout': {
            'title': 'our second graph!'
        }
    })
])

if __name__ == '__main__':
    app.run_server(debug=True)
