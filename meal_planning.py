import streamlit as st # type: ignore
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Load meals data
def load_meals():
    return pd.read_csv("nmeals.csv")

# Function to plot pie chart of nutrient distribution
def plot_nutrient_distribution(total_nutrients):
   labels = list(total_nutrients.keys())
   sizes = list(total_nutrients.values())

   fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, hole=.3)])
   fig.update_traces(textinfo='percent+label')

   st.plotly_chart(fig)  # Equal aspect ratio ensures that pie is drawn as a circle.
   
                   
# Main function for meal planning
def main():
    st.title("Meal Planning")
    st.write("Create your meal plan here.")

    meals_data = load_meals()

    # Define meal categories with unique sorted food items
    meal_categories = {
        "Breakfast": sorted(meals_data['Food'].unique()),
        "Lunch": sorted(meals_data['Food'].unique()),
        "Dinner": sorted(meals_data['Food'].unique()),
        "Snack": sorted(meals_data['Food'].unique())
    }

    selected_meals = {}
    total_nutrients = {
        "Calories": 0,
        "Protein": 0,
        "Sat.Fat": 0,
        "Fiber": 0,
        "Carbs": 0
    }

    for meal_type, options in meal_categories.items():
        st.subheader(meal_type)
        selected_meals[meal_type] = []
        
        selected_food = st.multiselect(
            f"Select {meal_type} items",
            options
        )

        for food in selected_food:
            selected_meals[meal_type].append(food)
            food_data = meals_data[meals_data["Food"] == food]
            total_nutrients["Calories"] += food_data["Calories"].values[0]
            total_nutrients["Protein"] += food_data["Protein"].values[0]
            total_nutrients["Sat.Fat"] += food_data["Sat.Fat"].values[0]
            total_nutrients["Fiber"] += food_data["Fiber"].values[0]
            total_nutrients["Carbs"] += food_data["Carbs"].values[0]
            st.write(f"- **{food}**: {food_data['Calories'].values[0]} Calories, {food_data['Protein'].values[0]}g Protein, {food_data['Sat.Fat'].values[0]}g Sat.Fat, {food_data['Fiber'].values[0]}g Fiber, {food_data['Carbs'].values[0]}g Carbs")

    if st.button("Generate Summary"):
        st.write("### Meal Summary")
        for meal_type in selected_meals:
            st.write(f"**{meal_type}:** {', '.join(selected_meals[meal_type])}")
        
        st.write("### Total Nutrients")
        st.write(f"Total Calories: {total_nutrients['Calories']}")
        st.write(f"Total Protein: {total_nutrients['Protein']}g")
        st.write(f"Total Saturated Fat: {total_nutrients['Sat.Fat']}g")
        st.write(f"Total Fiber: {total_nutrients['Fiber']}g")
        st.write(f"Total Carbs: {total_nutrients['Carbs']}g")

        # Plot and display pie chart
        st.write("### Nutrient Distribution")
        plot_nutrient_distribution(total_nutrients)

if __name__ == "__main__":
    main()
