# достаю данные участников чата
import os

for partic in client.iter_participants(chat_name):
    lastname = ''
    if partic.username:  # у некоторых None
        lastname = partic.username
    users[chat_name][partic.id] = lastname


# --------------------------------------------------------------------------------------------------

# хранение username в словаре
chats_name = ['DreamTeam.Москва.Фотографы/модели/стилисты/визажисты/продюссеры',  # работает
              'Фотографы и видеографы',  # не работает
              'Чат|TFP |Фотографы|Визажисты|Модели',  # работает
              'Фотограф Москва']  # работает

users = {'DreamTeam.Москва.Фотографы/модели/стилисты/визажисты/продюссеры': {},
         'Фотографы и видеографы': {},
         'Чат|TFP |Фотографы|Визажисты|Модели': {},
         'Фотограф Москва': {}}

# в users хранится имя пользователя по ключу его id
for chat_name in chats_name:
    print(chat_name)
    print(users)
    participants = client.get_participants(chat_name)

    for partic in participants:
        users[chat_name][partic.id] = partic.username

print(users)

# ------------------------------------------------------------------------------------------------------------

# эвент получения нового сообщения
@client.on(events.NewMessage(chats=[1641848611]))
async def normal_handler(event):
    # print(event.message.to_dict()['from_id']['user_id'])
    print(event.message.to_dict()['message'])

# ------------------------------------------------------------------------------------------------------------

channelId = getChannelId(client, 'Модели Сьемки Москва')

# ------------------------------------------------------------------------------------------------------------

# запуск функции отправки сообщения
user_name = os.getenv('MYUSERNAME')
# with client:
#    client.loop.run_until_complete(send_mess(user_name))

# ------------------------------------------------------------------------------------------------------------

# username = await client.get_entity(user_id)['username']
# print(username)

# ------------------------------------------------------------------------------------------------------------

# -1001490523131:Модель на проект  чат
@client.on(events.NewMessage(chats=[1490523131]))
async def normal_handler(event):
    # print(event.message.to_dict()['from_id']['user_id'])
    mess = event.message.to_dict()['message']
    print(mess)

    try:
        username = client.get_entity(event.message.from_id.user_id).username
    except:
        username = 'No'
    if not username:
        username = 'No'
    print(username)

# ------------------------------------------------------------------------------------------------------------

# -1001590272186:Фотограф Москва  чат
@client.on(events.NewMessage(chats=[1590272186]))
async def normal_handler(event):
    user_id = event.message.from_id.user_id
    print(user_id)
    user = await client.get_entity(user_id)
    username = user.username
    print(username)

    mess = event.message.to_dict()['message']
    print(mess)

# ------------------------------------------------------------------------------------------------------------

async with client:
    await client.loop.run_until_complete(await send_mess_to_me(mess, user_id))
client.start()

# ------------------------------------------------------------------------------------------------------------

# -1001315422609:Ищу Модель. TFP (ТФП) Ищу Фотографа. Кастинг.  чат
@client.on(events.NewMessage(chats=[1315422609]))
async def normal_handler(event):
    user_id = event.message.from_id.user_id
    print(user_id)

    mess = event.message.to_dict()['message']
    print(mess)

    await analyze(mess, user_id=user_id)


# -1001152312586:Фотографы и видеографы  чат
@client.on(events.NewMessage(chats=[1152312586]))
async def normal_handler(event):
    user_id = event.message.from_id.user_id
    print(user_id)

    mess = event.message.to_dict()['message']
    print(mess)

    await analyze(mess, user_id=user_id)


# -1001490523131:Модель на проект  чат
@client.on(events.NewMessage(chats=[1490523131]))
async def normal_handler(event):
    user_id = event.message.from_id.user_id
    print(user_id)

    mess = event.message.to_dict()['message']
    print(mess)

    await analyze(mess, user_id=user_id)


# -1001577195928:DreamTeam.Москва.Фотографы/модели/стилисты/визажисты/продюссеры  чат
@client.on(events.NewMessage(chats=[1577195928]))
async def normal_handler(event):
    user_id = event.message.from_id.user_id
    print(user_id)

    mess = event.message.to_dict()['message']
    print(mess)

    await analyze(mess, user_id=user_id)


# -1001566780615:Чат|TFP |Фотографы|Визажисты|Модели  чат
@client.on(events.NewMessage(chats=[1566780615]))
async def normal_handler(event):
    user_id = event.message.from_id.user_id
    print(user_id)

    mess = event.message.to_dict()['message']
    print(mess)

    await analyze(mess, user_id=user_id)


# -1001358852681:Красивые люди  чат сообщения от имени группы
@client.on(events.NewMessage(chats=[1358852681]))
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


# -1001565344096:Ищу модель ! Москва  чат  сообщения от имени группы
@client.on(events.NewMessage(chats=[1565344096]))
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
