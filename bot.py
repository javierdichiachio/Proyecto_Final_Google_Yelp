import telebot

bot = telebot.TeleBot("6530792617:AAHNzI79Jf4-i1P7BCz6YW_jFLQ4AXdRuBs")
@bot.message_handler(commands=["help","start"])

def enviar(message):
    bot.reply_to(message, "escribi bien puto")

@bot.message_handler(func=lambda message:True)

def mensaje(message):
    bot.reply_to(message, message.text)
    
bot.polling()