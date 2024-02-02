import streamlit as st
from predict import predict_page
from data import explore_page

page = st.sidebar.selectbox("Predict or Explore", ("Predict", "Explore"))
if page == "Predict":
    predict_page()
else:
    explore_page()

