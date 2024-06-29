import streamlit as st
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

meals_df = pd.read_csv('nmeals.csv')

def main():
    def calculate_bmi(weight, height):
        height_m = height / 100  
        bmi = weight / (height_m ** 2)
        return bmi

    def get_recommendations(duration):
        bmi = calculate_bmi(weight, height)
        user_features = np.array([[bmi * 10, bmi * 1.5, bmi * 2.5, bmi * 0.4]])
        distances, indices = knn.kneighbors(user_features)

        if len(indices[0]) == 0:
            st.warning("No recommendations found. Please adjust your inputs.")
            return pd.DataFrame(columns=['Food', 'Calories', 'Protein', 'Carbs', 'Sat.Fat'])

        if duration == 'Weekly':
            num_recommendations = 5
        elif duration == 'Monthly':
            num_recommendations = 5
        
        # Ensure enough indices are available for recommendations
        if len(indices[0]) < num_recommendations:
            st.warning(f"Not enough recommendations available. Found {len(indices[0])}, but need {num_recommendations}.")
            return pd.DataFrame(columns=['Food', 'Calories', 'Protein', 'Carbs', 'Sat.Fat'])

        # Generate random indices for recommendations
        random_indices = np.random.choice(indices[0], size=num_recommendations, replace=False)
        
        recommended_meals = meals_df.iloc[random_indices][['Food', 'Calories', 'Protein', 'Carbs', 'Sat.Fat']]

        return recommended_meals
    


    st.title('Personalized Meal Recommendation')

    weight = st.number_input('Enter your weight (kg)', min_value=30, max_value=200, value=int(st.session_state['user_info']['weight']))
    height = st.number_input('Enter your height (cm)', min_value=100, max_value=2500, value=int(st.session_state['user_info']['height']))

    duration = st.radio('Select duration for recommendations:', ['Weekly', 'Monthly'])
    if st.button('Get Recommendations'):
        if duration == 'weekly':
            for i in range(5,10):

                features = meals_df[['Calories', 'Protein', 'Carbs', 'Sat.Fat']]
                knn = NearestNeighbors(n_neighbors=i, metric='euclidean')
                knn.fit(features)

                
                recommended_meals = get_recommendations(duration)
                    
                st.write(f'Your BMI: {calculate_bmi(weight, height):.2f}')
                st.write(f'Recommended {duration} Meals:')
                st.table(recommended_meals[['Food', 'Calories', 'Protein', 'Carbs', 'Sat.Fat']])
        else:
            for i in range(5,35):

                features = meals_df[['Calories', 'Protein', 'Carbs', 'Sat.Fat']]
                knn = NearestNeighbors(n_neighbors=i, metric='euclidean')
                knn.fit(features)

                recommended_meals = get_recommendations(duration)
                    
                st.write(f'Your BMI: {calculate_bmi(weight, height):.2f}')
                st.write(f'Recommended {duration} Meals:')
                st.table(recommended_meals[['Food', 'Calories', 'Protein', 'Carbs', 'Sat.Fat']])

        

if __name__ == "__main__":
    main()
