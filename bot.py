import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# Сюда вставьте ваш токен, который вы брали в @BotFather
API_TOKEN = 'ВАШ_ТОКЕН_БОТА' 

# Ваша ссылка на игру в GitHub Pages
URL_ИГРЫ = 'https://github.io' 

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    web_app = WebAppInfo(URL_ИГРЫ)
    button = KeyboardButton(text="🟢 Играть в Змейку 2000!", web_app=web_app)
    markup.add(button)
    
    bot.send_message(
        message.chat.id, 
        "Привет! Нажми на кнопку ниже, чтобы запустить легендарную ретро-змейку! 🐍📱", 
        reply_markup=markup
    )

print("Бот успешно запущен на Render!")
bot.infinity_polling()
