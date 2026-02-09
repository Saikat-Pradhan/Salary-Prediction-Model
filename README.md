# Salary Prediction Web App

A smart machine learning–based web application that predicts salary based on years of experience and age.
Built using Python, Scikit-learn, and Streamlit, and deployed for anyone to use online!

## 🔗 Live Demo

Try the deployed web app here: https://salary-prediction-model-by-saikat-pradhan.streamlit.app/

## 🚀 Project Overview

This project demonstrates how machine learning can estimate salaries using real data. A regression model 
predicts salary using user inputs, and the result is shown instantly in a clean web interface.

Input fields:
- Years of Experience
-  Age

Output:
- Predicted Salary

📂 Project Structure
├── app.py                    # Streamlit web app
├── model.pkl                 # Trained machine learning model
├── Package_Prediction.ipynb  # Notebook used to train the model
├── Salary_Data.csv           # Dataset
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

## 🧠 Technologies Used

- Python 🐍
- Streamlit 🌐
- Pandas 📊
- NumPy 📐
- Scikit-learn 🤖
- Pickle 📦

## ⚙️ Setup Guide (Run Locally)
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the App
streamlit run app.py


Then open:

http://localhost:8501

## 📊 Dataset

The dataset (Salary_Data.csv) includes:

- Years of Experience
- Age
- Salary

This data trains the model to understand salary patterns.

## 🏗️ Model Training

Model development happens in:

Package_Prediction.ipynb


It includes:

- Data preprocessing
- Feature handling
- Regression model training
- Model evaluation
- Saving the model with Pickle

## 🧠 How the App Works

- User enters experience and age
- Inputs go through the trained model
- Model predicts a salary value
- Prediction shows on the UI
