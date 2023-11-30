import telebot
from telebot import types

token = "6621864497:AAHQHmbHAfexHVDm4B0yx2k357mZyzg693M"
bot = telebot.TeleBot(token)

HELP = """
/info - вывести список доступных действий
/quizlet - запросить ссылку на викторину по теме 'Эпоха великих географических открытий'
/disvoverers - показть информацию про открывателей 1991-2022гг"""

@bot.message_handler(commands = ["info", "start"])
def info(message):
  bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands = ["discoverers"]) 
def discoverers_info(message):
  text="""
  Выберите открывателя, про которого хотите получить информацию и нажмите на цифру,под которой он указан:

  1.Афанасий Никитин 
  2.Фрэнсис Дрейк 
  3.Руаль Амундсен
  4.Америго Веспуччи
  5.Давид Ливингстон
  6.Фернан Магеллан
  7.Николай Миклухо-Маклай
  8.Васко да Гама
  9.Джеймс Кук
  10.Христофор Колумб
  """
  markup = types.InlineKeyboardMarkup()
  for i in range(1,11):
    button=types.InlineKeyboardButton(str(i), callback_data=str(i))
    if i%2!=0:
      markup.add(button)
    else:
      markup.row(button)
  bot.send_message(message.chat.id, text)


@bot.message_handler(commands = ["quizlet"]) 
def quiz(message):
  markup = types.InlineKeyboardMarkup()
  button = types.InlineKeyboardButton("Викторина", url="")
  markup.add(button)
  bot.send_message(message.chat.id, "Ссылка на сайт с викториной:")
  
bot.polling(none_stop=True)