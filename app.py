import streamlit as st
import random

class WorkoutRecommendationSystem:
    def __init__(self, user_profile):
        self.user_profile = user_profile

    def generate_workout_plan(self):
        workout_types = {
            "Cardio": ["Running", "Cycling", "Jump Rope"],
            "Strength Training": ["Push-ups", "Squats", "Dumbbell Rows"],
            "Flexibility": ["Yoga", "Pilates", "Stretching"],
        }
        workout_intensity = ["Low", "Moderate", "High"]

        recommended_workouts = {
            "Monday": {"Exercise": random.choice(workout_types["Cardio"]), "Intensity": random.choice(workout_intensity)},
            "Wednesday": {"Exercise": random.choice(workout_types["Strength Training"]), "Intensity": random.choice(workout_intensity)},
            "Friday": {"Exercise": random.choice(workout_types["Flexibility"]), "Intensity": random.choice(workout_intensity)},
        }

        return recommended_workouts

    def suggest_diet(self):
        if "Weight Loss" in self.user_profile["Goals"]:
            return "Focus on a balanced diet with a slight caloric deficit. Include more vegetables, lean proteins, and whole grains."
        elif "Muscle Gain" in self.user_profile["Goals"]:
            return "Consume a diet rich in protein to support muscle growth. Include sources like chicken, fish, eggs, and legumes."

def main():
    st.title("Personalized Workout Recommendation App")

    # Collect user input
    age = st.number_input("Enter your age", min_value=1, max_value=100, step=1)
    gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])
    fitness_level = st.selectbox("Select your fitness level", ["Beginner", "Intermediate", "Advanced"])
    goals = st.text_input("Enter your fitness goals, separated by commas (e.g., Weight Loss, Muscle Gain)")

    # Process user input
    user_profile = {
        "Age": age,
        "Gender": gender,
        "Fitness_Level": fitness_level,
        "Goals": goals.split(","),
    }

    recommendation_system = WorkoutRecommendationSystem(user_profile)
    workout_plan = recommendation_system.generate_workout_plan()
    diet_recommendation = recommendation_system.suggest_diet()

    # Display recommendations
    st.header("Your Personalized Workout Plan:")
    for day, details in workout_plan.items():
        st.write(f"{day}: {details['Intensity']} {details['Exercise']} workout")

    st.header("Diet Recommendation:")
    st.write(diet_recommendation)

if __name__ == "__main__":
    main()
