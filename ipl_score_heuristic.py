import streamlit as st

st.title("\U0001F3CF IPL Final Score Predictor (Rule-Based)")

# --- User Inputs ---
batting_team = st.selectbox("Batting Team", [
    'Chennai Super Kings', 'Mumbai Indians', 'Kolkata Knight Riders',
    'Royal Challengers Bangalore', 'Sunrisers Hyderabad',
    'Delhi Capitals', 'Punjab Kings', 'Rajasthan Royals',
    'Gujarat Titans', 'Lucknow Super Giants'
])

bowling_team = st.selectbox("Bowling Team", [
    'Chennai Super Kings', 'Mumbai Indians', 'Kolkata Knight Riders',
    'Royal Challengers Bangalore', 'Sunrisers Hyderabad',
    'Delhi Capitals', 'Punjab Kings', 'Rajasthan Royals',
    'Gujarat Titans', 'Lucknow Super Giants'
])

runs = st.number_input("Runs Scored (first 10 overs)", min_value=0, max_value=120, step=1)
wickets = st.number_input("Wickets Lost (first 10 overs)", min_value=0, max_value=10, step=1)
balls = st.number_input("Balls Played (first 10 overs)", min_value=1, max_value=60, step=1)

# --- Rule-Based Prediction Logic ---
def predict_score_with_rules(runs, wickets, balls):
    overs = balls / 6
    current_run_rate = runs / overs if overs != 0 else 0
    projected_score = current_run_rate * 20  # Project to full 20 overs

    # Subtract penalty based on wickets lost
    penalty = (wickets / 10) * 20
    final_score = projected_score - penalty
    return round(final_score)

# Predict when button clicked
if st.button("Predict Final Score"):
    predicted_score = predict_score_with_rules(runs, wickets, balls)
    st.success(f"\U0001F4CA Predicted Final Score: {predicted_score} runs")
# import pandas as pd
# import joblib
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.model_selection import train_test_split

# # Load delivery data
# df = pd.read_csv("deliveries.csv")

# # Group by match and batter to get total runs scored per match
# batter_stats = df.groupby(['match_id', 'batter', 'batting_team', 'bowling_team'])['batsman_runs'].sum().reset_index()
# batter_stats.rename(columns={'batsman_runs': 'runs_scored'}, inplace=True)

# # One-hot encode categorical columns
# features = ['batter', 'batting_team', 'bowling_team']
# X = pd.get_dummies(batter_stats[features])
# y = batter_stats['runs_scored']

# # Train/test split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train model
# model = RandomForestRegressor(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)

# # Save model and columns
# joblib.dump(model, "batter_model.pkl")
# joblib.dump(X.columns.tolist(), "batter_columns.pkl")

# print("✅ Model trained and saved: batter_model.pkl")
