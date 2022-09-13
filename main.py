import telebot

token='5799873487:AAGZ7LO0ZsZhxfs2OGwWXBl4vryec4NdEUk'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")

@bot.message_handler(content_types=['text'])
def new_message(message):
    if message.text == "Салам алейкум":
      bot.send_message(message.chat.id, "Алейкума салам")
    elif message.text == "Send pic":
      bot.send_photo(message.chat.id, photo= "https://ic.pics.livejournal.com/alternativamira/37073904/97886/97886_900.png")
    elif message.text == "Send emoji":
     bot.send_animation(message.chat.id, "CAACAgIAAxkBAAEFwQpjFH9BiXJGj0nsTKB6LuiO2alKsgACCAADwDZPE29sJgveGptpKQQ")  
    else:
      bot.send_message(message.chat.id, "Не знаю такой команды, пойди проспись")
bot.polling(none_stop = True)
