import requests
import sys



responce = requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + sys.argv[1]})

print(responce.status_code, responce.text, "yandexfood")
