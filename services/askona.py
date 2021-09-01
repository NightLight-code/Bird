import requests



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
