import streamlit as st
import pandas as pd
import plotly.express as px

# Dashboard Title
st.set_page_config(page_title="2MW Solar Dashboard", layout="wide")
st.title("☀️ 2MW Solar Plant: 7-Day Performance & Forecast")

# Load your 7-day data
df = pd.read_csv('data.csv')

# --- 1. Historical Analysis (7 Days) ---
st.header("Historical Analysis (Last 7 Days)")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Daily Energy Production")
    fig_prod = px.line(df, x='Timestamp', y='Power_kW', title="Power Output (kW)")
    st.plotly_chart(fig_prod)

with col2:
    st.subheader("Performance Ratio (PR)")
    # Sample logic for PR visualization
    st.metric(label="Current PR", value="78.5%", delta="+1.2%")

# --- 2. Predicted Data (Machine Learning) ---
st.header("⚡ Predicted Production (Next 24 Hours)")
# For now, you can mock this or link your ML model results
prediction_data = {"Time": ["08:00", "12:00", "16:00"], "Predicted_kW": [1200, 1950, 800]}
pred_df = pd.DataFrame(prediction_data)
st.bar_chart(pred_df.set_index("Time"))
