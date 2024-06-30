# Diet Recommendation System
## Introduction
The Diet Recommendation System is a web-based application developed using Streamlit. It provides personalized meal suggestions based on user information such as age, weight, gender, height, dietary preferences, allergies, and health goals. The application integrates with MongoDB for user authentication and data storage.

## Features
- **User Authentication**: Secure signup and login functionality with password hashing.
- **User Profile Management**: Users can view and update their personal information.
- **Meal Planning**: Users can plan their meals.
- **KNN Classifier for Meal Suggestions**: Personalized meal suggestions using K-Nearest Neighbors algorithm.
- **Admin Dashboard**: Admins can manage users, retrieve user information, and remove users.

## Usage
  1. **Signup/Login**: Users can create a new account or log in to an existing account.
  2. **Profile Management**: Users can view and update their personal information.
  3. **Meal Planning**: Users can access meal planning features.
  4. **Meal Suggestions**: Users receive meal suggestions based on their profile       information and the KNN classifier.

## Technologies Used
- **Streamlit**: Web application framework for building interactive and data-driven web apps.
- **MongoDB**: NoSQL database for storing user information.
- **pymongo**: Python driver for MongoDB.
- **hashlib**: Library for password hashing.
- **scikit-learn**: Machine learning library used for the KNN classifier.

## KNN Classifier for Meal Suggestions
The application includes a KNN (K-Nearest Neighbors) classifier to provide personalized meal suggestions based on user information. The classifier uses the following features to suggest meals:
- Age
- Weight
- Gender
- Height
- Dietary Preferences
- Allergies
- Health Goals

The KNN classifier compares the user's profile with the profiles of other users to find the closest matches and suggests meals that have been successful for similar users.

## Future Improvements
- **Enhanced Recommendation Algorithms**: Incorporate more advanced algorithms for better meal suggestions.
- **Nutritional Analysis**: Provide detailed nutritional information for suggested meals.
- **Integration with Fitness Trackers**: Sync with fitness trackers to get real-time health data.

## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push to the branch.
5. Create a pull request.
