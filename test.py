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


def get_username(user_id):
    try:
        username = client.get_entity(user_id).username
    except:
        username = 'No'
    if not username:
        username = 'No'

    return username


def analise(mess, user_id):
    username = get_username(user_id)
    if not mess:
        return 'error: no message'
    mess = mess.lower()
    key_words = [['#ищумодель', 'модель', 'моделей', 'модели', 'роль', 'кастинг'],
                 ['парень', 'парней', 'парня', 'парни', 'мужчин', 'мужчина', 'мальчик', 'мальчика'],
                 ['коммерция', 'оплата', 'гонорар', 'бартер', 'мерч', 'бренд']]
    bad_words = ['#ищуфотографа', 'ищу фотографа', 'tfp', 'оплата студии', 'моделей нашли', 'тфп',
                 'модель на проф., макияж', 'мои фото']
    is_ok = 0
    for key_word in key_words:
        for kk in key_word:
            if kk in mess:
                is_ok += 1
                break
    for bad_word in bad_words:
        if bad_word in mess:
            is_ok -= 1
            break
    print(is_ok)
    print(username)


client.start()

# загружаем все внутренние диалоги
# что-то там с кешем. нужно вывести все чаты, чтобы они появились в кеше
for dialog in client.iter_dialogs():
    if dialog.is_channel:
        print(f'{dialog.id}:{dialog.title}')
print('---------------------------------------------------------------------------------------------------------')

client.start()


# -1001677493193:FULL TEAM | chat ОБЩЕНИЯ ОБСУЖДЕНИЕ
@client.on(events.NewMessage(chats=[1677493193]))
async def normal_handler(event):
    user_id = event.message.from_id.user_id
    print(user_id)
    user = await client.get_entity(user_id)
    username = user.username
    print(username)

    mess = event.message.to_dict()['message']
    print(mess)


# -1001152312586:Фотографы и видеографы  чат
@client.on(events.NewMessage(chats=[1152312586]))
async def normal_handler(event):
    user_id = event.message.from_id.user_id
    print(user_id)
    user = await client.get_entity(user_id)
    username = user.username
    print(username)

    mess = event.message.to_dict()['message']
    print(mess)


client.run_until_disconnected()
