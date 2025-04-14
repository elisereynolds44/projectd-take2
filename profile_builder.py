from dash import html, dcc
import dash_bootstrap_components as dbc

def get_profile_builder_tab():
    return dbc.Tab([
        html.Div([
            html.H4("Build-A-Person: Predict Their Obesity Class"),
            html.P("Try tweaking lifestyle features to see how obesity class changes. Spoiler: It's not just about fast food..."),

            dcc.Slider(
                id="builder-fastfood",
                min=0,
                max=3,
                marks={i: f"{i}" for i in range(4)},
                value=1,
                tooltip={"placement": "bottom"},
            ),
            html.P("🍔 Fast Food Consumption (0 = Never, 3 = Often)", style={"marginTop": "-10px"}),

            dcc.RadioItems(
                id="builder-exercise",
                options=[{"label": "Yes", "value": 1}, {"label": "No", "value": 0}],
                value=1,
                labelStyle={"display": "inline-block", "marginRight": "10px"}
            ),
            html.P("Physical Exercise"),

            dcc.Input(id="builder-calories", type="number", placeholder="Calories per meal", value=500),
            html.Br(),

            dcc.Input(id="builder-water", type="number", placeholder="Water intake (liters/day)", value=2.0),
            html.Br(),

            dcc.Slider(
                id="builder-snacks",
                min=0,
                max=3,
                marks={i: f"{i}" for i in range(4)},
                value=1,
                tooltip={"placement": "bottom"},
            ),
            html.P("Snacking Frequency (0 = Never, 3 = Frequent)", style={"marginTop": "-10px"}),

            dbc.Button("Predict Class", id="builder-submit", color="primary", className="mt-3"),
            html.Div(id="builder-result", style={"marginTop": "20px", "fontWeight": "bold"}),
        ])
    ], label="Build-A-Person", tab_id="tab-builder")