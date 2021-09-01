import requests 

headers = {
        'authority': 'i.api.kari.com',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'accept': 'application/json, text/plain, */*',
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJZCI6IjY0YmQ5NjQ5LWQxN2MtNDJjMC04ZDdkLWI1ZTQ5MjhhYWZjOCIsImlzVGVtcCI6dHJ1ZSwiaWF0IjoxNjI5NDY5MDU5LCJleHAiOjE2MzAwNzM4NTl9.vcv4ILkED070ZbWklbcDtHILbGNk6hN-8qNtG63UcCE',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'origin': 'https://kari.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://kari.com/',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'rees46VisitorSegment=H; KariLocationId=7700000000000; utm_source=google; utm_medium=cpc; utm_campaign=ga_rus_search_tg%3Akw_brand-time-for-school_g%3Aall_s%3Aall_a%3Aall_d%3Aall; utm_content=astat%3Akwd-389560150766%7Cret%3Akwd-389560150766%7Ccid%3A14226417746%7Cgid%3A131371668171%7Caid%3A538261643274%7Cpos%3A%7Cst%3A%7Csrc%3A%7Cdvc%3Ac%7Creg%3A9047022; utm_term=%2Bkari%7Cmt%3Ap; referrer=https%3A%2F%2Fwww.google.com%2F; KariTempToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJZCI6IjY0YmQ5NjQ5LWQxN2MtNDJjMC04ZDdkLWI1ZTQ5MjhhYWZjOCIsImlzVGVtcCI6dHJ1ZSwiaWF0IjoxNjI5NDY5MDU5LCJleHAiOjE2MzAwNzM4NTl9.vcv4ILkED070ZbWklbcDtHILbGNk6hN-8qNtG63UcCE; _gcl_au=1.1.1889467062.1629469060; tmr_lvid=04cbccf145d629a776504ebc1b7bc1fc; tmr_lvidTS=1629469060704; _ga=GA1.2.2107195766.1629469061; _gid=GA1.2.1127688900.1629469061; _gac_UA-131156523-1=1.1629469061.Cj0KCQjwpf2IBhDkARIsAGVo0D3Jcm5PD-QH0wU2H79TwQDUYeWPyAQtmJlFdCHL-yJ2PB1qHjwKE3caAqeSEALw_wcB; _gcl_aw=GCL.1629469061.Cj0KCQjwpf2IBhDkARIsAGVo0D3Jcm5PD-QH0wU2H79TwQDUYeWPyAQtmJlFdCHL-yJ2PB1qHjwKE3caAqeSEALw_wcB; ssaid=61005390-01c1-11ec-98ab-4d5fd50e8a35; _gat_UA-131156523-1=1; _ym_uid=1629469061828693439; _ym_d=1629469061; _ym_isad=1; tmr_reqNum=5; __tld__=null; _ga_MR8XC96CH3=GS1.1.1629469060.1.1.1629469066.0; KariClientLocationConfirmed=true',
    }

params = (
        ('phone', '+' + phone))

response5 = requests.get('https://i.api.kari.com/ecommerce/client/registration/verify/phone/code', headers=headers, params=params)

print(response5.status_code, 'kari')
