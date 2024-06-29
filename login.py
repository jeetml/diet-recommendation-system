import streamlit as st # type: ignore
from pymongo import MongoClient
import hashlib
import warnings
warnings.filterwarnings("ignore")


# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["auth-diet"]
users_collection = db["auth-diet"]

# Utility function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Utility function to verify passwords
def verify_password(stored_password, provided_password):
    return stored_password == hash_password(provided_password)

# Signup function with extended user information
def signup(username, password, role, age, weight, gender, height, dietary_preferences, allergies, health_goals):
    if users_collection.find_one({"username": username}):
        st.warning("Username already exists")
    else:
        user_data = {
            "username": username,
            "password": hash_password(password),
            "role": role,
            "age": age,
            "weight": weight,
            "gender": gender,
            "height": height,
            "dietary_preferences": dietary_preferences,
            "allergies": allergies,
            "health_goals": health_goals
        }
        users_collection.insert_one(user_data)
        st.success("User created successfully")

# Update user information function
def update_user_info(username, age, weight, gender, height, dietary_preferences, allergies, health_goals):
    query = {"username": username}
    new_values = {
        "$set": {
            "age": age,
            "weight": weight,
            "gender": gender,
            "height": height,
            "dietary_preferences": dietary_preferences,
            "allergies": allergies,
            "health_goals": health_goals
        }
    }
    users_collection.update_one(query, new_values)
    st.success("User information updated successfully")

# Login function
def login(username, password):
    user = users_collection.find_one({"username": username})
    if user and verify_password(user["password"], password):
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        st.session_state["role"] = user["role"]
        st.session_state["user_info"] = {
            "age": user.get("age", ""),
            "weight": user.get("weight", ""),
            "gender": user.get("gender", ""),
            "height": user.get("height", ""),
            "dietary_preferences": user.get("dietary_preferences", ""),
            "allergies": user.get("allergies", ""),
            "health_goals": user.get("health_goals", "")
        }
        st.experimental_set_query_params(page="welcome")
        st.experimental_rerun()
    else:
        st.error("Invalid username or password")

# Main application
def main():
    st.title("Diet Recommendation")

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    query_params = st.experimental_get_query_params()
    #query_params=st.query_params
    if st.session_state["logged_in"] and query_params.get("page") == ["welcome"]:
        if st.session_state["role"] == "user":
            welcome_user()
        else:
            admin_dashboard()
    elif st.session_state["logged_in"] and query_params.get("page") == ["meal_planning"]:
        import meal_planning
        meal_planning.main()
    elif st.session_state["logged_in"] and query_params.get("page") == ["suggestion"]:
        import suggestion
        suggestion.main()
    else:
        choice = st.selectbox("Login/Signup", ["Login", "Signup"])
        if choice == "Signup":
            st.subheader("Create a new account")
            new_username = st.text_input("Username")
            new_password = st.text_input("Password", type="password")
            new_role = st.selectbox("Role", ["user", "admin"])
            new_age = st.number_input("Age", min_value=0, max_value=150)
            new_weight = st.number_input("Weight (kg)", min_value=0.0)
            new_gender = st.radio("Gender", ["Male", "Female", "Other"])
            new_height = st.number_input("Height (cm)", min_value=0.0)
            new_dietary_preferences = st.text_input("Dietary Preferences")
            new_allergies = st.text_input("Allergies")
            new_health_goals = st.text_input("Health Goals")

            if st.button("Signup"):
                signup(new_username, new_password, new_role, new_age, new_weight,
                       new_gender, new_height, new_dietary_preferences, new_allergies, new_health_goals)

        elif choice == "Login":
            
            st.subheader("Login to your account")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                login(username, password)
    

# Welcome page for users
def welcome_user():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Welcome", "Meal Planning", "View My Info", "Update My Info", "Suggestion Meal Planning"])
    
    if page == "Welcome":
        st.title(f"Welcome, {st.session_state['username']}!")
        st.write("You are logged in as a user.")
    elif page == "Meal Planning":
        st.experimental_set_query_params(page="meal_planning")
        st.experimental_rerun()
    # elif page == "Suggestion Meal Planning":
    #     st.experimental_set_query_params(page="suggestion.py")
    #     st.experimental_rerun()
    elif page == "Suggestion Meal Planning":
        st.experimental_set_query_params(page="suggestion")
        st.experimental_rerun()
    elif page == "View My Info":
        show_user_info()
    elif page == "Update My Info":
        update_user_form()
    
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.experimental_rerun()

