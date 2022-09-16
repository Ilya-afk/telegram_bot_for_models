from telethon import TelegramClient, sync, events
from dotenv import load_dotenv
import os


# load_dotenv() в данном случае и так работает, но это более общее решение
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# авторизация клиента (сначала нужно получить id и hash на сатйте my.telegram.org)
api_id = int(os.getenv('ID'))
api_hash = os.getenv('HASH')
client = TelegramClient('anon', api_id, api_hash)

client.start()

# 0
user_id = 0
client.send_message(user_id, 'тест бота')
