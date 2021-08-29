import telebot

import config

import utilities

guest_main_keyboard = telebot.types.ReplyKeyboardMarkup(True).row(config.get_premium_button_text)

admin_main_keyboard = telebot.types.ReplyKeyboardMarkup(True) \
    .row(telebot.types.KeyboardButton("Выдать премиум"),
        telebot.types.KeyboardButton("Забрать премиум")) \
            .row(telebot.types.KeyboardButton("Выдать администратора"),
                telebot.types.KeyboardButton("Снять администратора")) \
                    .row(telebot.types.KeyboardButton("Изменить цену"),
                        telebot.types.KeyboardButton("Изменить номер"),
                        telebot.types.KeyboardButton("Изменить токен")) \
                        .row(telebot.types.KeyboardButton("Изменить длительность"),
                            telebot.types.KeyboardButton("Показать конфиг"))

premium_main_keyboard = telebot.types.ReplyKeyboardMarkup(True) \
    .row(telebot.types.KeyboardButton("СМС")) \
        .row(telebot.types.KeyboardButton("Звонки"))

def payment_inline_keyboard(userid):
    keyboard = telebot.types.InlineKeyboardMarkup() \
        .add(telebot.types.InlineKeyboardButton(text='Оплатить', url = utilities.create_payment_link(userid, utilities.get_price()))) \
            .add(telebot.types.InlineKeyboardButton(text='Проверить оплату', callback_data = "checkpayment" ))
    return keyboard


def stop_inline_button():
    keyboard = telebot.types.InlineKeyboardMarkup() \
        .add(telebot.types.InlineKeyboardButton(text='СТОП', callback_data = "stop_attack"))

    return keyboard
