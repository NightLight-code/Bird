import requests
import sys
import proxy

r = requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': sys.argv[1], "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, proxies = proxy.getproxy())

print(r.status_code, r.text, "ICQ")
