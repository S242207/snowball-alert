import requests
import time
import random
import os
# Telegram bot config
TOKEN = os.environ['TOKEN']
CHAT_ID = os.environ['CHAT_ID']
API_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

# 防止重複發送
last_alert_sent = False

def send_alert(message):
    data = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(API_URL, data=data)

def check_market_condition():
    # 模擬條件，之後你可以替換為實際邏輯
    condition = random.choice([True, False])
    message = "⚠️ 雪球預警：符合條件「突破型態 放量」\n請立即檢查 2330.TW，5分鐘 K 線出現異常波動"
    return condition, message

while True:
    try:
        alert, msg = check_market_condition()
        if alert:
            if not last_alert_sent:
                send_alert(msg)
                last_alert_sent = True
        else:
            last_alert_sent = False
        time.sleep(300)  # 每五分鐘檢查一次
    except Exception as e:
        print(f"錯誤：{e}")
        time.sleep(300)
    
