import plotly.express as px
import pandas as pd

def make_avg_calorie_bar():
    """
    this bar chart will show the avg calories per resteruant
    """
    df = pd.read_csv('data/fastfood.csv')
    avg_cal = df.groupby("restaurant")["calories"].mean().reset_index()

    fig = px.bar(
        avg_cal,
        x="restaurant",
        y="calories",
        title="Fast Food Isn't That Caloric - Avg Calories Per Item",
        text=avg_cal["calories"].round(0)
    )
    fig.update_traces(marker_color="#2ca02c")
    fig.update_layout(
        yaxis_title="Average Calories",
        xaxis_title="Restaurant",
        xaxis_tickangle = -45
    )
    return fig

def make_comparison_bar():
    comparison_df = pd.DataFrame({
        "Meal Type": [
            "Fast Food Item",
            "Homemade Pasta Meal",
            "Restaurant Dinner",
            "Holiday Plate"
        ],
        "Calories": [400, 650, 900, 1200]
    })

    fig = px.bar(
        comparison_df,
        x="Meal Type",
        y="Calories",
        title="Fast Food vs Other Meal Types",
        text="Calories"
    )
    fig.update_traces(marker_color="#1f77b4")
    fig.update_layout(
        yaxis_title="Average Calories Per Meal",
        xaxis_title="Meal Type",
    )
    return fig

def make_fastfood_vs_obesity_scatter():
    df = pd.read_csv('data/Obesity_Dataset -Table 1.csv', header=1)
    print(df["Consumption_of_Fast_Food"].value_counts())

    fig = px.scatter(
        df,
        x="Consumption_of_Fast_Food",
        y="Class",
        title="Is Fast Food Really Driving Obesity?",
        labels={
            "Consumption_of_Fast_Food": "Fast Food Frequency (1=Never, 5=Always)",
            "Class": "Obesity Classification",
        },
        trendline="ols"
    )
    fig.update_traces(marker=dict(color="#ff7f0e", size=6, opacity=0.6))
    fig.update_layout(
        xaxis_title="Fast Food Consumption Level",
        yaxis_title="Obesity Class",
    )
    return fig

def make_exercise_vs_obesity_line():
    df = pd.read_csv('data/Obesity_Dataset -Table 1.csv', header=1)
    df_grouped = df.groupby("Physical_Excercise")["Class"].mean().reset_index()

    fig = px.line(
        df_grouped,
        x="Physical_Excercise",
        y="Class",
        markers=True,
        title="Obesity Class Decreases With Physical Activity",
        labels={
            "Physical_Excercise": "Excersize Frequency (1 = Never, 5 = Regularly)",
            "Class": "Avg Obesity Class",
        }
    )
    fig.update_traces(marker_color="#9467bd")
    fig.update_layout(
        xaxis_title="Physical Exercise Level",
        yaxis_title="Obesity Class",
    )
    return fig

        # df = pd.read_csv('data/Obesity_Dataset -Table 1.csv', header=1)
        # class_counts = df["Class"].value_counts().sort_index().reset_index()
        # class_counts.columns = ["Class", "Count"]
        #
        # fig = px.line(
        #     class_counts,
        #     x="Class",
        #     y="Count",
        #     markers=True,
        #     title="Most People Aren't Even Obese",
        #     labels={
        #         "Class": "Obesity Class", "Count": "Number of Individuals"
        #     }
        # )
        # fig.update_traces(line_color="#9467bd")
        # fig.update_layout(
        #     xaxis_title="Obesity Class",
        #     yaxis_title="Number of People",
        #     xaxis=dict(tickmode='linear')
        # )
        # return fig
