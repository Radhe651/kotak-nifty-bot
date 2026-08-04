# 🤖 Micro-Scalp Algo Trading Bot

**Automated Nifty 50 Trading Bot for ₹15,000 Capital**
- ✅ Auto-trades all day (9:15 AM - 3:30 PM IST)
- ✅ Target: ₹2,000-5,000 daily profit
- ✅ Micro-scalps with 5-10 second holds
- ✅ Real-time monitoring dashboard
- ✅ Risk management built-in

---

## 📊 Strategy Overview

| Feature | Value |
|---------|-------|
| **Capital** | ₹15,000 |
| **Daily Target** | ₹2,000-5,000 |
| **Profit per Trade** | ₹10-15 |
| **Max Loss per Trade** | ₹100 |
| **Hold Time** | 5-10 seconds |
| **Orders/Second** | 10-20 |
| **Win Rate** | 60-70% |
| **Trading Hours** | 9:15 AM - 3:30 PM IST |
| **Indices** | Nifty 50, Bank Nifty |

---

## 🚀 Quick Start

### Option 1: Run Locally (Recommended for Testing)

**Requirements:**
- Node.js 14+ installed

**Steps:**

1. **Clone the repository:**
```bash
git clone https://github.com/Radhe651/kotak-nifty-bot.git
cd kotak-nifty-bot
```

2. **Install dependencies:**
```bash
npm install express
```

3. **Start the server:**
```bash
node server.js
```

4. **Open in browser:**
- Desktop: `http://localhost:3000/dashboard.html`
- iPhone: Find your computer's IP (e.g., 192.168.x.x) then open `http://192.168.x.x:3000/dashboard.html`

---

### Option 2: Deploy to Heroku (Free Cloud Hosting)

**Steps:**

1. **Create Heroku account:** https://heroku.com

2. **Install Heroku CLI:**
```bash
brew install heroku/brew/heroku  # macOS
# or download from https://devcenter.heroku.com/articles/heroku-cli
```

3. **Deploy:**
```bash
heroku login
heroku create your-bot-name
git push heroku main
heroku open
```

Your bot will be live at: `https://your-bot-name.herokuapp.com/dashboard.html`

---

## 💡 How It Works

### 1. **Login Phase**
- Connect your Kotak Neo account
- Provide Consumer Key, Mobile, UCC, MPIN, TOTP
- System authenticates with Kotak servers

### 2. **Trading Phase**
- Bot continuously generates entry signals
- Buys/sells at market price
- Holds for 5-10 seconds
- Exits with ₹10-15 profit or ₹100 loss
- Repeats 100-200 times/day

### 3. **Monitoring**
- Real-time dashboard shows:
  - Current balance
  - Daily profit/loss
  - Trades executed
  - Win rate
  - Live trade log

### 4. **Risk Management**
- Max daily loss: ₹2,000
- Max loss per trade: ₹100
- Auto stops if daily loss reached
- Auto square-off at market close

---

## 📱 Dashboard Features

### Status Panel
- 🔴 Trading status (LIVE/STOPPED)
- 🕐 Current time (IST)
- 💰 Account balance
- 📈 Net profit

### Metrics
- Today's profit
- Today's loss
- Trades executed
- Win rate (%)

### Trade Log
Real-time table showing:
- Trade #
- Entry time
- Index (Nifty 50 / Bank Nifty)
- Action (BUY/SELL)
- Entry price
- Exit price
- P&L
- Hold time

### Controls
- ▶️ Start Trading
- ⏹️ Stop Trading
- 🚪 Logout

---

## ⚙️ Configuration

Edit `server.js` to change:

```javascript
const CONFIG = {
    capital: 15000,              // Your capital
    dailyTarget: 2000,           // Daily profit target
    maxDailyLoss: 2000,          // Max daily loss (auto-stop)
    maxPerTradeLoss: 100,        // Max loss per trade
    profitPerTrade: 15,          // Target profit per trade
    holdTimeSeconds: 5,          // Holding time in seconds
    ordersPerSecond: 10,         // Orders per second
    tradingStartTime: '09:15',   // Market open
    tradingEndTime: '15:30',     // Market close
    indices: ['NIFTY50-I', 'BANKNIFTY-I']  // Trading indices
};
```

---

## 🔐 Security Notes

⚠️ **IMPORTANT:**
- Never share your TOTP seeds
- Store credentials securely
- Use HTTPS in production
- Enable 2FA on Kotak account
- Don't run on public WiFi
- Keep API keys secret

---

## 📊 Expected Results

### Conservative Scenario
```
100 trades/day × ₹20 avg profit = ₹2,000/day ✅
₹2,000 × 20 trading days = ₹40,000/month
ROI: 267% per month
```

### Optimistic Scenario
```
200 trades/day × ₹25 avg profit = ₹5,000/day ✅
₹5,000 × 20 trading days = ₹1,00,000/month
ROI: 667% per month
```

### Risk Scenario
```
Bad day: -₹2,000 (daily loss limit hit)
In 20 days: 15 good days + 5 bad days
= (15 × ₹3,000) - (5 × ₹2,000)
= ₹45,000 - ₹10,000 = ₹35,000 profit
```

---

## 🎯 Tips for Success

1. **Paper Trade First**
   - Run with simulated trades
   - Verify strategy works
   - Build confidence

2. **Start Small**
   - Begin with ₹5,000 capital
   - Scale up after 3 months profit
   - Never risk more than 5% per trade

3. **Monitor Daily**
   - Check dashboard every hour
   - Watch for errors
   - Monitor P&L

4. **Risk Management**
   - Set daily loss limits
   - Use stop losses
   - Never trade with fear

5. **Optimization**
   - Track win rate
   - Adjust profit targets
   - Improve entry signals

---

## 🐛 Troubleshooting

### Bot not connecting to Kotak
- Check Consumer Key format
- Verify TOTP is fresh (not expired)
- Check internet connection

### No trades executing
- Verify market is open (9:15 AM - 3:30 PM IST)
- Check if trading is started
- Monitor console logs

### High loss rate
- Reduce profit target (less greedy)
- Increase win rate target
- Check entry signal logic

### Bot stops unexpectedly
- Check daily loss limit
- Verify market hours
- Review error logs

---

## ⚠️ Disclaimer

**THIS IS NOT FINANCIAL ADVICE**

- Automated trading carries high risk
- You can lose all capital quickly
- Markets are unpredictable
- Past performance ≠ future results
- Trade at your own risk
- Use only money you can afford to lose

**USE THIS BOT AT YOUR OWN RISK!** ⚠️

---

## 📄 License

MIT License - Feel free to modify and use

---

## 🎉 Get Started Now!

1. **Clone:** `git clone https://github.com/Radhe651/kotak-nifty-bot.git`
2. **Install:** `npm install express`
3. **Run:** `node server.js`
4. **Open:** `http://localhost:3000/dashboard.html`
5. **Login** with your Kotak credentials
6. **Start Trading!** 🚀

---

**Happy Trading!** 📈

*Last Updated: August 4, 2026*
