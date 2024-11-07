import streamlit as st

st.title("Food Hygiene Community Additions")

st.header(st.query_params["business"])

if st.query_params["toAdd"] == "website":
    url = st.text_input(label="Website URL")