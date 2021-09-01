import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'application/json;charset=utf-8',
    'Origin': 'https://city-mobil.ru',
    'Connection': 'keep-alive',
    'Referer': 'https://city-mobil.ru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'TE': 'trailers',
}

data = '{"phone":"79222633421","landing":"main"}'

response = requests.post('https://hemingoway.city-mobil.ru/api/v1/send_link', headers=headers, data=data)
