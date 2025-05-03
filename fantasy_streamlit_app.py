import streamlit as st
import pandas as pd
import joblib

# Load model and feature columns
model = joblib.load("fantasy_model.pkl")
model_columns = joblib.load("fantasy_columns.pkl")

st.title("🌟 IPL Fantasy Points Predictor")

# User input
batter = st.selectbox("Select Batter", [
    'Virat Kohli', 'Rohit Sharma', 'MS Dhoni', 'David Warner', 'Shubman Gill',
    'Jos Buttler', 'KL Rahul', 'Rinku Singh', 'Faf du Plessis', 'Suryakumar Yadav'
])

batting_team = st.selectbox("Batting Team", [
    'Chennai Super Kings', 'Mumbai Indians', 'Kolkata Knight Riders',
    'Royal Challengers Bangalore', 'Sunrisers Hyderabad', 'Delhi Capitals',
    'Punjab Kings', 'Rajasthan Royals', 'Gujarat Titans', 'Lucknow Super Giants'
])

bowling_team = st.selectbox("Bowling Team", [
    'Chennai Super Kings', 'Mumbai Indians', 'Kolkata Knight Riders',
    'Royal Challengers Bangalore', 'Sunrisers Hyderabad', 'Delhi Capitals',
    'Punjab Kings', 'Rajasthan Royals', 'Gujarat Titans', 'Lucknow Super Giants'
])

if st.button("Predict Fantasy Points"):
    input_dict = {
        'batter': [batter],
        'batting_team': [batting_team],
        'bowling_team': [bowling_team]
    }

    input_df = pd.DataFrame(input_dict)
    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(input_encoded)[0]
    st.success(f"🏆 Predicted Fantasy Points: {round(prediction)} points")
