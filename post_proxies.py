import json
import requests
from telegram import Bot
import schedule
import time

# توکن ربات و شناسه کانال را وارد کنید
TOKEN = '6717683305:AAGJoVLAXI8eh5QaHB4Ic2_cZvpMT4ynE3Y'
CHANNEL_ID = '@FreedomMtProtoProxy'
bot = Bot(token=TOKEN)

# آدرس فایل JSON را وارد کنید
JSON_URL = 'https://raw.githubusercontent.com/yebekhe/MTProtoCollector/main/proxy/mtproto.json'

def fetch_proxy_data():
    response = requests.get(JSON_URL)
    proxy_data = response.json()
    return proxy_data

def post_proxy_to_channel():
    proxy_data = fetch_proxy_data()
    message_text = f"Server: {proxy_data['query']['server']}\n" \
                   f"Port: {proxy_data['query']['port']}\n" \
                   f"Secret: {proxy_data['query']['secret']}\n" \
                   f"Link: {proxy_data['link']}"
    bot.send_message(chat_id=CHANNEL_ID, text=message_text)

schedule.every(1).minutes.do(post_proxy_to_channel)

while True:
    schedule.run_pending()
    time.sleep(1)
