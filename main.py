import telebot
from telebot.types import Message
import os
from flask import Flask , request

TOKEN = '5011437054:AAE_7lJZZsX2aTeLSQpTnb3tgY_FuXxSzbE'
APP_URL =f'https://toyotastockfiles.herokuapp.com/{TOKEN}'
bot  = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start','help'])
def start_message(message: Message):
    bot.send_message(chat_id=message.from_user.id,text='❗Для начала поиска напишите идентификационный номер файла, например 89663-22220 или 22220❗')
@bot.message_handler()
def echo(message: Message):
    bot.send_message(chat_id=message.from_user.id,text= message.text)
@server.route('/'+TOKEN, methods = ['POST'])
def get_message():
    json_stirng = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_stirng)
    bot.process_new_updates([update])
    return '!',200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)))

