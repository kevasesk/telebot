from telebot import TeleBot
import random

app = TeleBot(__name__)

@app.route('(?!/).+')
def parrot(message):
   chat_dest = message['chat']['id']
   user_msg = message['text']

   #msg = "Parrot Says: {}".format(user_msg)
   messages = [
       'м',
       'Владка классная',
       'Ну конечно',
       'Всё понятно',
       '😘',
       'Ой ну не ной',
       'Это да',
       'Умничка'
   ]
   app.send_message(chat_dest, random.choice(messages))

if __name__ == '__main__':
    app.config['api_key'] = '1336768592:AAEL3X6W-Eo5DaHtQ78U6YFokTBk3MZFQp0'
    app.poll(debug=True)