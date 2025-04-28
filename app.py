import streamlit as st
import pandas as pd

st.title("My Streamlit App 🚀")
st.write("Welcome to your first deployed Streamlit app!")

# Example of loading data from the data folder
try:
    df = pd.read_csv("data/sample.csv")
    st.subheader("Sample Data")
    st.dataframe(df)
except FileNotFoundError:
    st.info("No sample data found. Add a CSV file to the data/ folder!")

# Example of using a helper from utils
try:
    from utils.helpers import shout
    st.write(shout("This text is from a helper function!"))
except Exception:
    st.info("No helpers found. (Create utils/helpers.py to add helpers.)")

# Example of using an image from assets
from PIL import Image
import os

logo_path = "assets/logo.png"
if os.path.exists(logo_path):
    st.image(Image.open(logo_path), caption="App Logo")
