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

import random

def create_payment_link(userid, price):
	cookies = {
    '_ga_M9PW8YS3DF': 'GS1.1.1630405503.2.1.1630406870.0',
    '_ga': 'GA1.2.2054320385.1630267095',
    '_fbp': 'fb.1.1630267095104.791528437',
    'uxs_uid': '72ab65f0-0903-11ec-a2f6-7d49979ea0ed',
    'uxs_mig': '1',
    '_ga_cid': '2054320385.1630267095',
    '_ga_info': '4|59|1630406874066|r=https://www.google.com/|db3264cb7b67ae1716430cdf2acbd0e23fcd9f708f918f73340830f0a63e50f4',
    'auth_ukafokfuabbuzdckyiwlunsh': 'MDI3fF98X3xDblgFRwxLWFpnfVlsR1sRFwNLI3IwFxtoAAMLd1ZjWAhbeGdfR1IKCEdDZlByX0sTbQkIN1xfHWBxC3lkYn9RRT5MURENHUFHZXRbOV0MRhRWUiZmYkMFYFdSBX8Ebg==',
    '_gid': 'GA1.2.1829446771.1630403515',
    'token-tail': '02ba549445c5308b',
    '_ym_uid': '1630404539204393690',
    '_ym_d': '1630404539',
    '_ym_isad': '2',
    'token-tail-checkout-oauth': '2963df88225e00bc',
    'token-tail-web-qw': 'e3b8729d540e77fe',
    'spa_upstream': 'af0376ede1e7ba4eed661170519eedd4',
    '_ym_visorc': 'w',
    '_gat_qiwistream': '1',
}

	headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'application/json',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://qiwi.com/',
    'Content-Type': 'application/json',
    'Authorization': 'TokenHeadV2 Y2hlY2tvdXQtb2F1dGg6NDE3OTFmNjU3OWMxZDIyNQ',
    'Origin': 'https://qiwi.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'TE': 'trailers',
}

	data = '{"amount":' + str(price) + ',"extras":[{"code":"themeCode","value":"Polyna-ShCmHO5mLFz"},{"code":"apiClient","value":"p2p-admin"},{"code":"apiClientVersion","value":"0.17.0"}],"comment":"' + str(userid) + '","customers":[],"public_key":"48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iPrHfihmUVnxKqPWtUpRRFNQeNeyXemwu3J8hCqGq3tgcW2AbDT96VqLFYVfFDZA5N2SSx8vKPK2DVSW2p58kVqh5q1jSGuEBQCs9eZPU1D"}'

	response = requests.post('https://edge.qiwi.com/checkout-api/invoice/create', headers=headers, cookies=cookies, data=data)


	url = response.text.replace('{"invoice_uid":"', "").replace('"}', '')

	url = "https://oplata.qiwi.com/form?invoiceUid=" + url

	return url

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

def get_sms_timesleep():
	db_connect = sqlite3.connect(config.bd_name)
	cursor = db_connect.cursor()
	cursor.execute(f"SELECT * FROM Config")
	timesleep = cursor.fetchall()[0][5]
	db_connect.close()

	return str(timesleep)

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
			if payments_history['data'][i]['sum']['amount'] == get_price():
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


def auto_give_premium(userid):
	try:
		db_connect = sqlite3.connect(config.bd_name)
		cursor = db_connect.cursor()
		cursor.execute('Update Users set Status = "user" where id = ' + str(userid))
		db_connect.commit()
		db_connect.close()

	except:
		pass

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
