import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from callbacks import register_callbacks
from utils.tabs import get_tabs
from profiles_callback import register_profile_builder_callback

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.CERULEAN])
app.title = "Fast Food & Obesity Dashboard"

app.layout = dbc.Container([
    dbc.Row(dbc.Col([
        html.H2("Fast Food Isn't That Bad!", className="text-center bg-primary text-white p-2"),
        html.H5("Elise Reynolds - CS 150", className="text-center bg-primary text-white p-2"),
    ])),

    dbc.Row([
        dbc.Tabs(get_tabs(), id="tabs", active_tab="tab-overview", style={"marginBottom": "20px"})
    ])
], fluid=True)

register_callbacks(app)
register_profile_builder_callback(app)

if __name__ == '__main__':
    app.run_server(debug=True)