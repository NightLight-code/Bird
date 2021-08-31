import sqlite3

import telebot

import requests

import json

import time

import config

from caller import main as run_call

from sms import run_sms as run_sms

from threading import Thread

import keyboards

def create_payment_link(userid, price):
	response = requests.get(f'https://oplata.qiwi.com/create?publicKey=48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iPrHfihmUVnxKqPWtUpRRFNQeNeyXemwu3J8hCqGq3tgcW2AbDT96VqLFYVfFDZA5N2SSx8vKPK2DVSW2p58kVqh5q1jSGuEBQCs9eZPU1D&amount=100&comment=123')
	print(response.text)
	return response.text

def create_users_table():
	db_connect = sqlite3.connect(config.bd_name)
	cursor = db_connect.cursor()
	cursor.execute("CREATE TABLE Users(Id INT, Status TEXT, Running INT)")
	db_connect.commit()
	db_connect.close()

def create_config_table():
	db_connect = sqlite3.connect(config.bd_name)
	cursor = db_connect.cursor()
	cursor.execute("CREATE TABLE Config(Id INT, Price TEXT, Wallet_Number TEXT, Wallet_Token TEXT)")
	db_connect.commit()
	db_connect.close()

def default_config():
	db_connect = sqlite3.connect(config.bd_name)
	cursor = db_connect.cursor()
	cursor.execute(f"INSERT INTO Config VALUES({int(1)}, '500', '+79222633421', '2c2ff8420fab5705e594deb8a3e1c7ebs')")
	db_connect.commit()
	db_connect.close()

def get_price():
	db_connect = sqlite3.connect(config.bd_name)
	cursor = db_connect.cursor()
	cursor.execute(f"SELECT * FROM Config")
	price = cursor.fetchall()[0][1]
	db_connect.close()

	return int(price)

def get_wallet_number():
	db_connect = sqlite3.connect(config.bd_name)
	cursor = db_connect.cursor()
	cursor.execute(f"SELECT * FROM Config")
	wallet_number = cursor.fetchall()[0][2]
	db_connect.close()

	return str(wallet_number)

def get_autostop_time():
	db_connect = sqlite3.connect(config.bd_name)
	cursor = db_connect.cursor()
	cursor.execute(f"SELECT * FROM Config")
	autostop_time = cursor.fetchall()[0][4]
	db_connect.close()

	return str(autostop_time)

def change_price(message):
	try:
		price = int(message.text)
		db_connect = sqlite3.connect(config.bd_name)
		cursor = db_connect.cursor()
		cursor.execute(f'Update Config set Price = "{str(price)}" where id = 1')
		db_connect.commit()
		db_connect.close()

		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Цена изменена!")
	except:
		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Цена не изменена!")

def change_wallet_number(message):
	try:
		number = message.text
		number = number.split("#*#*#")
		check = number[1]
		number = number[0]
		number = number.replace("+", "").replace("-", "").replace("(", "").replace(")", "")
		number = int(number)
		number = "+" + str(number)
		db_connect = sqlite3.connect(config.bd_name)
		cursor = db_connect.cursor()
		cursor.execute(f'Update Config set Wallet_Number = "{str(number)}" where id = 1')
		db_connect.commit()
		db_connect.close()

		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Номер изменен!")
	except:
		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Номер не изменен!")

def change_autostop_time(message):
	try:
		time = int(message.text)
		db_connect = sqlite3.connect(config.bd_name)
		cursor = db_connect.cursor()
		cursor.execute(f'Update Config set Stop_time = "{str(time)}" where id = 1')
		db_connect.commit()
		db_connect.close()

		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Длительность изменена!")
	except:
		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Длительность не изменена!")




def get_wallet_token():
	db_connect = sqlite3.connect(config.bd_name)
	cursor = db_connect.cursor()
	cursor.execute(f"SELECT * FROM Config")
	wallet_token = cursor.fetchall()[0][3]
	db_connect.close()

	return str(wallet_token).replace("\'", '')

def change_wallet_token(message):
	try:
		token = message.text
		token = token.split("#*#*#")
		check = token[1]
		token = token[0]
		db_connect = sqlite3.connect(config.bd_name)
		cursor = db_connect.cursor()
		cursor.execute(f'Update Config set Wallet_Token = "{str(token)}" where id = 1')
		db_connect.commit()
		db_connect.close()

		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Токен изменен!")
	except:
		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Токен не изменен!")

def save_user(userid):
	db_connect = sqlite3.connect(config.bd_name)
	cursor = db_connect.cursor()
	cursor.execute(f"INSERT INTO Users VALUES({int(userid)}, 'guest', '0')")
	db_connect.commit()
	db_connect.close()

