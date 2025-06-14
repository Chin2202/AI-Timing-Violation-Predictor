import streamlit as st
import joblib
import numpy as np
from utils.optimization import suggest_optimal_frequency

st.set_page_config(page_title="AI-Based Timing Violation Predictor", page_icon="⚡")
st.title("⚡ AI-Based Timing Violation Predictor")

import os
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "models", "trained_model.pkl")
model = joblib.load(model_path)


st.sidebar.header("🔧 Input Parameters")

num_gates = st.sidebar.number_input("Number of Gates", min_value=100, max_value=50000, value=1000)
max_path_delay = st.sidebar.number_input("Maximum Path Delay (ns)", min_value=0.1, max_value=20.0, value=5.0)
slack = st.sidebar.number_input("Slack (ns)", min_value=-20.0, max_value=20.0, value=0.5)
frequency = st.sidebar.number_input("Operating Frequency (MHz)", min_value=1.0, max_value=2000.0, value=500.0)
fanout = st.sidebar.number_input("Fanout", min_value=1, max_value=20, value=3)

if st.sidebar.button("Predict Timing Violation"):
    input_features = np.array([[num_gates, max_path_delay, slack, frequency, fanout]])
    prediction = model.predict(input_features)[0]

    if prediction == 1:
        st.error("❌ Timing Violation Detected!")
        optimal_freq = suggest_optimal_frequency(max_path_delay, target_slack=0.5)
        st.info(f"🔧 Suggested Optimal Frequency: **{optimal_freq} MHz** to avoid violation.")
    else:
        st.success("✅ No Timing Violation Detected. Design is Safe!")

st.sidebar.markdown("---")
st.sidebar.write("Made with ❤️ by Chin")
