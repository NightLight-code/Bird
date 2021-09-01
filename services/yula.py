import requests

cookies = {
    'sessid': '3lki8b912k7udtuuo8tl1f8f1s',
    '_youla_uid': '612e884fa3420',
    'tmr_reqNum': '3',
    'tmr_lvid': 'c4382737a6ce7679113c835f78252368',
    'tmr_lvidTS': '1630439507092',
    '_ga': 'GA1.2.1718341564.1630439507',
    '_gid': 'GA1.2.441193419.1630439507',
    '_ym_uid': '1630439508736304789',
    '_ym_d': '1630439508',
    'cto_bundle': 'rIsVvV9Hck44VTlLYzNvVFBmUzNmOUVDSSUyQlk3T0VlOWNGOEJrQU5lUlZURFRiMW5kQnVMY0w5a2xCOCUyRlZwa3A4bUxBNmdVaWk2NXZhQ2hhYkdiak9vb0hhaXFRTjBJTjlXdHJYY0V5U3AlMkY2VjZ5Ums3dkRKbkUySmJZRm1BbnBxZHJHSA',
    'tmr_detect': '0%7C1630439509988',
    'mr1lad': '612fc06db2c3160-300-300-',
    '_ym_isad': '2',
    'redirect': 'https://youla.ru/',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://youla.ru/',
    'Content-Type': 'application/json; charset=utf-8',
    'X-Youla-Json': '{}',
    'Origin': 'https://youla.ru',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

data = '{"phone":"79222633421"}'

response = requests.post('https://youla.ru/web-api/auth/request_code', headers=headers, cookies=cookies, data=data)