def is_user_in_table(userid):
	db_connect = sqlite3.connect(config.bd_name)
	cursor = db_connect.cursor()
	cursor.execute(f"SELECT * FROM Users")
	users_list = cursor.fetchall()
	db_connect.close()

	if str(userid) in str(users_list):
		return True
	else:
		return False


def is_admin(userid):
	db_connect = sqlite3.connect(config.bd_name)
	cursor = db_connect.cursor()
	cursor.execute(f"SELECT * FROM Users")
	users_list = cursor.fetchall()
	db_connect.close()

	for user in users_list:
		if user[0] == userid and user[1] == "admin":
			return True
		else:
			return False

def is_has_premium(userid):
	db_connect = sqlite3.connect(config.bd_name)
	cursor = db_connect.cursor()
	cursor.execute(f"SELECT * FROM Users")
	users_list = cursor.fetchall()
	db_connect.close()

	for user in users_list:
		if user[0] == userid and user[1] == "user":
			return True
	return False

def is_attack_running(userid):
	db_connect = sqlite3.connect(config.bd_name)
	cursor = db_connect.cursor()
	cursor.execute(f"SELECT * FROM Users where id = " + str(userid))
	userinfo = cursor.fetchall()
	db_connect.close()
	attack_status = userinfo[0][2]

	if int(attack_status) == 1:
		return True
	else:
		return False


def check_payment(userid):
	URL = "https://edge.qiwi.com/payment-history/v2/persons/" + get_wallet_number() + "/payments"
	PARAMS = {'rows': 1, 'operation': 'IN'}
	HEADERS = {'Accept': 'application/json', 'Authorization': 'Bearer ' + get_wallet_token()}
	r = requests.get(url=URL, params=PARAMS, headers=HEADERS)
	payments_history = json.loads(r.text)

	for i in range(len(payments_history['data'])):
		if payments_history['data'][i]['comment'] == str(userid):
			if payments_history['data'][i]['sum']['amount'] == utilities.get_price():
				return True

	return False



def give_premium(message):
	try:
		userid = message.text
		db_connect = sqlite3.connect(config.bd_name)
		cursor = db_connect.cursor()
		cursor.execute('Update Users set Status = "user" where id = ' + str(userid))
		db_connect.commit()
		db_connect.close()

		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Премиум выдан!")
	except:
		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Премиум не выдан!")

def remove_premium(message):
	try:
		userid = message.text
		db_connect = sqlite3.connect(config.bd_name)
		cursor = db_connect.cursor()
		cursor.execute('Update Users set Status = "guest" where id = ' + str(userid))
		db_connect.commit()
		db_connect.close()

		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Премиум удален!")
	except:
		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Премиум не удален!")



def give_admin(message):
	try:
		userid = message.text
		db_connect = sqlite3.connect(config.bd_name)
		cursor = db_connect.cursor()
		cursor.execute('Update Users set Status = "admin" where id = ' + str(userid))
		db_connect.commit()
		db_connect.close()

		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Администратор добавлен!")
	except:
		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Администратор не добавлен!")

def remove_admin(message):
	try:
		userid = message.text
		db_connect = sqlite3.connect(config.bd_name)
		cursor = db_connect.cursor()
		cursor.execute('Update Users set Status = "guest" where id = ' + str(userid))
		db_connect.commit()
		db_connect.close()

		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Администратор удален!")
	except:
		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Администратор не удален!")

def caller(message):
	number = message.text.replace("+", '').replace('(', '').replace(')', '').replace('-', '')
	if len(number) == 11:
		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Звонки запущены!")
		Thread(target = run_call(number, message.chat.id)).start()

	else:
		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Номер введен не верно!")


def make_user_active_attack(userid):
	db_connect = sqlite3.connect(config.bd_name)
	cursor = db_connect.cursor()
	cursor.execute('Update Users set Running = "1" where id = ' + str(userid))
	db_connect.commit()
	db_connect.close()

def make_user_unactive_attack(userid):
	db_connect = sqlite3.connect(config.bd_name)
	cursor = db_connect.cursor()
	cursor.execute('Update Users set Running = "0" where id = ' + str(userid))
	db_connect.commit()
	db_connect.close()


def smser(message):
	userid = str(message.from_user.id)
	number = message.text.replace("+", '').replace('(', '').replace(')', '').replace('-', '')
	if len(number) == 11:
		bot = telebot.TeleBot(config.bot_token)
		make_user_active_attack(message.from_user.id)
		bot.send_message(message.chat.id, "СМС запущены!", reply_markup = keyboards.stop_inline_button())
		Thread(target = run_sms, args = (number, message.from_user.id)).start()
		Thread(target = autostop, args = (1, userid)).start()

	else:
		bot = telebot.TeleBot(config.bot_token)
		bot.send_message(message.chat.id, "Номер введен не верно!")



def autostop(num, userid):
	time.sleep(int(get_autostop_time()))
	make_user_unactive_attack(str(userid))
