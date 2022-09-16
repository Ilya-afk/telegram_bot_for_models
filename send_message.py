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


# функция отправки шаблонного сообщения пользователю
async def send_mess(user_id):
    # Getting information about yourself
    me = await client.get_me()

    await client.send_message(user_id, 'Доброго времени суток! \n Модель. Опыт съёмок есть')
    await client.send_message(user_id, os.getenv('CLOUD'))
    await client._send_album(user_id, ('P1.jpg', 'P2.jpg', 'P3.jpg', 'P4.jpg', 'P5.jpg'))


client.start()

# загружаем все внутренние диалоги
# что-то там с кешем. нужно вывести все чаты, чтобы они появились в кеше
for dialog in client.iter_dialogs():
    if dialog.is_channel:
        print(f'{dialog.id}:{dialog.title}')
print('---------------------------------------------------------------------------------------------------------')

client.get_dialogs()

# 0
user_id = 0

with client:
    client.loop.run_until_complete(send_mess(user_id))
