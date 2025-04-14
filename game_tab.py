from dash import html, dcc
import dash_bootstrap_components as dbc

def get_quiz_tab():
    return dbc.Tab(
        html.Div([
            html.H4("Game: Obesity Predictor"),
            dcc.Store(id="quiz-state"),
            html.Div([
                html.H5("Guess the Obesity Class!"),
                html.P("Click start to reveal a person's lifestyle details and try to guess their obesity class."),
                html.Button("Start Game", id="start-quiz-game", n_clicks=0, className="btn btn-primary")
            ]),
            html.Div(id="quiz-question", style={"marginTop": "15px"}),
            html.Div([
                dcc.RadioItems(
                    id="quiz-guess",
                    options=[
                        {"label": "Normal (1)", "value": 1},
                        {"label": "Overweight (2)", "value": 2},
                        {"label": "Obese (3)", "value": 3},
                        {"label": "Extremely Obese (4)", "value": 4},
                    ],
                    labelStyle={"display": "block"},
                    style={"marginBottom": "15px"},
                ),
                dbc.Button("Submit Guess", id="submit-guess", color="primary", className="me-2"),
                dbc.Button("Next Round", id="next-round", color="secondary", className="me-2", disabled=True),
            ], style={"marginTop": "10px"}),
            html.Div(id="quiz-feedback", className="mb-2", style={"marginTop": "15px", "fontWeight": "bold"}),
            html.Div(id="quiz-score", style={"marginTop": "10px"}),
        ]),
        label="Game: Obesity Predictor",
        tab_id="tab-quiz"
    )
