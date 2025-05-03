# import streamlit as st
# import pandas as pd
# import joblib

# # Load model and column list
# model = joblib.load("ipl_model.pkl")
# model_columns = joblib.load("model_columns.pkl")

# st.title("🏏 IPL Score Predictor (First 10 Overs)")

# # --- User Inputs ---
# batting_team = st.selectbox("Batting Team", [
#     'Chennai Super Kings', 'Mumbai Indians', 'Kolkata Knight Riders',
#     'Royal Challengers Bangalore', 'Sunrisers Hyderabad',
#     'Delhi Capitals', 'Punjab Kings', 'Rajasthan Royals',
#     'Gujarat Titans', 'Lucknow Super Giants'
# ])

# bowling_team = st.selectbox("Bowling Team", [
#     'Chennai Super Kings', 'Mumbai Indians', 'Kolkata Knight Riders',
#     'Royal Challengers Bangalore', 'Sunrisers Hyderabad',
#     'Delhi Capitals', 'Punjab Kings', 'Rajasthan Royals',
#     'Gujarat Titans', 'Lucknow Super Giants'
# ])

# runs = st.number_input("Runs Scored (first 10 overs)", min_value=0, max_value=120, step=1)
# wickets = st.number_input("Wickets Lost (first 10 overs)", min_value=0, max_value=10, step=1)
# balls = st.number_input("Balls Played (first 10 overs)", min_value=0, max_value=60, step=1)

# # Predict when button clicked
# if st.button("Predict Final Score"):
#     input_dict = {
#         'batting_team': [batting_team],
#         'bowling_team': [bowling_team],
#         'runs': [runs],
#         'wickets': [wickets],
#         'balls': [balls]
#     }

#     input_df = pd.DataFrame(input_dict)

#     # One-hot encode & align with training columns
#     input_encoded = pd.get_dummies(input_df)
#     input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

#     # Predict
#     prediction = model.predict(input_encoded)[0]
#     st.success(f"🏏 Predicted Final Score: {int(prediction)} runs")

# def predict_score_with_rules(runs, wickets, balls):
#     overs = balls / 6
#     current_run_rate = runs / overs if overs != 0 else 0
#     projected_score = current_run_rate * 20  # project to full 20 overs

#     # Subtract penalty for lost wickets
#     penalty = (wickets / 10) * 20  # max 20 run penalty if 10 wickets lost

#     final_score = projected_score - penalty
#     return round(final_score)
# if st.button("Predict Final Score"):
#     predicted_score = predict_score_with_rules(runs, wickets, balls)
#     st.success(f"🧮 Predicted Final Score: {predicted_score} runs")
