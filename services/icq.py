import requests
import sys


r = requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': "89222633421", "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})

print(r.status_code, r.text, "ICQ")
