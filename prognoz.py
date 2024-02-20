"""
import telebot

API_TOKEN = "6728519495:AAGmbnPQq9Pipo-HIhWXmlru58AEmGomVpY"
if __name__ == "__main__":
    bot2 = telebot.TeleBot(API_TOKEN)
    """
#1) Мы перешли по ссылке прогноза погоды который вдает нам данные в API
#2) Перефрозировав ссылку (фото будет на телефоне) мы вставляем наш API_KEY сюда ,так же не забываем указывать токен
#3)указали все библиотеки с которыми будем работать(так же указали нашу папку откуда перем токен и API_KEY)
#6)чтобы чат бот выводил нам значки нужно скопировать ссылку сайта и написать https://openweathermap.org значки погоды
#7)далее мы казали с помощью telebot наш токин и создали хэндлер
#8)создали функцию и написали с помощью bot.send_message что нам выведет бот при старте
#9)по классике сделали bot.polling чтобы текст выводился повторно
#10) далее создали еще один хэндлер в котором уже делаем ,что наш бот будет нам отправлять(погоду)
#11)создали функцию и переменную которая ограничивает написание города message.text.strip().lower через верхний регистр
#13)с помощью json мы переводим наш запрос в красивый формат
#14)выводим данные которые нам будут нужны
#15)далее создаем список который будет хранить в себе перевод с сайта>>>>> с помощью if  проверяем его наличие ,а если не знает такую погоду то исключение
#16)далее запускаем вывод погоды с помощью bot.reply_to
#17) перешли к сайту значкам ,вставили ссылку и по вложению внесли нашу переменную которая будет определять какую именно картинку нам нужно будетт вносить
import bot1
import requests
import telebot
API_KEY = bot1.API_KEY #распаковали с папки
bot = telebot.TeleBot(bot1.token2)
@bot.message_handler(commands=["start"])
def funcshion(massage):
    bot.send_message(massage.chat.id, "Привет ватсок, напиши мне свой город)Я тебе разьясню по совести>>базарю")
@bot.message_handler(content_types=["text"])
def weather(message):
    city_name = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric')
    res_q = res.json()
    """bot.reply_to(message, f"Погода сейчас {res.json()}")"""
    temperature = res_q["main"]["temp"]
    feels_like = res_q["main"]["feels_like"]
    weather_diskripshen = res_q["weather"][0]["main"] #мы можем обратиться по индексу потому что находится в списке
    weather_icon = res_q["weather"][0]["icon"]


    """bot.reply_to(message, f"Погодка супер\t{round(temperature)})"""
    """bot.reply_to(message, f"Oщущается как\t{round(feels_like)})"""



    weathe_diskr = {"Clear": "Ясно","Snow": "снежно","Rain": "Дождик","Clouds": "Облачно","Drizzle": "туман","Thunderstorm":"гроза"}
    if weather_diskripshen in weathe_diskr:
        bd = weathe_diskr[weather_diskripshen]
    else:
        bd = "я незнаю такой погоды"
    bot.reply_to(message, f"Погодка супер\t{round(temperature)}, На улице:\n{bd}, Oщущается как\t{round(feels_like)}")
    bot.send_photo(message.chat.id, f"https://openweathermap.org/img/wn/{weather_icon}@2x.png")
if __name__ == "__main__":
    bot.polling(none_stop=True)
