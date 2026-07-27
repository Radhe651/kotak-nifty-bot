import streamlit as st
import pandas as pd
from neo_api_client import NeoAPI

st.set_page_config(page_title="Kotak Nifty Bot", page_icon="📈")
st.title("🤖 Kotak Nifty Trading Bot")

# Load credentials securely from Streamlit secrets
CONSUMER_KEY = st.secrets["KOTAK_CONSUMER_KEY"]
MOBILE_NUMBER = st.secrets["KOTAK_MOBILE_NUMBER"]
UCC = st.secrets["KOTAK_UCC"]
MPIN = st.secrets["KOTAK_MPIN"]

# Sidebar Controls
st.sidebar.header("Trading Parameters")
stop_loss = st.sidebar.number_input("Stop Loss (Points)", value=10)
target = st.sidebar.number_input("Target (Points)", value=20)
qty = st.sidebar.number_input("Quantity", value=50)

# Authentication Section
st.subheader("Daily Session Login")
totp_input = st.text_input("Enter 6-Digit TOTP from Authenticator", type="password")

if st.button("Authenticate & Launch Bot"):
    if totp_input:
        try:
            client = NeoAPI(environment='prod', consumer_key=CONSUMER_KEY)
            client.totp_login(mobile_number=MOBILE_NUMBER, ucc=UCC, totp=totp_input)
            client.totp_validate(mpin=MPIN)
            st.success("Authenticated successfully! Trading bot active.")
        except Exception as e:
            st.error(f"Authentication Error: {e}")
    else:
        st.warning("Please enter your 6-digit TOTP code.")
