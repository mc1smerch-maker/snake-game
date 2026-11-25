import os
from threading import Thread
from flask import Flask
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# 1. Фоновый веб-сервер для хостинга Render, чтобы бот не отключался
app = Flask('')

@app.route('/')
def home():
    return "Бот и веб-сервер успешно запущены!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# Запускаем сервер в фоновом потоке
Thread(target=run_flask).start()


# 2. Основная логика Telegram-бота
API_TOKEN = '8131625654:AAFF3tHbu0GY8rYZNtEPKvCtf4U2vAedhGE' 
URL_ИГРЫ = 'https://github.io' 

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    web_app = WebAppInfo(URL_ИГРЫ)
    button = KeyboardButton(text="🟢 Играть в Змейку VI!", web_app=web_app)
    markup.add(button)
    
    bot.send_message(
        message.chat.id, 
        "Привет! Нажми на кнопку ниже, чтобы запустить мега-крутую змейку в стиле GTA VI! 🐍🌴🏎️", 
        reply_markup=markup
    )

print("Бот успешно запущен на хостинге!")
bot.infinity_polling()
