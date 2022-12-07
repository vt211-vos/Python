import telebot
from telebot import types
import random
from datetime import date
import time

TOKEN = "5949276147:AAEEhfpS-CMTbGWmO2XJCZDLjtQ46K1gzD4"
bot = telebot.TeleBot(TOKEN)
RAND = 0
USED = []
ANSWER = 0
START_TIME = 0
test = [
    {
        'question': 'Коли народився Шевченко Т.Г.?',
        'a': 1814,
        'b': 1818,
        'c': 1826,
        'd': 1817,
        'answer': 1814
    },
    {
        'question': 'Коли був виданий "Кобзар"?',
        'a': 1834,
        'b': 1840,
        'c': 1846,
        'd': 1847,
        'answer': 1840
    },
    {
        'question': 'Який був перший твір Шевченка?',
        'a': 'Тарасова ніч',
        'b': 'Причинна',
        'c': 'Катерина',
        'd': 'Перебендя',
        'answer': 'Причинна'
    }
]


@bot.message_handler(commands=['start'])
def start(message):
    global RAND
    global USED
    global ANSWER
    global START_TIME
    START_TIME = time.time()
    ANSWER = 0
    USED.clear()
    RAND = random.randint(0,2)
    USED.append(RAND)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(test[RAND]['a'], callback_data=test[RAND]['a'])
    btn2 = types.InlineKeyboardButton(test[RAND]['b'], callback_data=test[RAND]['b'])
    btn3 = types.InlineKeyboardButton(test[RAND]['c'], callback_data=test[RAND]['c'])
    btn4 = types.InlineKeyboardButton(test[RAND]['d'], callback_data=test[RAND]['d'])

    keyboard.add(btn1, btn2, btn3, btn4)
    bot.send_message(
        message.chat.id,
        test[RAND]['question'],

        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    global ANSWER
    global RAND
    global USED
    print(f'callback => {callback.data}')
    print(f'REND => {RAND}')
    if callback.data == str(test[RAND]['answer']):
        print('right')
        ANSWER += 1
        bot.edit_message_text(
            chat_id=callback.message.chat.id,
            message_id=callback.message.id,
            text='Шевченко пишається тобою',
            reply_markup=None
        )
    else:
        bot.edit_message_text(
            chat_id=callback.message.chat.id,
            message_id=callback.message.id,
            text='Шевченко обурений',
            reply_markup=None
        )
    while RAND in USED and len(USED) < 3:
        RAND = random.randint(0, 2)

    USED.append(RAND)
    if len(USED) < 4:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(test[RAND]['a'], callback_data=test[RAND]['a'])
        btn2 = types.InlineKeyboardButton(test[RAND]['b'], callback_data=test[RAND]['b'])
        btn3 = types.InlineKeyboardButton(test[RAND]['c'], callback_data=test[RAND]['c'])
        btn4 = types.InlineKeyboardButton(test[RAND]['d'], callback_data=test[RAND]['d'])
        keyboard.add(btn1, btn2, btn3, btn4)
        bot.send_message(
            callback.message.chat.id,
            test[RAND]['question'],
            reply_markup=keyboard
        )
    else:
        global START_TIME
        today = date.today()
        bot.send_message(
            callback.message.chat.id,
            f"Результат {ANSWER}/3\nДата проходження =>{today.strftime('%m/%d/%y')}\nЧас проходження =>{int(time.time()-START_TIME)}c"
        )

bot.polling(none_stop=True)

