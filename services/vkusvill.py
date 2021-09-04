import requests

import sys



cookies = {
    'PHPSESSID': 'fBBg3UnqBrKxH4S1cN5A0yvavIJo8BPE',
    'BITRIX_SM_SALE_UID': '87446020',
    'BITRIX_SM_REGION_ID_3': '3872',
    'SERVERID': 'bitrix01',
    'ShowLangChange4': 'Y',
    'uxs_uid': '6bc8b260-0d81-11ec-be12-cb60d47976ef',
    'BX_USER_ID': '3f66791853a2b1c0566f6fdbc1cf473a',
    'tmr_reqNum': '3',
    'tmr_lvid': '949f56b6f3a5f11c541f3f69c80d9e14',
    'tmr_lvidTS': '1630761006727',
    '_ga': 'GA1.2.1138987411.1630761007',
    '_gid': 'GA1.2.978970118.1630761007',
    '_gac_UA-138047372-1': '1.1630761030.Cj0KCQjwssyJBhDXARIsAK98ITRVZBDGckRymoPCmo7-FEsTEjb2VkHayGUYcIZ9wcVDO1um9lRUgPYaAlTOEALw_wcB',
    '_gat_gtag_UA_138047372_1': '1',
    '_gac_': '1.1630761007.Cj0KCQjwssyJBhDXARIsAK98ITRVZBDGckRymoPCmo7-FEsTEjb2VkHayGUYcIZ9wcVDO1um9lRUgPYaAlTOEALw_wcB',
    '_ym_uid': '1630761007325018697',
    '_ym_d': '1630761007',
    '_fbp': 'fb.1.1630761007468.48762324',
    '_ym_isad': '2',
    'tmr_detect': '0%7C1630761009474',
    '_gat_UA-138047372-1': '1',
    'pw_deviceid': '6cd42e9a-c192-482a-8347-b1aa8b426bf0',
    'pw_status_e13b8176c02dbab146cb9f74950c9be7c19d223cd33ae1592c6990de6bf2a1d9': 'deny',
    'WE_USE_COOKIE': 'Y',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://vkusvill.ru',
    'Connection': 'keep-alive',
    'Referer': 'https://vkusvill.ru/goods/?utm_source=google&utm_medium=cpc&utm_campaign=g_s_brand_msk_catalog_11408266051&utm_content=|pid|kwd-311576656943|cid|11408266051|aid|476130430001|gid|111179537686|pos||src|g_|dvc|c|reg|9040982|rin|&utm_term=%D0%B2%D0%BA%D1%83%D1%81%D0%B2%D0%B8%D0%BB%D0%BB&9040982_&gclid=Cj0KCQjwssyJBhDXARIsAK98ITRVZBDGckRymoPCmo7-FEsTEjb2VkHayGUYcIZ9wcVDO1um9lRUgPYaAlTOEALw_wcB',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

data = {
  'FUSER_ID': '87446020',
  'USER_NAME': '\u0412\u0438\u043A\u0442\u043E\u0440',
  'USER_PHONE': '+' + sys.argv[1],
  'token': '',
  'is_retry': 'N'
}

response = requests.post('https://vkusvill.ru/ajax/user_v2/auth/check_phone.php', headers=headers, cookies=cookies, data=data)


print(response.status_code, response.text, "vkusvill")
