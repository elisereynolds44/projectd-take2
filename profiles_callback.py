import numpy as np
from dash import Input, Output, State
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

import pandas as pd

def register_profile_builder_callback(app):
    df = pd.read_csv("data/Obesity_Dataset -Table 1.csv", header=1)
    features = [
        "Consumption_of_Fast_Food",
        "Physical_Excercise",
        "Calculation_of_Calorie_Intake",
        "Liquid_Intake_Daily",
        "Food_Intake_Between_Meals"
    ]

    X = df[features].dropna()
    y = df.loc[X.index, "Class"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LogisticRegression(multi_class="multinomial", max_iter=1000)
    model.fit(X_scaled, y)

    @app.callback(
        Output("builder-result", "children"),
        Input("builder-submit", "n_clicks"),
        State("builder-fastfood", "value"),
        State("builder-exercise", "value"),
        State("builder-calories", "value"),
        State("builder-water", "value"),
        State("builder-snacks", "value")
    )
    def predict_class(n_clicks, fastfood, exercise, calories, water, snacking):
        if n_clicks is None or None in [fastfood, exercise, calories, water, snacking]:
            return "👆 Adjust the sliders to build a profile and see their predicted obesity class."

        input_array = np.array([[fastfood, exercise, calories, water, snacking]])
        input_scaled = scaler.transform(input_array)
        prediction = model.predict(input_scaled)[0]

        class_labels = {
            1: "Normal",
            2: "Overweight",
            3: "Obese",
            4: "Extremely Obese"
        }

        snark = [
            "Fast food again? Still not the culprit... 🤷‍♀️",
            "Turns out it’s *more* than fries and shakes.",
            "Fast food played a part... or did it?",
            "Someone’s blaming the cheeseburger again 😅",
            "We checked. It’s not the nuggets."
        ]

        return f"Predicted Class: **{class_labels.get(prediction, 'Unknown')}**\n\n{np.random.choice(snark)}"

