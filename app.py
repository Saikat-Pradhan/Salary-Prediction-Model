import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))

def predict_salary(years_experience, age):
    input_data = [[years_experience, age]]
    prediction = model.predict(input_data)
    return prediction[0]

st.title("Salary Prediction Model")
years_experience = st.number_input("Years of Experience", min_value=0.0, step=0.1)
age = st.number_input("Age", min_value=0, step=1)

if st.button("Predict Salary"):
    predicted_salary = predict_salary(years_experience, age)
    st.write(f"Predicted Salary: {predicted_salary:.2f}")