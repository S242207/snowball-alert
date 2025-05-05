import os
import requests
import yfinance as yf
import time

# Telegram config
TOKEN = os.environ['TOKEN']
CHAT_ID = os.environ['CHAT_ID']
API_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

# 股票與布林通道條件
STOCK = "2330.TW"
last_alert_time = 0

def send_alert(message):
    data = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(API_URL, data=data)

def check_condition():
    df = yf.download(STOCK, period="5d", interval="5m")
    if len(df) < 20:
        return False, "資料不足"

    close = df['Close']
    ma20 = close.rolling(window=20).mean()
    std = close.rolling(window=20).std()
    upper = ma20 + 2 * std
    lower = ma20 - 2 * std

    last_close = close.iloc[-1]
    last_upper = upper.iloc[-1]

    if last_close > last_upper:
        return True, f"⚠️ 雪球預警：{STOCK} 突破布林通道上軌，股價：{round(last_close, 2)}"
    return False, ""

while True:
    try:
        condition, msg = check_condition()
        if condition:
            global last_alert_time
            now = time.time()
            if now - last_alert_time > 300:
                send_alert(msg)
                last_alert_time = now
    except Exception as e:
        print("Error:", e)

    time.sleep(300)
