import requests
import time
import json
from telegram import Bot

def get_proxies():
    # Fetch the proxy list from the provided URL
    response = requests.get("https://raw.githubusercontent.com/yebekhe/MTProtoCollector/main/proxy/mtproto.json")
    if response.status_code != 200:
        raise Exception(f"Failed to fetch proxy list: {response.text}")
    
    return response.json()["result"]

def format_proxy(proxy):
    query_params = {
        "server": proxy["ip"],
        "port": proxy["port"],
        "secret": proxy["token"],
        "name": proxy["username"]
    }
    link = f"https://t.me/{proxy['username']}/proxy?{urllib.parse.urlencode(query_params)}"
    return {"server": proxy["ip"], "port": proxy["port"], "link": link}

def send_message(bot, message):
    response = bot.send_message(chat_id="889383653", text=message)
    if response.ok:
        print("Message sent successfully")
    else:
        raise Exception(f"Failed to send message: {response.content}")

if __name__ == "__main__":
    config = json.load(open("config.json"))
    bot = Bot(token=config["telegramBotToken"])

    while True:
        try:
            proxies = get_proxies()
            formatted_proxies = [format_proxy(p) for p in proxies]
            
            messages = []
            for p in formatted_proxies:
                message = f"🔗 Server: {p['server']}\n🌐 Port: {p['port']}\n🔒 Link: {p['link']}"
                messages.append(message)

            send_message(bot, "\n".join(messages))
        except Exception as e:
            print(e)

        time.sleep(config["postIntervalMinutes"] * 60)
