import telebot
import config
import random
import requests
from num2t4ru import num2text
from telebot import types
import datetime
import time
bot = telebot.TeleBot(config.TELEGRAM_TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Здравствуйте, чем могу вам помочь?')
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")
    item3 = types.KeyboardButton("🪙Орел/Решка")
    item4 = types.KeyboardButton("🎧Музыка")
    item5 = types.KeyboardButton("🏎️Форсаж")
    item6 = types.KeyboardButton("🌡️Погода")
    item7 = types.KeyboardButton("🃏Шутка")
    item8 = types.KeyboardButton("⁉️Правда/Действие")
    item9 = types.KeyboardButton("🪨✂️📜")
    item10= types.KeyboardButton("📰Новости")
    item11 = types.KeyboardButton("📲Приложение")
    
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный для поддержки связи и временного показа возможностей голосового помошника Markus".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == '😊 Как дела?':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        elif message.text == '🪙Орел/Решка':
            c_var = ['Орёл🦅','Решка🌾']
            bot.send_message(message.chat.id, random.choice(c_var))
        elif message.text == '🎧Музыка':
            bot.send_message(message.chat.id, 'https://music.yandex.ru/users/rayno125/playlists/1015')
        elif message.text == '🏎️Форсаж':
            bot.send_message(message.chat.id, 'https://music.yandex.ru/users/Djavidan17/playlists/1023')
        elif message.text == 'ты молодец' or message.text == 'Ты молодец':
            c_var = ['Рад стараться🤗','Стараюсь😎','Всегда к вашим услугам😉']
            bot.send_message(message.chat.id, random.choice(c_var))
        elif message.text == '🌡️Погода':

            params = {'q': 'BaKu', 'units': 'metric', 'lang': 'ru', 'appid': '8e999f79fd8c71617341303a20605026'}
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
            w = response.json()
            temperature = round(w['main']['temp'])
            bot.send_message(message.chat.id, f"На улице {w['weather'][0]['description']} {temperature} градусов")
        elif message.text == '📲Приложение':
            bot.send_message(message.chat.id, 'Приложение пока находится в разработке, но скоро вы сможете им воспользоваться')
        elif message.text == 'Привет' or message.text == 'привет':
            hour  = int(datetime.datetime.now().hour)
            if hour>=0 and hour<=12:
                bot.send_message(message.chat.id, "Доброе утро, {0.first_name}!".format(message.from_user, bot.get_me() ))
            elif hour >12 and hour<=18:
                bot.send_message(message.chat.id, "Добрый день, {0.first_name}!".format(message.from_user, bot.get_me()))
            else:
                bot.send_message(message.chat.id, "Добрый вечер, {0.first_name}!".format(message.from_user, bot.get_me()))
        elif message.text == '🃏Шутка':
            jokes = config.JOKES

            bot.send_message(message.chat.id, random.choice(jokes))
        elif message.text == '⁉️Правда/Действие':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Правда", callback_data='truth')
                item2 = types.InlineKeyboardButton("Действие", callback_data='dare')
                item3 = types.InlineKeyboardButton("Стоп", callback_data='stop')
                markup.add(item1, item2, item3)
                bot.send_message(message.chat.id, 'Правда или Действие?', reply_markup=markup)
        elif message.text == '🪨✂️📜':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Камень", callback_data='rock')
                item2 = types.InlineKeyboardButton("Ножницы", callback_data='scissors')
                item3 = types.InlineKeyboardButton("Бумага", callback_data='papper')
                markup.add(item1, item2, item3)
                bot.send_message(message.chat.id, 'Камень/Ножницы/Бумага?', reply_markup=markup)
        elif message.text == 'ты дурак' or message.text == 'Ты дурак':
            bot.send_message(message.chat.id, 'Давайте без оскорблений😒')
        elif message.text == '📰Новости':
            from pars import news
            news(message)
        elif 'статус' in message.text:
            bot.send_message(message.chat.id, 'Мы подключены и готовы👍')
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
        
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
            
            elif call.data == 'truth':
                with open('C:\\Users\\acer\\OneDrive\\Рабочий стол\\jarvis-master (3)\\truth or dare\\truth.txt', 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    bot.send_message(call.message.chat.id, random.choice(lines))
            elif call.data == 'dare':
                with open('C:\\Users\\acer\\OneDrive\\Рабочий стол\\jarvis-master (3)\\truth or dare\\dare.txt', 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    bot.send_message(call.message.chat.id, random.choice(lines))
            elif call.data == 'stop':
                bot.send_message(call.message.chat.id, 'Игра окончена!')    
            # remove inline buttons
            elif call.data == 'rock':
                comp_var = ['Камень','Ножницы','Бумага']
                comp_choise = random.choice(comp_var)
                bot.send_message(call.message.chat.id, comp_choise)
                if comp_choise == 'Камень':
                    bot.send_message(call.message.chat.id, 'Ничья')
                elif comp_choise == 'Ножницы':
                    bot.send_message(call.message.chat.id, 'Вы победили!')
                else:
                    bot.send_message(call.message.chat.id, 'Я победил!')
            elif call.data == 'scissors':
                comp_var = ['Камень','Ножницы','Бумага']
                comp_choise = random.choice(comp_var)
                bot.send_message(call.message.chat.id, comp_choise)
                if comp_choise == 'Камень':
                    bot.send_message(call.message.chat.id, 'Я победил!')
                elif comp_choise == 'Ножницы':
                    bot.send_message(call.message.chat.id, 'Ничья')
                else:
                    bot.send_message(call.message.chat.id, 'Вы победили!')
            elif call.data == 'papper':
                comp_var = ['Камень','Ножницы','Бумага']
                comp_choise = random.choice(comp_var)
                bot.send_message(call.message.chat.id, comp_choise)
                if comp_choise == 'Камень':
                    bot.send_message(call.message.chat.id, 'Вы победили!')
                elif comp_choise == 'Ножницы':
                    bot.send_message(call.message.chat.id, 'Я победил!')
                else:
                    bot.send_message(call.message.chat.id, 'Ничья')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Принято👍",
                 reply_markup=None)
            
            
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)