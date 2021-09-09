import requests
import sys
import proxy

response = requests.get('https://www.askona.ru/api/registration/sendcode?csrf_token=d0e09be3bd6eb8ab1f7ecdf5ae3afe49&contact[phone]=' + sys.argv[1], proxies = proxy.getproxy())

print(response.status_code, response.text)
