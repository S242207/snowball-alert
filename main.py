
import requests
import time
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=data)

def check_market_condition():
    # 模擬邏輯：實際應該改為抓取 API 並分析
    return True, "⚠️ 雪球預警：符合條件「突破型態 放量」\n請立即檢查 2330.TW，5分鐘K線出現異常波動"

while True:
    alert, msg = check_market_condition()
    if alert:
        send_alert(msg)
    time.sleep(300)  # 每5分鐘檢查一次
