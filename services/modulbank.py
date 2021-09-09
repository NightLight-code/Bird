import requests
import proxy
import sys

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'application/json',
    'PLATFORM': 'web',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://my.modulbank.ru',
    'Connection': 'keep-alive',
    'Referer': 'https://my.modulbank.ru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

data = '{"CellPhone":"' + sys.argv[1][1:] + '"}'
#9 first
response = requests.post('https://my.modulbank.ru/api/v2/auth/phone', headers=headers, data=data, proxies = proxy.getproxy())

print(response.status_code, response.text)
