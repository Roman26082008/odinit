#1. мы указали токен
#2.  импортировать библиотеку PY TELEGRAM BOT API
#3. В нашем втором файле импортируем библиотеку import telebot
#4. чтобы обратиться к нашему токену мы импортируем этот файл import bot1
#5. теперь обращаемся к нашему токену с помощью telebot.Telebot
#6 мы должны создать хэндлер для того ,чтобы бот мог обрабатывать апдейты (@bot.messeg_hendler())
#7 теперь в хэндлере указываем какие значения будет принимать бот @bot.message_handler(content_types=['text'])
#7.1 ЕСЛИ ЖЕ МЫ НИЧЕГО НЕ УКАЖЕМ, ТО БОТ БУДЕТ ПРИНИМАТЬ ЛЮБУЮ ИНФОРМАЦИЮ
#8. теперь мы создаем функцию и пишем в ней ,что бот будет принимать messeg-это аргумент
#9. Мы испольуем метод send_message для отправки от лица бота нашего аргумента
#10. мы обращаемся к id чата с помощью chat.id(он нужен для того,чтобы писать в личные сообщения)
#11. далее мы пишем bot.polling(non_stop=True) или bot.infinity_polling()- это нужно чтобы бот на следующие запросы нам также отвечал
token = "6662893713:AAEffeqrybgB-HZ5c6rlnOzA-PuR4H1sJfk"
toke2 = "6728519495:AAGmbnPQq9Pipo-HIhWXmlru58AEmGomVpY"
#////////////////////////////////////////////////////////
token2 = "6728519495:AAGmbnPQq9Pipo-HIhWXmlru58AEmGomVpY"
API_KEY = "25f5fc1d740a8e7f2f26d1b361ec51ca"
