Binance Futures Testnet Trading Bot

Overview

This project is a Python-based Binance Futures Testnet Trading Bot.

The bot:

- Connects to Binance Futures Testnet
- Fetches live BTCUSDT market data
- Calculates EMA indicators
- Generates BUY/SELL signals
- Places automatic MARKET orders

---

Features

- Binance Futures Testnet API integration
- Live market data fetching
- EMA 10 / EMA 20 strategy
- Automatic BUY and SELL orders
- Logging support
- Environment variable security (.env)

---

Technologies Used

- Python
- python-binance
- pandas
- dotenv

---

Project Structure

finance-futures-testnet-bot/

bot/

- client.py
- logging_config.py
- orders.py
- validators.py

logs/

cli.py
market_data.py
ema_strategy.py
README.md
requirements.txt
.env

---

Installation

Install required packages:

pip install -r requirements.txt

---

Configure API Keys

Create a .env file:

BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key

---

Run Trading Bot

Run EMA strategy bot:

python ema_strategy.py

---

Strategy Logic

- If EMA 10 > EMA 20:
  BUY SIGNAL

- If EMA 10 < EMA 20:
  SELL SIGNAL

---

Notes

- This project uses Binance Futures Testnet only.
- No real funds are used.