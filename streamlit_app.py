import streamlit as st
from pexpect import pxssh

st.title("Food Hygiene Community Additions")

st.header(st.query_params["business"])

if st.query_params["toAdd"] == "website":
    url = st.text_input(label="Website URL")

    if len(url) > 5:
        if st.button("Add Website"):
            st.write("hi")