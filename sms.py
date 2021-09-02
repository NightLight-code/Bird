import requests

import utilities

import telebot

from threading import Thread

import time

import config

import os
import sys


def run_sms(phone, userid):

    os.system("python3 aptekaapril.py " + phone)

    os.system("python3 citymobil.py " + phone)

    os.system("python3 kari.py " + phone)

    os.system("python3 mvideo.py " + phone)

    os.system("python3 perekrestok.py " + phone)

    os.system("python3 sravni.py " + phone)

    os.system("python3 uber.py " + phone)

    if not utilities.is_attack_running(userid):
        bot = telebot.TeleBot(config.bot_token)
        bot.send_message(userid, "СМС остановлены!")
        return 0