def show_user_info():
    st.header("Your Information:")
    st.write(f"- **Age:** {st.session_state['user_info']['age']}")
    st.write(f"- **Weight:** {st.session_state['user_info']['weight']} kg")
    st.write(f"- **Gender:** {st.session_state['user_info']['gender']}")
    st.write(f"- **Height:** {st.session_state['user_info']['height']} cm")
    st.write(f"- **Dietary Preferences:** {st.session_state['user_info']['dietary_preferences']}")
    st.write(f"- **Allergies:** {st.session_state['user_info']['allergies']}")
    st.write(f"- **Health Goals:** {st.session_state['user_info']['health_goals']}")
    if st.button("Back"):
        st.experimental_set_query_params(page="welcome")
        st.experimental_rerun()

def update_user_form():
    st.header("Update Your Information:")
    current_user_info = st.session_state["user_info"]
    updated_age = st.number_input("Age", value=current_user_info["age"], min_value=0, max_value=150)
    updated_weight = st.number_input("Weight (kg)", value=current_user_info["weight"], min_value=0.0)
    gender_options = ["Male", "Female", "Other"]
    updated_gender = st.radio("Gender", gender_options, index=gender_options.index(current_user_info["gender"]))
    updated_height = st.number_input("Height (cm)", value=current_user_info["height"], min_value=0.0)
    updated_dietary_preferences = st.text_input("Dietary Preferences", value=current_user_info["dietary_preferences"])
    updated_allergies = st.text_input("Allergies", value=current_user_info["allergies"])
    updated_health_goals = st.text_input("Health Goals", value=current_user_info["health_goals"])

    if st.button("Update"):
        update_user_info(st.session_state["username"], updated_age, updated_weight,
                         updated_gender, updated_height, updated_dietary_preferences,
                         updated_allergies, updated_health_goals)
        st.session_state["user_info"]["age"] = updated_age
        st.session_state["user_info"]["weight"] = updated_weight
        st.session_state["user_info"]["gender"] = updated_gender
        st.session_state["user_info"]["height"] = updated_height
        st.session_state["user_info"]["dietary_preferences"] = updated_dietary_preferences
        st.session_state["user_info"]["allergies"] = updated_allergies
        st.session_state["user_info"]["health_goals"] = updated_health_goals
        st.success("Information updated successfully!")
        st.experimental_set_query_params(page="welcome")
        st.experimental_rerun()
    if st.button("Cancel"):
        st.experimental_set_query_params(page="welcome")
        st.experimental_rerun()
def get_user_info(username):
    user = users_collection.find_one({"username": username})
    if user:
        return {
            "username": user["username"],
            "role": user["role"],
            "age": user.get("age", ""),
            "weight": user.get("weight", ""),
            "gender": user.get("gender", ""),
            "height": user.get("height", ""),
            "dietary_preferences": user.get("dietary_preferences", ""),
            "allergies": user.get("allergies", ""),
            "health_goals": user.get("health_goals", "")
        }
    else:
        return None
def remove_user(username):
    if users_collection.find_one({"username": username}):
        users_collection.delete_one({"username": username})
        st.success(f"User '{username}' removed successfully")
    else:
        st.warning("Username not found")

# Admin dashboard
def admin_dashboard():
    st.title(f"Welcome, {st.session_state['username']} (Admin)!")
    st.write("You have admin access.")
    
    st.header("Remove User")
    username_to_remove = st.text_input("Username to remove")
    if st.button("Remove User"):
        if username_to_remove:
            remove_user(username_to_remove)
        else:
            st.warning("Please enter a username")

    st.header("Retrieve User Information")
    username_to_retrieve = st.text_input("Username to retrieve information")
    if st.button("Retrieve User Info"):
        if username_to_retrieve:
            user_info = get_user_info(username_to_retrieve)
            if user_info:
                st.write("User Information:")
                st.write(f"- Username: {user_info['username']}")
                st.write(f"- Role: {user_info['role']}")
                st.write(f"- Age: {user_info['age']}")
                st.write(f"- Weight: {user_info['weight']} kg")
                st.write(f"- Gender: {user_info['gender']}")
                st.write(f"- Height: {user_info['height']} cm")
                st.write(f"- Dietary Preferences: {user_info['dietary_preferences']}")
                st.write(f"- Allergies: {user_info['allergies']}")
                st.write(f"- Health Goals: {user_info['health_goals']}")
            else:
                st.warning("Username not found")
        else:
            st.warning("Please enter a username")

    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.experimental_rerun()

if __name__ == "__main__":
    main()
