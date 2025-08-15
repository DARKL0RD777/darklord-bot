import telebot

TOKEN = "8323571210:AAH3Ga32QqGKjX64HOpo1YfNM9WHnFctWXg"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom DARKLORD! 👑 Bot ishga tushdi 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("Bot ishga tushdi... Kutyapman 📡")
bot.infinity_polling()

