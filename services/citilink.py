import requests
import sys


responce = requests.post('https://www.citilink.ru/registration/confirm/phone/+'+sys.argv[1]+'/')

print(responce.status_code, responce.text, "citilink")
