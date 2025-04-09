import telebot
import webbrowser

bot = telebot.TeleBot('7832470628:AAHjFbsurgc0l5mAEyrykYqx2VmNIWnxuYY')


@bot.message_handler(commands=['start'])
def start_chating(message):
    bot.send_message(message.chat.id, f'Hi, {message.from_user.last_name}')

@bot.message_handler(commands=['help'])
def ask_help(message):
    bot.send_message(message.chat.id, '<b>Help list:</b>\n/start', parse_mode='html')

@bot.message_handler(commands=['site'])
def start_chating(message):
    bot.send_message(message.chat.id, "Откройте сайт: https://bleskdesign.ru", 
                     reply_markup=telebot.types.InlineKeyboardMarkup().add(
                         telebot.types.InlineKeyboardButton(text='Перейти на сайт', url='https://bleskdesign.ru')
                     ))

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Hi, {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

bot.polling(non_stop=True)