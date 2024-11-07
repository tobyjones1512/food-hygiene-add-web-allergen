import streamlit as st
from pexpect import pxssh

st.title("Food Hygiene Community Additions")

st.header(st.query_params["business"])

if st.query_params["toAdd"] == "website":
    url = st.text_input(label="Website URL")

    if len(url) > 5:
        if st.button("Add Website"):
            st.info("DO NOT CLOSE THIS WINDOW.")
            s = pxssh.pxssh()
            if not s.login (st.secrets.DB_hostname, st.secrets.DB_username, st.secrets.DB_password):
                print ("SSH session failed on login.")
            else:
                print ("SSH session login successful")
                s.sendline ('cd "New Website (July 2024)/' + st.secrets.DB_remote_dir + '/websites"')
                s.prompt()
                if url.__contains('http'):
                    s.sendline ('echo "' + url + '" > "' + st.query_params["id"] + '.txt"')
                else:
                    s.sendline ('echo "https://' + url + '" > "' + st.query_params["id"] + '.txt"')
                s.prompt()
                s.logout()

                st.success("Successfully added the website to our database. Thank you!")

                st.write("You may close the window.")

                st.balloons()

elif st.query_params["toAdd"] == "allergenGuide":
    url = st.text_input(label="Guide URL")

    if len(url) > 5:
        if st.button("Add Allergen Guide"):
            st.info("DO NOT CLOSE THIS WINDOW.")
            s = pxssh.pxssh()
            if not s.login (st.secrets.DB_hostname, st.secrets.DB_username, st.secrets.DB_password):
                print ("SSH session failed on login.")
            else:
                print ("SSH session login successful")
                s.sendline ('cd "New Website (July 2024)/' + st.secrets.DB_remote_dir + '/allergen-guides"')
                s.prompt()
                if url.__contains('http'):
                    s.sendline ('echo "' + url + '" > "' + st.query_params["id"] + '.txt"')
                else:
                    s.sendline ('echo "https://' + url + '" > "' + st.query_params["id"] + '.txt"')
                s.prompt()
                s.logout()

                st.success("Successfully added the allergen guide to our database. Thank you!")

                st.write("You may close the window.")

                st.balloons()

elif st.query_params["toAdd"] == "waiverWarning":
    if st.button("Report Allergy Waiver Requirement"):
        st.info("DO NOT CLOSE THIS WINDOW.")
        s = pxssh.pxssh()
        if not s.login (st.secrets.DB_hostname, st.secrets.DB_username, st.secrets.DB_password):
            print ("SSH session failed on login.")
        else:
            print ("SSH session login successful")
            s.sendline ('cd "New Website (July 2024)/' + st.secrets.DB_remote_dir + '/waiver-warning"')
            s.prompt()
            s.sendline ('echo "" > "' + st.query_params["id"] + '.txt"')
            s.prompt()
            s.logout()

            st.success("Successfully added the warning to our database. Thank you!")

            st.write("You may close the window.")

            st.balloons()