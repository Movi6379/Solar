import streamlit as st
import pandas as pd
import plotly.express as px # This is the line that was crashing
import plotly.graph_objects as go

# Sample calculation for your 2MW plant Efficiency
def calculate_metrics(df):
    # Performance Ratio (Simplified)
    # PR = (Actual Yield / Reference Yield)
    pr_value = 75.2  # Example baseline
    return pr_value
