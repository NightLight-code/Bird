import requests

import os
import sys


headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'Accept': 'application/json, text/plain, */*',
    'X-Requested-With': 'XMLHTTPRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://apteka-april.ru',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://apteka-april.ru/',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
}

data = '{"phone":' + sys.argv[1] +  ',"password":"wefew3fwergf21124eFERFWEF","pname":"WEFDFW11EFSFE","name":"WEFWEFSDF11WEF","sname":"DWEF112F","email":"DQW213RWGF@gmail.com"}'

response = requests.post('https://web-api.apteka-april.ru/users', headers=headers, data=data)

print(response.status_code, response.text, "aptekaapril")
