# 🤖 Kotak Nifty Trading Bot - LOCAL SETUP GUIDE

## 📋 Prerequisites

Before you start, make sure you have:
- ✅ Windows PC or Mac with Python 3.8+
- ✅ Kotak Neo account with API enabled
- ✅ 6-digit TOTP authenticator (Google Authenticator/Authy)
- ✅ Your Kotak credentials ready:
  - Consumer Key
  - Mobile Number
  - UCC (Kotak account code)
  - MPIN (4-digit PIN)

---

## 🚀 STEP 1: Install Python & Requirements

### **Windows:**

1. Download Python from: https://www.python.org/downloads/
2. During installation, **CHECK** "Add Python to PATH"
3. Click Install

### **Mac:**

1. Python usually comes with Mac, but update it:
   ```bash
   brew install python3
   ```

---

## 📦 STEP 2: Clone the Repository

Open **Terminal** (Mac) or **Command Prompt** (Windows) and run:

```bash
git clone https://github.com/Radhe651/kotak-nifty-bot.git
cd kotak-nifty-bot
```

Or download the ZIP file from GitHub and extract it.

---

## 🔧 STEP 3: Install Dependencies

Run this command in Terminal/Command Prompt:

```bash
pip install -r requirements.txt
```

This will install:
- ✅ Streamlit (web framework)
- ✅ Pandas (data handling)
- ✅ Requests (API calls)
- ✅ Kotak Neo API library

---

## 🔑 STEP 4: Add Your Kotak Credentials

1. Open `local_bot.py` in a text editor (Notepad, VS Code, etc.)
2. Find this section (around line 10):

```python
# ============ CREDENTIALS - UPDATE THESE ============
CONSUMER_KEY = "your_consumer_key_here"
MOBILE_NUMBER = "+919876543210"
UCC = "ABC123"
MPIN = "1234"
# =================================================
```

3. Replace with YOUR actual Kotak details:
   - CONSUMER_KEY → Your API key from Kotak
   - MOBILE_NUMBER → Your registered mobile (with +91 country code)
   - UCC → Your Kotak UCC code
   - MPIN → Your 4-digit MPIN

4. **Save the file** (Ctrl+S)

---

## 🎯 STEP 5: Run the Bot

In Terminal/Command Prompt, run:

```bash
streamlit run local_bot.py
```

You should see:
```
Collecting usage statistics...
You can now view your Streamlit app in your browser.
URL: http://localhost:8501
```

The app will automatically open in your browser! 🎉

---

## 📱 STEP 6: Access from iPhone

### **Option A: Same WiFi (Easiest)**

1. **Find Your PC's IP Address:**
   
   **Windows:**
   - Open Command Prompt
   - Type: `ipconfig`
   - Look for "IPv4 Address" (e.g., 192.168.1.100)
   
   **Mac:**
   - Open Terminal
   - Type: `ifconfig`
   - Look for "inet" under your WiFi connection

2. **On Your iPhone:**
   - Open Safari
   - Go to: `http://192.168.1.100:8501` (replace IP with yours)
   - Bookmark it for easy access!
   - Tap Share → Add to Home Screen

### **Option B: Using Ngrok (Access from Anywhere)**

1. Download ngrok: https://ngrok.com/download
2. Unzip and open terminal in that folder
3. Run: `./ngrok http 8501`
4. Copy the URL shown (e.g., `https://abc123.ngrok.io`)
5. Share that URL with anyone to access your bot

---

## ⏰ STEP 7: Daily Trading Routine

**Every morning at 9:05 AM IST:**

1. Open Terminal/Command Prompt
2. Navigate to the bot folder
3. Run: `streamlit run local_bot.py`
4. Open iPhone Safari → Your bookmarked URL
5. Get 6-digit TOTP from Authenticator app
6. Paste TOTP and click "Login & Start Trading"
7. Set Stop Loss, Target, Quantity
8. Click BUY or SELL to place trades
9. Monitor P&L in real-time

---

## ⚠️ IMPORTANT NOTES

- ✅ **Bot runs on your PC** - PC must stay ON while trading
- ✅ **Internet required** - Must have stable connection
- ✅ **Real money trading** - All trades are LIVE
- ✅ **Start small** - Test with 1 lot first
- ✅ **Keep PC secure** - Don't share your PC

---

## 🐛 Troubleshooting

### **"Command not found: streamlit"**
Run: `pip install streamlit`

### **"ModuleNotFoundError: No module named 'neo_api_client'"**
Run: `pip install -r requirements.txt` again

### **"Connection refused"**
- Check PC and iPhone are on same WiFi
- Get correct IP with `ipconfig` or `ifconfig`
- Make sure Streamlit is running

### **"Authentication failed"**
- TOTP must be fresh (within 30 seconds)
- Check all credentials are correct
- Verify Kotak Neo API is enabled on your account

---

## 📞 Support

- **Kotak Neo API Docs:** https://github.com/Kotak-Neo/Kotak-neo-api-v2
- **Streamlit Docs:** https://docs.streamlit.io
- **GitHub Issues:** Post on your repo for help

---

## 🎯 Next Steps

1. ✅ Install Python and dependencies
2. ✅ Add your Kotak credentials
3. ✅ Run the bot: `streamlit run local_bot.py`
4. ✅ Access from iPhone
5. ✅ Start trading! 📈

**Good luck! 🚀**
