import streamlit as st
import pickle

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

# Title
st.title("📊 Marks Prediction App")

st.write("Enter details to predict student marks")

# Input fields
number_courses = st.number_input("Number of Courses", min_value=1, max_value=10, step=1)
time_study = st.number_input("Study Time (hours)", min_value=0.0, max_value=24.0, step=0.1)

# Predict button
if st.button("Predict Marks"):
    result = model.predict([[number_courses, time_study]])
    st.success(f"Predicted Marks: {result[0]:.2f}")