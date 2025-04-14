from dash import dcc, html
import dash_bootstrap_components as dbc

def get_correlation_tab():
    return dbc.Tab([
        html.Div([
            html.H4("Lifestyle Factor Correlations"),
            html.P("Select the lifestyle variables you're curious about and see how they correlate with one another."),

            dcc.Checklist(
                id="correlation-checklist",
                options=[
                    {"label": label.replace("_", " "), "value": label} for label in [
                        'Overweight_Obese_Family',
                        'Consumption_of_Fast_Food',
                        'Frequency_of_Consuming_Vegetables',
                        'Number_of_Main_Meals_Daily',
                        'Food_Intake_Between_Meals',
                        'Smoking',
                        'Liquid_Intake_Daily',
                        'Calculation_of_Calorie_Intake',
                        'Physical_Excercise',
                        'Schedule_Dedicated_to_Technology',
                        'Type_of_Transportation_Used'
                    ]
                ],
                value=["Consumption_of_Fast_Food", "Physical_Excercise"],
                labelStyle={"display": "block"},
                style={"marginBottom": "20px"},
            ),

            dcc.Graph(id="correlation-heatmap"),
            html.Div(id="correlation-warning", style={"color": "red"})
        ])
    ], label="Lifestyle Correlations", tab_id="tab-correlation")
