import requests
import sys


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': 'Bearer 2QtLgA-eRoIqAje9hCOuykhsZCRgPlPcLKhTJ_CYALOlp21cm9wGX603d5_VpGy3-YJ6wszFwPpOP05WHUc8Iz-fgaEZFF1jUcIlC60wO-M0lsCagONGny_mhEPcuyjNDZqiq-ShHgarc-kpxbqT3yaBpT2HCbIcK7Pfk_UAFLIh0TvF4vlEGwx_XWg-d-uk9lPlBKgU7xkPB82UIuWmtOQPWUtKtOl8Sf9DFp4cWO-eMfc8GIZstKn1wy3xoY0ugnBj9jXY3mNNBKrWcjXezBUI_t-HRD2fc6EEVz3LxcYRyllKWNHh15DOZV-pnLtbKfVwhgFzM0T5twyWsefrBUHoTF4PIkaw-ODrAdgJ5zVfOmY2Q5l8Sa-xbPBbUptH',
    'Origin': 'https://lkk.verno-info.ru',
    'Connection': 'keep-alive',
    'Referer': 'https://lkk.verno-info.ru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}

data = '{"password":"","login":"' + sys,argv[1] + '"}'

response = requests.post('https://loymax.ivoin.ru/publicapi/v1.2/Registration/BeginRegistration', headers=headers, data=data)

print(response.status_code, response.text)
