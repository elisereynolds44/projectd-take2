import dash
import random
from dash import Input, Output, State, callback, html, callback_context, dcc
import pandas as pd
import plotly.express as px
from mistune import markdown
from game import get_random_person, get_class_label

def register_callbacks(app):
    @app.callback(
        Output("lifestyle-line-chart", "figure"),
        Output("lifestyle-summary", "children"),
        Output("lifestyle-markdown-container", "children"),
        Output("lifestyle-markdown-container", "style"),
        Input("lifestyle-dropdown", "value"),
    )

    def update_lifestyle_chart(selected_dropdown_value):
        df = pd.read_csv("data/Obesity_Dataset -Table 1.csv", header=1)

        if selected_dropdown_value not in df.columns:
            return px.line(title="Invalid feature"), "No data available for this selection."

        grouped = df.groupby(selected_dropdown_value)["Class"].mean().reset_index()


        fig=px.line(
            grouped,
            x=selected_dropdown_value,
            y="Class",
            markers=True,
            title=f"Obesity Dataset vs {selected_dropdown_value.replace('_', ' ')}",
            labels={
                selected_dropdown_value: selected_dropdown_value.replace('_', ' '),
                "Class": "Average Obesity Class",
            }
        )

        summary_texts = {
            "Consumption_of_Fast_Food": "Obesity levels barely increase as fast food consumption rises.",
            "Physical_Excercise": "A small drop in obesity class with more exercise — not a dramatic shift.",
            "Calculation_of_Calorie_Intake": "People who eat more calories don’t show significant obesity differences.",
            "Liquid_Intake_Daily": "Higher liquid intake doesn’t correlate clearly with lower obesity.",
            "Food_Intake_Between_Meals": "Snacking frequency shows minor differences in obesity class."
        }

        summary = summary_texts.get(selected_dropdown_value, "")

        fig.update_layout(xaxis_title=selected_dropdown_value.replace('_', ' '), yaxis_title="Avg Obesity Class")

        markdown_content = dcc.Markdown("""
    ### Obesity Class Insights from Lifestyle Factors

    - The **average obesity class** in this dataset is **2.68**, which falls between *Overweight* and *Obese*.
    - The **most common class** is **2** (*Overweight*).
    - Lifestyle features most **positively correlated** with higher obesity class:
        - **Age** (0.58)
        - **Number of Main Meals Daily** (0.51)
        - **Lack of Physical Exercise** (0.39)
    - Lifestyle features most **negatively correlated** with obesity:
        - **Frequent Vegetable Consumption** (-0.54)
        - **Lower Fast Food Consumption** (-0.38)
        - **Active Transportation (e.g., walking, biking)** (-0.36)

    These correlations suggest that while fast food has a role, other lifestyle choices like meal frequency, age, and exercise have stronger predictive power.
    """, style={"marginTop": "30px"})

        return fig, summary, markdown_content, {"display": "block", "marginTop": "30px"}

    @callback(
        Output("quiz-question", "children"),
        Output("quiz-state", "data"),
        Output("quiz-score", "children"),
        Output("quiz-feedback", "children"),
        Output("quiz-guess", "value"),
        Output("submit-guess", "disabled"),
        Output("next-round", "disabled"),
        Input("start-quiz-game", "n_clicks"),
        Input("submit-guess", "n_clicks"),
        Input("next-round", "n_clicks"),
        State("quiz-guess", "value"),
        State("quiz-state", "data"),
        prevent_initial_call=True
    )
    def handle_game(start, submit, next_, guess, state):
        trigger = callback_context.triggered_id

        if trigger == "start-quiz-game" or state is None:
            description, answer = get_random_person()
            state = {"score": 0, "round": 1, "answer": answer}
            return (
                html.Ul([html.Li(d) for d in description]),
                state,
                "Score: 0/0",
                "Make your guess below!",
                None,
                False,  # submit enabled
                True  # next round disabled
            )

        if trigger == "submit-guess":
            if guess is None:
                return dash.no_update, dash.no_update, dash.no_update, "Please make a guess!", dash.no_update, False, True

            actual = state["answer"]
            correct = int(guess) == actual
            state["score"] += int(correct)

            snark = [
                "Guess what? They love fast food — and they're *not* obese. 🤯",
                "Shocking: this person rarely touches fast food. 😇",
                "This isn’t a burger problem. It’s more nuanced. 🍔✨",
                "Fast food didn’t do this alone. Don’t blame the fries. 🍟",
                "Obesity? More than just drive-thrus and nuggets. 💁‍♀️"
            ]

            feedback = (
                           "✅ Correct!" if correct else f"❌ Not quite! The correct class was {get_class_label(actual)}."
                       ) + " " + random.choice(snark)

            if state["round"] >= 5:
                return (
                    "Game over! Refresh to play again.",
                    {},
                    f"Final Score: {state['score']}/5",
                    feedback,
                    None,
                    True,  # submit disabled
                    True  # next disabled
                )

            return (
                dash.no_update,
                state,
                f"Score: {state['score']}/{state['round']}",
                feedback,
                guess,
                True,  # submit disabled
                False  # next round enabled
            )

        if trigger == "next-round":
            state["round"] += 1
            description, answer = get_random_person()
            state["answer"] = answer
            return (
                html.Ul([html.Li(d) for d in description]),
                state,
                f"Score: {state['score']}/{state['round'] - 1}",
                "New round! Make your guess below 👇",
                None,
                False,  # submit enabled
                True  # next round disabled
            )

        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

    @callback(
        Output("correlation-heatmap", "figure"),
        Output("correlation-warning", "children"),
        Input("correlation-checklist", "value"),
        prevent_initial_call=True
    )
    def update_correlation_heatmap(selected_columns):
        df = pd.read_csv("data/Obesity_Dataset -Table 1.csv", header=1)

        if len(selected_columns) < 2:
            return {}, "Please select at least two variables to compute correlation."

        # Compute correlation matrix
        corr_matrix = df[selected_columns].corr()

        fig = px.imshow(
            corr_matrix,
            text_auto=True,
            title="Correlation Matrix of Selected Lifestyle Factors",
            color_continuous_scale="RdBu_r",
            zmin=-1,
            zmax=1,
            labels=dict(color="Correlation"),
        )

        fig.update_layout(margin={"t": 40, "l": 10, "r": 10, "b": 10})

        return fig, ""


