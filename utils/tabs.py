from dash import dcc, html
import dash_bootstrap_components as dbc
from game_tab import get_quiz_tab
from correlation import get_correlation_tab
from profile_builder import get_profile_builder_tab

from utils.figures import (
    make_avg_calorie_bar,
    make_comparison_bar,
    make_fastfood_vs_obesity_scatter,
    make_exercise_vs_obesity_line,
)


def get_tabs():
    return [
        dbc.Tab([
            html.Div([
                html.H4("Overview"),
                dcc.Markdown("""
                    **Is fast food really to blame for the obesity epidemic?**  
                    That’s what we’ve been told—but the truth might surprise you.

                    This dashboard explores that assumption, guiding you through calorie comparisons, lifestyle factors, and an interactive game that tests your own bias.

                    > 🍟 Spoiler: It’s not just the fries.
                """),
            ])
        ], label="Overview", tab_id="tab-overview"),

        dbc.Tab([
            html.Div([
                html.H4("How Bad Is It Really?"),
                html.P("Average calories per fast food item by restaurant (real data)."),
                dcc.Graph(figure=make_avg_calorie_bar()),
                html.Br(),
                html.P("In context, fast food might not be worse than other common meals."),
                dcc.Graph(figure=make_comparison_bar())
            ])
        ], label="How Bad Is It Really?", tab_id="tab-comparison"),

        get_correlation_tab(),

        get_profile_builder_tab(),

        dbc.Tab([
            html.Div([
                html.H4("Obesity is About Lifestyle"),
                html.P("Use the dropdown below to explore how different lifestyle factors relate to obesity class."),
                dcc.Dropdown(
                    id="lifestyle-dropdown",
                    options=[
                        {"label": "Fast Food Consumption", "value": "Consumption_of_Fast_Food"},
                        {"label": "Physical Exercise", "value": "Physical_Excercise"},
                        {"label": "Calories Consumption Frequency", "value": "Calculation_of_Calorie_Intake"},
                        {"label": "Water Consumption Frequency", "value": "Liquid_Intake_Daily"},
                        {"label": "Snack Consumption", "value": "Food_Intake_Between_Meals"}
                    ],
                    value="Consumption_of_Fast_Food",
                    clearable=False,
                    style={"marginBottom": "20px"},
                ),
                dcc.Graph(id="lifestyle-line-chart"),
                html.P(id="lifestyle-summary", style={"fontStyle": "italic", "marginTop": "10px"}),

                html.Div(id="lifestyle-markdown-container", style={"display": "none", "marginTop": "30px"}),
            ])
        ], label="It's About Lifestyle, Not Food", tab_id="tab-lifestyle"),

        get_quiz_tab(),
    ]

