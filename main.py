import telebot
from telebot import types
import webbrowser

bot = telebot.TeleBot('7832470628:AAHjFbsurgc0l5mAEyrykYqx2VmNIWnxuYY')


@bot.message_handler(commands=['start'])
def start_chating(message):
    bot.send_message(message.chat.id, f'Hi, {message.from_user.last_name}')

@bot.message_handler(commands=['help'])
def ask_help(message):
    bot.send_message(message.chat.id, '<b>Help list:</b>\n/start', parse_mode='html')

@bot.message_handler(commands=['site'])
def get_site_url(message):
    bot.send_message(message.chat.id, "Откройте сайт: https://bleskdesign.ru", 
                     reply_markup=types.InlineKeyboardMarkup().add(
                        types.InlineKeyboardButton(text='Перейти на сайт', url='https://bleskdesign.ru')
                     ))

@bot.message_handler(commands=['buttons'])
def get_photo(message):
    markup = types.ReplyKeyboardMarkup()
    btn = {
        'btn1':types.KeyboardButton('Перейти на сайт'),
        'btn2':types.KeyboardButton('Удалить фото'),
        'btn3':types.KeyboardButton('Изменит текст'),
    }
    markup.row(btn['btn1'])
    markup.row(btn['btn2'],btn['btn3'])
    bot.send_message(message.chat.id, 'ОГОНЬ!!!', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
    

def on_click(message):
    if message.text.lower() == 'перейти на сайт':
        bot.send_message(message.chat.id, "Откройте сайт: https://bleskdesign.ru", 
                     reply_markup=types.InlineKeyboardMarkup().add(
                        types.InlineKeyboardButton(text='Перейти на сайт', url='https://bleskdesign.ru')
                     ))
    elif message.text.lower() == 'удалить фото':
        bot.send_message(message.chat.id, f'Hi, {message.from_user.last_name}')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn = {
        'btn1':types.InlineKeyboardButton(text='Перейти на сайт', url='https://bleskdesign.ru'),
        'btn2':types.InlineKeyboardButton(text='Удалить фото', callback_data='delete'),
        'btn3':types.InlineKeyboardButton(text='Изменит текст', callback_data='edit'),
    }
    markup.row(btn['btn1'])
    markup.row(btn['btn2'],btn['btn3'])
    bot.reply_to(message, 'ОГОНЬ!!!', reply_markup=markup)

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Hi, {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

@bot.callback_query_handler(func=lambda callback:True)
def callback_message(callback):
    if callback.data == 'delete':
       bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
       bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

bot.polling(non_stop=True)