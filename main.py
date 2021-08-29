import telebot

import config

import utilities

import keyboards

from threading import Thread

########################################
bot = telebot.TeleBot(config.bot_token)#
########################################

@bot.message_handler(commands=['start'])
def start_message(message):
	# New User check
	if utilities.is_user_in_table(message.from_user.id):
		pass
	else:
		utilities.save_user(message.from_user.id)
	#
	if not utilities.is_has_premium(message.from_user.id) and not utilities.is_admin(message.from_user.id):
		bot.send_message(message.from_user.id, config.guest_start_text, reply_markup = keyboards.guest_main_keyboard)



	elif utilities.is_admin(message.from_user.id):
		bot.send_message(message.from_user.id, "Рад приветствовать вас, Администратор!", reply_markup = keyboards.admin_main_keyboard)


	elif utilities.is_has_premium(message.from_user.id):
		bot.send_message(message.from_user.id, "Привествуем снова!", reply_markup = keyboards.premium_main_keyboard)




@bot.message_handler(content_types=['text'])
def main(message):
	if message.text == config.get_premium_button_text and not utilities.is_has_premium(message.from_user.id):
		bot.send_message(message.from_user.id, config.get_premium_text, reply_markup = keyboards.payment_inline_keyboard(message.from_user.id), parse_mode='html' )
	if message.text == "Звонки" and utilities.is_has_premium(message.from_user.id):
		bot.send_message(message.from_user.id, "Введите номер телефона: ")
		bot.register_next_step_handler(message, utilities.caller)
	elif message.text == "СМС" and utilities.is_has_premium(message.from_user.id):
		bot.send_message(message.from_user.id, "Введите номер телефона: ")
		bot.register_next_step_handler(message, utilities.smser)


	if utilities.is_admin(message.from_user.id):
		if message.text == "Выдать премиум":
			bot.send_message(message.from_user.id, "Введите user id пользователя: ")
			bot.register_next_step_handler(message, utilities.give_premium)
		elif message.text == "Забрать премиум":
			bot.send_message(message.from_user.id, "Введите user id пользователя: ")
			bot.register_next_step_handler(message, utilities.remove_premium)
		elif message.text == "Выдать администратора":
			bot.send_message(message.from_user.id, "Введите user id пользователя: ")
			bot.register_next_step_handler(message, utilities.give_admin)
		elif message.text == "Снять администратора":
			bot.send_message(message.from_user.id, "Введите user id пользователя: ")
			bot.register_next_step_handler(message, utilities.remove_admin)
		elif message.text == "Изменить цену":
			bot.send_message(message.from_user.id, "Введите цену в рублях (только число): ")
			bot.register_next_step_handler(message, utilities.change_price)
		elif message.text == "Изменить номер":
			bot.send_message(message.from_user.id, "WARNING!!!\nВведите номер: ")
			bot.register_next_step_handler(message, utilities.change_wallet_number)
		elif message.text == "Изменить токен":
			bot.send_message(message.from_user.id, "WARNING!!!\nВведите токен: ")
			bot.register_next_step_handler(message, utilities.change_wallet_token)
		elif message.text == "Изменить длительность":
			bot.send_message(message.from_user.id, "Введите длительность СМС (число в секундах): ")
			bot.register_next_step_handler(message, utilities.change_autostop_time)
		elif message.text == "Показать конфиг":
			bot.send_message(message.from_user.id, "Database name: " + config.bd_name + '\nPrice: ' + str(utilities.get_price()) + " RUB" + "\nWallet Number: " + utilities.get_wallet_number() + '\nWallet Token: ' + utilities.get_wallet_token() + '\nMax SMS time: ' + str(utilities.get_autostop_time()) + " Seconds" )

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
	if call.data == "checkpayment":
		if utilities.check_payment(call.from_user.id):
			bot.send_message(call.from_user.id, "Ваш платеж одобрен!")
		else:
			bot.send_message(call.from_user.id, "Ваш платеж не найден!")
	elif call.data == "stop_attack":
		utilities.make_user_unactive_attack(call.from_user.id)







bot.polling()
