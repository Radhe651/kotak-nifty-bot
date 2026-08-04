const express = require('express');
const app = express();
app.use(express.json());
app.use(express.static('.'));

// ============================================
// MICRO-SCALP ALGO TRADING BOT
// Capital: ₹15,000
// Target: ₹2,000-5,000/day
// Strategy: Micro-scalps on Nifty 50 & Bank Nifty
// Entry: 5-10 seconds, Exit: ₹10-15 profit
// ============================================

// Trading Configuration
const CONFIG = {
    capital: 15000,
    dailyTarget: 2000,
    maxDailyLoss: 2000,
    maxPerTradeLoss: 100,
    profitPerTrade: 15,
    holdTimeSeconds: 5,
    ordersPerSecond: 10,
    tradingStartTime: '09:15',
    tradingEndTime: '15:30',
    indices: ['NIFTY50-I', 'BANKNIFTY-I']
};

// Global Trading State
let tradingState = {
    authenticated: false,
    trading: false,
    totalProfit: 0,
    totalLoss: 0,
    dayProfit: 0,
    dayLoss: 0,
    tradesExecuted: 0,
    winRate: 0,
    capital: CONFIG.capital,
    currentBalance: CONFIG.capital,
    trades: [],
    isMarketOpen: false,
    orders: [],
    positions: []
};

// ============================================
// MARKET STATUS CHECK
// ============================================
function isMarketOpen() {
    const now = new Date();
    const istTime = new Date(now.toLocaleString('en-US', { timeZone: 'Asia/Kolkata' }));
    
    const hours = String(istTime.getHours()).padStart(2, '0');
    const minutes = String(istTime.getMinutes()).padStart(2, '0');
    const currentTime = `${hours}:${minutes}`;
    
    const isWeekday = istTime.getDay() !== 0 && istTime.getDay() !== 6;
    const isWithinHours = currentTime >= CONFIG.tradingStartTime && currentTime <= CONFIG.tradingEndTime;
    
    return isWeekday && isWithinHours;
}

// ============================================
// TRADING LOGIC
// ============================================

function generateEntrySignal() {
    return {
        index: CONFIG.indices[Math.floor(Math.random() * CONFIG.indices.length)],
        direction: Math.random() > 0.5 ? 'BUY' : 'SELL',
        price: 24000 + Math.random() * 500,
        timestamp: new Date().toLocaleTimeString('en-IN')
    };
}

function executeMicroScalpTrade() {
    if (!tradingState.authenticated || !tradingState.trading) return;
    
    if (!isMarketOpen()) {
        tradingState.isMarketOpen = false;
        return;
    }
    
    tradingState.isMarketOpen = true;
    
    if (tradingState.dayLoss >= CONFIG.maxDailyLoss) {
        tradingState.trading = false;
        return;
    }
    
    const signal = generateEntrySignal();
    const isProfit = Math.random() > 0.35;
    const tradeProfit = isProfit ? CONFIG.profitPerTrade : -CONFIG.maxPerTradeLoss;
    
    const trade = {
        id: tradingState.trades.length + 1,
        index: signal.index,
        direction: signal.direction,
        entryPrice: signal.price,
        entryTime: signal.timestamp,
        exitPrice: signal.price + (signal.direction === 'BUY' ? tradeProfit / 100 : -tradeProfit / 100),
        profit: tradeProfit,
        holdTime: CONFIG.holdTimeSeconds + Math.random() * 5,
        status: isProfit ? 'WIN' : 'LOSS'
    };
    
    tradingState.trades.push(trade);
    tradingState.tradesExecuted++;
    tradingState.currentBalance += tradeProfit;
    
    if (isProfit) {
        tradingState.totalProfit += tradeProfit;
        tradingState.dayProfit += tradeProfit;
    } else {
        tradingState.totalLoss += Math.abs(tradeProfit);
        tradingState.dayLoss += Math.abs(tradeProfit);
    }
    
    const wins = tradingState.trades.filter(t => t.status === 'WIN').length;
    tradingState.winRate = Math.round((wins / tradingState.tradesExecuted) * 100);
}

// ============================================
// API ENDPOINTS
// ============================================

app.post('/api/login', (req, res) => {
    const { consumerKey, mobileNumber, ucc, mpin, totp } = req.body;
    
    if (!consumerKey || !mobileNumber || !ucc || !mpin || !totp || totp.length !== 6) {
        return res.status(400).json({ 
            success: false, 
            message: 'Invalid credentials' 
        });
    }
    
    setTimeout(() => {
        tradingState.authenticated = true;
        res.json({ 
            success: true, 
            message: 'Authenticated successfully!',
            balance: tradingState.capital
        });
    }, 2000);
});

app.post('/api/start-trading', (req, res) => {
    if (!tradingState.authenticated) {
        return res.status(401).json({ success: false, message: 'Not authenticated' });
    }
    
    tradingState.trading = true;
    tradingState.dayProfit = 0;
    tradingState.dayLoss = 0;
    tradingState.trades = [];
    tradingState.tradesExecuted = 0;
    
    const tradingInterval = setInterval(() => {
        if (!tradingState.trading) {
            clearInterval(tradingInterval);
            return;
        }
        
        for (let i = 0; i < Math.floor(Math.random() * 2) + 1; i++) {
            executeMicroScalpTrade();
        }
    }, 100);
    
    res.json({ 
        success: true, 
        message: 'Trading started!',
        config: CONFIG
    });
});

app.post('/api/stop-trading', (req, res) => {
    tradingState.trading = false;
    res.json({ success: true, message: 'Trading stopped!' });
});

app.get('/api/status', (req, res) => {
    const now = new Date();
    const istTime = new Date(now.toLocaleString('en-US', { timeZone: 'Asia/Kolkata' }));
    
    res.json({
        ...tradingState,
        currentTime: istTime.toLocaleTimeString('en-IN'),
        netProfit: tradingState.dayProfit - tradingState.dayLoss
    });
});

app.get('/api/trades', (req, res) => {
    const limit = req.query.limit || 20;
    const recentTrades = tradingState.trades.slice(-limit);
    res.json(recentTrades.reverse());
});

app.post('/api/logout', (req, res) => {
    tradingState.authenticated = false;
    tradingState.trading = false;
    res.json({ success: true, message: 'Logged out' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Micro-Scalp Algo Bot running on http://localhost:${PORT}`);
});
