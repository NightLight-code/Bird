import requests

import sys

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'application/json',
    'Origin': 'https://www.technopark.ru',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Referer': 'https://www.technopark.ru/?utm_source=admitad&utm_medium=cpa&utm_campaign=1658832&utm_content=5d90ade16032f8c8179c6ddef28adf7d',
    'Connection': 'keep-alive',
    'TE': 'trailers',
}
#first 9
data = '{"operationName":"AuthStepOne","variables":{"phone":"' + sys.argv[1] + '","token":"tv0m892gc1ru64vdpkl0km1ah5","cityId":"36966"},"query":"mutation AuthStepOne($phone: String!, $token: String!, $cityId: ID!) @access(token: $token) @city(id: $cityId) {\\n sendOTP(phone: $phone)\\n}\\n"}'

response = requests.post('https://www.technopark.ru/graphql/', headers=headers, data=data)

print(response.status_code, response.text)
