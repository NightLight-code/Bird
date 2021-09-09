import requests
import sys
import proxy

responce = requests.post('https://www.citilink.ru/registration/confirm/phone/+'+sys.argv[1]+'/', proxies = proxy.getproxy())

print(responce.status_code, responce.text, "citilink")
