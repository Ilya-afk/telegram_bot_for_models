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


async def send_mess_to_me(mess, user_id):
    # Getting information about yourself
    me = await client.get_me()

    await client.send_message(os.getenv('MYUSERNAME'), mess)
    await client.send_message(os.getenv('MYUSERNAME'), str(user_id))


def getChannelId(client: TelegramClient, channelName):
    channel = findChannelEntity(client, channelName)
    # messages = client.iter_messages(channel)

    # for message in messages:
        # print(message)

    return channel.id


def findChannelEntity(client: TelegramClient, channelTitle):
    channelID = findChannelID(client, channelTitle)
    channelEntity = client.get_entity(channelID)

    return channelEntity


def findChannelID(client: TelegramClient, channelTitle):
    for dialog in client.iter_dialogs():
        if not dialog.is_group and dialog.is_channel:
            if channelTitle == dialog.title:
                return dialog.id


async def analyze(mess, user_id=0, username='No'):
    if not mess:
        return 'error: no message'
    mess = mess.lower()
    key_words = [['#ищумодель', 'модель', 'моделей', 'модели', 'роль', 'кастинг'],
                 ['парень', 'парней', 'парня', 'парни', 'мужчин', 'мужчина', 'мальчик', 'мальчика', 'юноша'],
                 ['коммерция', 'оплата', 'гонорар', 'бартер', 'мерч', 'бренд']]
    bad_words = ['#ищуфотографа', 'ищу фотографа', 'tfp', 'оплата студии', 'моделей нашли', 'тфп',
                 'модель на проф., макияж', 'мои фото', ' #модель']
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
    if username == 'No' and user_id == 0 and is_ok > 1:
        await send_mess_to_me(mess, user_id)
    elif username == 'No' and user_id == 0:
        return 'bad'

    if user_id == 0 and username != 'No':
        user_id = username

    if is_ok == 3:
        await send_mess(user_id)
    elif is_ok == 2:
        await send_mess_to_me(mess, user_id)
    else:
        return 'bad'


client.start()

# загружаем все внутренние диалоги
# что-то там с кешем. нужно вывести все чаты, чтобы они появились в кеше
for dialog in client.iter_dialogs():
    if dialog.is_channel:
        print(f'{dialog.id}:{dialog.title}')
print('---------------------------------------------------------------------------------------------------------')

client.get_dialogs()

# -1001590272186:Фотограф Москва  чат
# -1001315422609:Ищу Модель. TFP (ТФП) Ищу Фотографа. Кастинг.  чат
# -1001152312586:Фотографы и видеографы  чат
# -1001577195928:DreamTeam.Москва.Фотографы/модели/стилисты/визажисты/продюссеры  чат
# -1001490523131:Модель на проект  чат
# -1001566780615:Чат|TFP |Фотографы|Визажисты|Модели  чат
# -1001641848611:Модели Сьемки Москва  канал
# -1001358852681:Красивые люди  чат сообщения от имени группы
# -1001565344096:Ищу модель ! Москва  чат  сообщения от имени группы


# -1001590272186:Фотограф Москва  чат
@client.on(events.NewMessage(chats=[1590272186, 1315422609, 1152312586, 1490523131, 1577195928, 1566780615]))
async def normal_handler(event):
    user_id = event.message.from_id.user_id
    print(user_id)

    mess = event.message.to_dict()['message']
    print(mess)

    await analyze(mess, user_id=user_id)


# -1001641848611:Модели Сьемки Москва  канал
@client.on(events.NewMessage(chats=[1641848611, 1358852681, 1565344096]))
async def normal_handler(event):
    mess = event.message.to_dict()['message']
    print(mess)

    # mess = mess.replase('\n', ' ')

    # replace не работал - я написал свой
    norm_mess = []
    for i in range(len(mess)):
        if mess[i] == '\n':
            norm_mess.append(' ')
            continue
        norm_mess.append(mess[i])
    norm_mess = ''.join(norm_mess)

    mess_list = norm_mess.split(' ')
    username = 'No'
    for m in mess_list:
        if '@' in m:
            username = m[1:]
    print(username)

    await analyze(mess, username=username)


client.run_until_disconnected()

# не отправлять сообщение несколько раз одному и тому же (создавать список user_id и user_name
# доделать анализ сообщения, добавить еще 100500 слов
# сделать машинное обучение. супер лень самому собирать данные. а как иначе
# раскидать функции по файликам для удобства
# сделать более общие функции для более удобного расширения
