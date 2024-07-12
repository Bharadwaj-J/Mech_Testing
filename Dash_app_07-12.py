from dash import Dash, dcc, Input, Output, html
import dash_bootstrap_components as dbc
from backend import start_treadmill

app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

# Components
page_title = dcc.Markdown('# FARMWISE TREADMILL TEST SETUP')

speed = html.Div(
    [
        html.P("Enter Speed [Range -2.78 - 6.95 m/s]"),
        dbc.Input(id='speed', type="number", value=0, min=-2.78, max=6.95, size="lg"),
    ],
)

start_button = html.Div(
    [
        dbc.Button(
            "START", id="start-button", className="me-2", n_clicks=0
        ),
        html.Span(id="start-output", style={"verticalAlign": "middle"}),
    ]
)

stop_button = html.Div(
    [
        dbc.Button(
            "STOP", id="stop-button", className="me-2", n_clicks=0
        ),
        html.Span(id="stop-output", style={"verticalAlign": "middle"}),
    ]
)

# Customize your own Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([page_title], width=12),
    ], justify='center'),

    dbc.Row([
        dbc.Col([start_button], width=2),
    ], justify='center'),

    dbc.Row([
        dbc.Col([speed], width=3),
    ], justify='center'),

    dbc.Row([
        dbc.Col([stop_button], width=2),
    ], justify='center'),
])

# Callback decorator
@app.callback(
    Output('start-output', 'children'),
    [Input('speed', 'value'),
     Input('start-button', 'n_clicks'),
     Input('stop-button', 'n_clicks')]
)
def treadmill(speed, start_clicks, stop_clicks):
    if start_clicks > 0:
        return f"Treadmill started at speed: {speed} m/s"
    elif stop_clicks > 0:
        return "Treadmill stopped"
    return "Awaiting action..."

if __name__ == "__main__":
    app.run(debug=True)