import requests

cookies = {
    'dodo_utm': '',
    'rerf': 'AAAAAGEvyXSG3mnxA+jpAg==',
    'ipp_uid': '1630521716873/jA9XfNWTOZjZ3QTr/jfCb6jFRB3lwxx3yKZ8tww==',
    'ipp_uid1': '1630521716873',
    'ipp_uid2': 'jA9XfNWTOZjZ3QTr/jfCb6jFRB3lwxx3yKZ8tww==',
    'dodo_visit': '478ccab8-ffa3-469b-ab75-c9748bef0840',
    'dodo_visitor': 'a81348dc-dbfd-4537-9c46-d442f6c95c49',
    '_gcl_au': '1.1.1278644556.1630521719',
    'deduplication_cookie': 'undefined',
    'cityads_deduplication_cookie': 'undefined',
    'sessionID': '1630521719567.ykqoaf1jf',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    '_ga': 'GA1.2.1222628562.1630521721',
    '_gid': 'GA1.2.697934942.1630521721',
    '_ym_uid': '163052172286668073',
    '_ym_d': '1630521722',
    'locality': 'moscow',
    'WorkflowId': '48404950-01af-41d9-9c09-7576b6e333d0',
    '_gat_UA-100114221-5': '1',
    '_gat_UA-162076268-1': '1',
    'cto_bundle': 'CCwQUV8lMkZkNldBdERQWFM4SER5YiUyQjg4RUclMkJlMXJlNjdaJTJCOWFhMSUyQkhLZjFkZUs0UXNlYUdVNHBsQldrb05hc20lMkJCb054N0RJdW5sTHkxcjdPR1F6QyUyQiUyRmx4JTJCWG51Ykl5NU9EV0lyOFRrRFAwN2xnZGMzZ0NzS2tYQnJySWolMkJNWXdqSXRKTGJCYWFFeW9RRFpLaVVvNHlMbkRhZyUzRCUzRA',
    '_fbp': 'fb.1.1630521727176.960593051',
    '_ym_visorc': 'w',
    '_ym_isad': '2',
    'cp': '1630521732',
    'mindboxDeviceUUID': '12a7bb8d-048b-40a0-ad08-96e69c5dcbcb',
    'directCrm-session': '%7B%22deviceGuid%22%3A%2212a7bb8d-048b-40a0-ad08-96e69c5dcbcb%22%7D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://dodopizza.ru/moscow',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://dodopizza.ru',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

data = {
  'phoneNumber': '+79222633421'
}

response = requests.post('https://dodopizza.ru/api/sendconfirmationcode', headers=headers, cookies=cookies, data=data)
