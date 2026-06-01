from binance.client import Client
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

client = Client(api_key, api_secret)

klines = client.futures_klines(symbol="BTCUSDT", interval="1m", limit=50)

data = pd.DataFrame(klines)

data[4] = data[4].astype(float)

data["EMA_10"] = data[4].ewm(span=10).mean()
data["EMA_20"] = data[4].ewm(span=20).mean()

last_ema10 = data["EMA_10"].iloc[-1]
last_ema20 = data["EMA_20"].iloc[-1]

print("EMA 10:", last_ema10)
print("EMA 20:", last_ema20)

from bot.client import client
from binance.enums import *

symbol = "BTCUSDT"
quantity = 0.001

if last_ema10 > last_ema20:
    print("BUY SIGNAL 🚀")

    order = client.futures_create_order(
        symbol=symbol,
        side=SIDE_BUY,
        type=FUTURE_ORDER_TYPE_MARKET,
        quantity=quantity
    )

    print("BUY ORDER PLACED ✅")

elif last_ema10 < last_ema20:
    print("SELL SIGNAL 🔻")

    order = client.futures_create_order(
        symbol=symbol,
        side=SIDE_SELL,
        type=FUTURE_ORDER_TYPE_MARKET,
        quantity=quantity
    )

    print("SELL ORDER PLACED ✅")

else:
    print("NO SIGNAL")