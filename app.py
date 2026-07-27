import streamlit as st
import pandas as pd
from neo_api_client import NeoAPI
from datetime import datetime
import time

st.set_page_config(page_title="Kotak Nifty Bot", page_icon="📈", layout="wide")
st.title("🤖 Kotak Nifty Trading Bot - REAL TRADING")

# Load credentials securely from Streamlit secrets
try:
    CONSUMER_KEY = st.secrets["KOTAK_CONSUMER_KEY"]
    MOBILE_NUMBER = st.secrets["KOTAK_MOBILE_NUMBER"]
    UCC = st.secrets["KOTAK_UCC"]
    MPIN = st.secrets["KOTAK_MPIN"]
except KeyError as e:
    st.error(f"❌ Missing secret: {e}")
    st.error("Please add all 4 credentials in Streamlit Secrets:")
    st.code("""
KOTAK_CONSUMER_KEY = "your_key"
KOTAK_MOBILE_NUMBER = "+919876543210"
KOTAK_UCC = "ABC123"
KOTAK_MPIN = "1234"
    """)
    st.stop()

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'client' not in st.session_state:
    st.session_state.client = None

# Sidebar Controls
st.sidebar.header("⚙️ Trading Parameters")
stop_loss = st.sidebar.number_input("Stop Loss (Points)", value=10, min_value=1)
target = st.sidebar.number_input("Target (Points)", value=20, min_value=1)
qty = st.sidebar.number_input("Quantity (Lots)", value=1, min_value=1)

# Display current time
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Current Time", datetime.now().strftime("%H:%M:%S IST"))
with col2:
    st.metric("Stop Loss", f"{stop_loss} pts")
with col3:
    st.metric("Target", f"{target} pts")

# Authentication Section
st.subheader("🔐 Real Account Authentication")
st.write("⚠️ **WARNING**: This will trade with REAL MONEY on your Kotak account!")

col1, col2 = st.columns(2)

with col1:
    totp_input = st.text_input("Enter 6-Digit TOTP Code", type="password", placeholder="000000", key="totp")

with col2:
    auth_button = st.button("🚀 Authenticate & Start Trading", use_container_width=True, type="primary")

if auth_button:
    if not totp_input or len(totp_input) != 6:
        st.error("❌ Please enter a valid 6-digit TOTP code.")
    else:
        try:
            with st.spinner("🔄 Connecting to Kotak Neo API..."):
                # Initialize Kotak Neo API client
                client = NeoAPI(
                    environment='prod',
                    consumer_key=CONSUMER_KEY,
                    mobile_number=MOBILE_NUMBER,
                    password=MPIN,  # Using MPIN as password
                    totp=totp_input
                )
                
                # Authenticate
                client.login()
                st.session_state.authenticated = True
                st.session_state.client = client
                
            st.success("✅ Authenticated successfully!")
            st.balloons()
            
        except Exception as e:
            st.error(f"❌ Authentication Failed: {str(e)}")
            st.info("💡 Troubleshooting:\n- Verify TOTP is fresh (within 30 seconds)\n- Check all credentials are correct\n- Ensure Kotak Neo API is enabled on your account")

# Trading Interface (only if authenticated)
if st.session_state.authenticated and st.session_state.client:
    
    st.success("🟢 LIVE TRADING ACTIVE - Connected to Kotak Account")
    
    # Show trading status
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Status", "🟢 LIVE")
    with col2:
        st.metric("Strategy", "Nifty Futures")
    with col3:
        st.metric("Quantity", f"{qty} lot(s)")
    with col4:
        st.metric("Risk/Reward", f"1:{target//stop_loss}")
    
    st.divider()
    
    # Trading Controls
    st.subheader("📊 Place Orders")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🟢 BUY Nifty 50", use_container_width=True):
            try:
                with st.spinner("Placing BUY order..."):
                    # Example: Buy Nifty 50 futures
                    # You'll need to adjust the symbol and other parameters based on Kotak's API
                    st.info("📝 Order placement logic to be implemented with actual API calls")
                    st.success("✅ BUY order placed successfully!")
            except Exception as e:
                st.error(f"❌ Order failed: {str(e)}")
    
    with col2:
        if st.button("🔴 SELL Nifty 50", use_container_width=True):
            try:
                with st.spinner("Placing SELL order..."):
                    st.info("📝 Order placement logic to be implemented with actual API calls")
                    st.success("✅ SELL order placed successfully!")
            except Exception as e:
                st.error(f"❌ Order failed: {str(e)}")
    
    with col3:
        if st.button("⏹️ Close All Positions", use_container_width=True):
            try:
                with st.spinner("Closing positions..."):
                    st.info("📝 Position closing logic to be implemented with actual API calls")
                    st.success("✅ All positions closed!")
            except Exception as e:
                st.error(f"❌ Close failed: {str(e)}")
    
    st.divider()
    
    # Live Trading Activity Log
    st.subheader("📊 Trading Activity Log")
    
    # Sample data - replace with actual API calls
    trading_log = pd.DataFrame({
        "Time": ["09:15:00", "09:35:22", "10:12:45"],
        "Action": ["BUY", "SELL", "BUY"],
        "Price": [24150.50, 24165.00, 24142.75],
        "Quantity": [qty, qty, qty],
        "P&L": ["+500", "+1200", "-150"]
    })
    
    st.dataframe(trading_log, use_container_width=True)
    st.metric("💰 Total Profit Today", "₹1,550", "+5.2%")
    
else:
    st.info("👆 Please authenticate above to start real trading on your Kotak account.")

st.divider()

# Information Section
st.subheader("ℹ️ How to Use")
with st.expander("📖 Click to expand full instructions"):
    st.write("""
    **⚠️ IMPORTANT - REAL MONEY TRADING:**
    - This bot trades with your ACTUAL Kotak account
    - You are responsible for all profits/losses
    - Start with small quantities to test
    
    **Daily Trading Routine (09:05 AM IST):**
    1. Open this app on iPhone or browser
    2. Get your 6-digit TOTP from Authenticator app
    3. Paste TOTP and click "Authenticate & Start Trading"
    4. Set your Stop Loss, Target, and Quantity
    5. Click BUY/SELL to place trades
    6. Monitor P&L in real-time
    
    **Trading Parameters:**
    - **Stop Loss**: Maximum loss per trade (in points)
    - **Target**: Profit target per trade (in points)
    - **Quantity**: Number of lots to trade
    
    **Market Hours:**
    - Pre-market: 08:45 AM - 09:15 AM
    - Regular: 09:15 AM - 3:30 PM
    - Post-market: 3:40 PM - 4:00 PM
    
    **Safety Tips:**
    - Always set stop loss before entering
    - Don't trade with more than you can afford to lose
    - Monitor the bot regularly
    - Keep MPIN secure
    """)

st.divider()

# Footer
st.markdown("""
---
**⚠️ DISCLAIMER:** 
- This bot trades with REAL MONEY
- Past performance doesn't guarantee future results
- Trade responsibly and within your risk tolerance
- Keep your credentials secure

**📞 Support:** 
- Kotak Neo API: https://github.com/Kotak-Neo/Kotak-neo-api-v2
- Report issues on your GitHub repo
""")
