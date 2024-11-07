import streamlit as st
from pexpect import pxssh

st.title("Food Hygiene Community Additions")

st.header(st.query_params["business"])

if st.query_params["toAdd"] == "website":
    url = st.text_input(label="Website URL")

    if len(url) > 5:
        if st.button("Add Website"):
            s = pxssh.pxssh()
            if not s.login (st.secrets.DB_hostname, st.secrets.DB_username, st.secrets.DB_password):
                print ("SSH session failed on login.")
            else:
                print ("SSH session login successful")
                s.sendline ('cd "New Website (July 2024)/' + st.secrets.DB_remote_dir + '/websites"')
                s.prompt()
                s.sendline ('echo "' + url + '" > "' + st.query_params["id"] + '.txt"')
                s.prompt()
                s.logout()