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


def analise(mess):
    if not mess:
        return 'error: no message'
    mess = mess.lower()
    key_words = [['#ищумодель', 'модель', 'моделей', 'модели', 'роль', 'кастинг'],
                 ['парень', 'парней', 'парня', 'парни', 'мужчин', 'мужчина'],
                 ['коммерция', 'оплата', 'гонорар', 'бартер']]
    bad_words = ['#ищуфотографа', 'ищу фотографа']
    is_ok = 0
    for key_word in key_words:
        for kk in key_word:
            print(kk)
            if kk in mess:
                is_ok += 1
                break
    for bad_word in bad_words:
        if bad_word in mess:
            print(bad_word)
            is_ok -= 1
            break
    print(is_ok)


a = '''моделей нашли. всем спасибо! 

москва 
🔸команда из фотографа, стилиста, визажиста и дизайнера украшений

 🔸#ищумодель тфп
ищем модель:
 ⁃ девушку
 ⁃ парня 
 ⁃ или пару

🔸 дата: 11 сентября 14:00
либо обговаривается 

🔸 🔹параметры девушки:
размер s
грудь 85-88
талия 63-66
бедра 87-90 
обувь 37-38 размера (24,3 - 24,8 см)

     🔹параметры парня: 
размер 44/182 
грудь 86-90
талия 74-78
бедра 92-96 
обувь 42 размера(26,5 - 27) 

будет городская фотосессия в свадебной стилистике 

🔸соц.сети: https://instagram.com/mua_victoriya?igshid=ymmymta2m2y=

связь в тг: @mua_victoriya'''


b = '''Москва

КОГО ИЩУ
#ретушера #ищуретушера 

УСЛОВИЯ
#коммерция

ЗАДАЧИ
Обработка фото для маркетплейсов 
Отбор/кадрирование/цвет/свет.

КОНТАКТ ДЛЯ СВЯЗИ: 
@imdiukina (в лс)

Условия: 10 руб. обработанный снимок (обработка без дублей, т.е. отобрать лучшие фото. Максимальное количество фото на 1 образ до 10, в идеале 6-8). 

Нужна максимальная скорость выполнения задачи. Скидываю материал сегодня, обработанные фото нужны уже завтра до обеда. 
У нас около 500 исходников от фотографа. 

У нас постоянный поток работы. 
Портфолио скидывайте в лс.'''

b = b.replace('\n', ' ')
b_list = b.split(' ')
for bebra in b_list:
    if '@' in bebra:
        print(bebra)
