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
- MARKET Orders
- LIMIT Orders
- BUY and SELL support
- CLI input using argparse
- Input validation
- Logging support
- Error handling
- EMA 10 / EMA 20 strategy example
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

CLI Usage

Market Buy Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Market Sell Order

python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001

Limit Buy Order

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000

Limit Sell Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000

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
