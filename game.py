import pandas as pd
import random

df = pd.read_csv('data/Obesity_Dataset -Table 1.csv', header=1)


features = [
    "Consumption_of_Fast_Food",
    "Physical_Excercise",
    "Calculation_of_Calorie_Intake",
    "Liquid_Intake_Daily",
    "Food_Intake_Between_Meals",
    "Class"
]

game_df = df[features].dropna().reset_index(drop=True)

def get_random_person():
    "return a randomm person from the dataset & the correct class"
    person = game_df.sample(1).iloc[0]

    lifestyle_description = [
        f"Fast food consumption level: {int(person['Consumption_of_Fast_Food'])}/3",
        f"Physical exercise: {'Yes' if person['Physical_Excercise'] == 1 else 'No'}",
        f"Calories per meal: {round(person['Calculation_of_Calorie_Intake'], 1)}"
        f"Water intake: {round(person['Liquid_Intake_Daily'], 1)} / liters/day",
        f"Snacking: {'Frequent' if person['Food_Intake_Between_Meals'] >= 2 else 'Occasional'}",
    ]

    return lifestyle_description, int(person["Class"])

def get_class_label(num):
    return {
        1: "Normal",
        2: "Overweight",
        3: "Obese",
        4: "Extremely Obese"
    }.get(num, "Unknown")