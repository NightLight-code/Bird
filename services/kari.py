import requests
import sys
import os






cookies = {
    'KariLocationId': '7700000000000',
    'utm_source': 'google',
    'utm_medium': 'cpc',
    'utm_campaign': 'ga_rus_search_tg%3Akw_brand-time-for-school_g%3Aall_s%3Aall_a%3Aall_d%3Aall_test_a_conversions',
    'utm_content': 'astat%3Akwd-389560150766%7Cret%3Akwd-389560150766%7Ccid%3A14226417746%7Cgid%3A131371668171%7Caid%3A538261643274%7Cpos%3A%7Cst%3A%7Csrc%3A%7Cdvc%3Ac%7Creg%3A9040982',
    'utm_term': '%2Bkari%7Cmt%3Ap',
    'referrer': 'https%3A%2F%2Fwww.google.com%2F',
    '_gcl_aw': 'GCL.1630607153.Cj0KCQjw7MGJBhD-ARIsAMZ0eetg4yNFw2kMsw59lsW3SCiMzZzUEHxDSfUwihjouCpQiaw1EFN0xDEaAviTEALw_wcB',
    '_gcl_au': '1.1.6055557.1630607153',
    'rees46VisitorSegment': 'F',
    '_ga_MR8XC96CH3': 'GS1.1.1630607152.1.1.1630607160.0',
    '_ga': 'GA1.2.1533389773.1630607153',
    '_ga_49W3R7LP51': 'GS1.1.1630607153.1.1.1630607160.0',
    'KariTempToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJZCI6IjkyNjk2ZDRkLTQxODUtNGRmOC1hYWNmLTRmODczNTU1NWFhZSIsImlzVGVtcCI6dHJ1ZSwiaWF0IjoxNjMwNjA3MTUzLCJleHAiOjE2MzEyMTE5NTN9.ktXvVF_Xjg0JNL5hwszZ39eMfDdA7DheD7BhzA0tui0',
    'ssaid': '3524feb0-0c1b-11ec-97ad-450a02e7e902',
    '_gid': 'GA1.2.962813093.1630607154',
    '_gac_UA-131156523-1': '1.1630607154.Cj0KCQjw7MGJBhD-ARIsAMZ0eetg4yNFw2kMsw59lsW3SCiMzZzUEHxDSfUwihjouCpQiaw1EFN0xDEaAviTEALw_wcB',
    'tmr_reqNum': '3',
    'tmr_lvid': 'e41862aeb4bdefa25a7ae646cfeaf1b7',
    'tmr_lvidTS': '1630607154281',
    '_gat_UA-131156523-1': '1',
    '_fbp': 'fb.1.1630607156004.2100181396',
    'KariClientLocationConfirmed': 'true',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJZCI6IjkyNjk2ZDRkLTQxODUtNGRmOC1hYWNmLTRmODczNTU1NWFhZSIsImlzVGVtcCI6dHJ1ZSwiaWF0IjoxNjMwNjA3MTUzLCJleHAiOjE2MzEyMTE5NTN9.ktXvVF_Xjg0JNL5hwszZ39eMfDdA7DheD7BhzA0tui0',
    'Origin': 'https://kari.com',
    'Connection': 'keep-alive',
    'Referer': 'https://kari.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'TE': 'trailers',
}

params = (
    ('phone', '+' + sys.argv[1]),
)

response = requests.get('https://i.api.kari.com/ecommerce/client/registration/verify/phone/code', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://i.api.kari.com/ecommerce/client/registration/verify/phone/code?phone=%2B79222633421', headers=headers, cookies=cookies)
