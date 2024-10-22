import streamlit as st

CAN_ACCESS = False

st.title("Rate My Selfies: Web App")

if not CAN_ACCESS:
    st.write(
        "Rate My Selfies uses Cryptocurrency (USDC) for transactions to reduce fees for both the developer and you, the user. Crypto also keeps payments secure, fast and private. If you do not have Cryptocurrency, we recommend [Coinbase Wallet](https://www.coinbase.com/en-gb/wallet). It is secure, utilising PayPal and card payments for transactions; has a strong support team; and is free and easy to use."
    )

    st.warning('YOU MUST BE 18 OR OVER TO USE THIS PLATFORM.')

    st.caption('Neither "Rate My Selfies" nor its developer is sponsored by Coinbase. You are free to make your own informed choices.')

    st.write(
        'By continuing, you are also agreeing to the [EULA, Terms of Use and Privacy Policy](https://ratemyselfies.xyz/wp-content/uploads/2024/10/Legal.pdf).'
    )

    with st.button('I AM 18 OR OVER'):
        CAN_ACCESS = True
else:
    st.heading("Dashboard")