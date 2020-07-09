import telebot
from telebot import types
import logging
from telebot import apihelper






bot = telebot.TeleBot("963936543:AAEVPVExTceVIpPKrlM9QRvxhnfPeKOkX3s")


@bot.message_handler(commands=['start'])
def welcom(message):
    markup = types.ReplyKeyboardMarkup()
    but1 = types.KeyboardButton("Меню")
    but2 = types.KeyboardButton("Shop")
    but3 = types.KeyboardButton("GPS")
    but4 = types.KeyboardButton("welcom")
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)
    bot.send_message(message.chat.id, "Привет", reply_markup=markup)
    markup = types.ReplyKeyboardMarkup()
    markup.row('🎁Акция🎁', '🆔Профиль🆔')
    markup.row('🧩Команда🧩', '💲Easy💲', '💬Отзывы💬')
    bot.send_message(message.chat.id, "Для Покупок Введите Меню:", reply_markup=markup)



    print(message.chat)


@bot.message_handler(content_types=['text'])
def menu(message):
    if message.text == 'Меню':
        markup = types.ReplyKeyboardMarkup()
        button1 = types.KeyboardButton("Первая кнопка")
        button2 = types.KeyboardButton("Вторая кнопка")
        button3 = types.KeyboardButton("Третья кнопка")
        markup.add(button1, button2, button3, )
        bot.send_message(message.chat.id, "Вот кнопки:", reply_markup=markup)
    if message.text == "Первая кнопка":
        bot.send_message(message.chat.id, "Ты нажал на первую кнопку!")





bot.polling(none_stop=True)
