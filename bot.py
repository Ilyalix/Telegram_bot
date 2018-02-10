
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Filters, MessageHandler
import random
import requests

def start(bot,update):
	reply_keyboard = ['Man','Nigger','Person']
	print(update.message.from_user.username)
	bot.sendMessage(chat_id=update.message.chat_id, text="Hi! " + random.choice(reply_keyboard))

def weather(bot, update):
	print(update.message.from_user.username)
	bot.sendMessage(chat_id=update.message.chat_id, text="Hello")

def whome(bot, update):
	answer = "Привет, " + str(update.message.from_user.username)
	print(answer)
	bot.sendMessage(chat_id=update.message.chat_id, text=answer)

def echo(bot, update):
	if (update.message.text == u'Как дела?') :
		bot.send_message(chat_id=update.message.chat_id, text="Not Bad!!")
	else:
		city = str(update.message.text)
		r=requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c408f280234f6ef54fc71ba34eb5c77f")
		a=r.json()
		weathernow = round(a["main"]["temp"]-273.15,2)
		weathernow_2 = a["weather"][0]["main"]
		bot.send_message(chat_id=update.message.chat_id, text="Weather in " + city + " is : " + str(weathernow))
		bot.send_message(chat_id=update.message.chat_id, text=str(weathernow_2))


updater = Updater(token='460661808:AAHJCR4--QskAFiXmCjupgm06SxAnQo0AImk') # по какому токину надо проверять  

start_handler = CommandHandler('weather', weather)  # ловит команды
updater.dispatcher.add_handler(start_handler)

start_handler = CommandHandler('start', start)  # ловит команды
updater.dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo) # ловит сообщения 
updater.dispatcher.add_handler(echo_handler)

start_handler = CommandHandler('who', whome)  # ловит команды
updater.dispatcher.add_handler(start_handler)  
updater.start_polling() 
