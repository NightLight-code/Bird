import requests
import sys
import proxy
cookies = {
    'PHPSESSID': 'atuukp80a0m25l78u4tkhoidf1',
    'BITRIX_SM_admitad_broker': 'google',
    'BITRIX_SM_utm_source': 'google',
    'BITRIX_SM_utm_medium': 'cpc',
    'BITRIX_SM_utm_term': '%D1%81%D0%B1%D0%B5%D1%80+%D0%B0%D0%BF%D1%82%D0%B5%D0%BA%D0%B0',
    'BITRIX_SM_utm_campaign': 'g_srch_msk_Konkurenty_new%7C13555614473',
    'BITRIX_SM_utm_content': 'k50id%7Ckwd-1184463619606%7Ccid%7C13555614473%7Caid%7C543451584403%7Cgid%7C127400384567%7Cpos%7C%7Csrc%7Cg_%7Cdvc%7Cc%7Creg%7C9040982%7Crin%7C9047022%7C',
    'BITRIX_SM_utm_exists': '1',
    'BITRIX_SM_ABTEST_s1': '1%7CB',
    'BITRIX_SM_LAST_REG_CODE': 'Moscowregion',
    'BITRIX_SM_OLD_FAVORITES_CHECKED': 'Y',
    '_ttgclid': 'Cj0KCQjwssyJBhDXARIsAK98ITTkhDZP8IDI69AU6DSIoz2_g3bMfRfirXQQMrYHbeIUhoIf3N0zR6EaAprwEALw_wcB',
    'BX_USER_ID': '3f66791853a2b1c0566f6fdbc1cf473a',
    'mindboxDeviceUUID': '12a7bb8d-048b-40a0-ad08-96e69c5dcbcb',
    'directCrm-session': '%7B%22deviceGuid%22%3A%2212a7bb8d-048b-40a0-ad08-96e69c5dcbcb%22%7D',
    '_gcl_aw': 'GCL.1630760382.Cj0KCQjwssyJBhDXARIsAK98ITTkhDZP8IDI69AU6DSIoz2_g3bMfRfirXQQMrYHbeIUhoIf3N0zR6EaAprwEALw_wcB',
    '_gcl_dc': 'GCL.1630760382.Cj0KCQjwssyJBhDXARIsAK98ITTkhDZP8IDI69AU6DSIoz2_g3bMfRfirXQQMrYHbeIUhoIf3N0zR6EaAprwEALw_wcB',
    '_gcl_au': '1.1.1639154708.1630760382',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    'flocktory-uuid': '5b817055-6a4e-40ca-813b-ca526aece4b0-1',
    'tmr_reqNum': '14',
    'tmr_lvid': '3f7d8a65f6d711c5e7456c155f8bd64c',
    'tmr_lvidTS': '1630760383223',
    '_ym_uid': '1630760384987704571',
    '_ym_d': '1630760384',
    '_ga': 'GA1.2.418694563.1630760384',
    '_gid': 'GA1.2.141589943.1630760384',
    '_gac_UA-60065697-1': '1.1630760399.Cj0KCQjwssyJBhDXARIsAK98ITTkhDZP8IDI69AU6DSIoz2_g3bMfRfirXQQMrYHbeIUhoIf3N0zR6EaAprwEALw_wcB',
    '_ym_visorc': 'b',
    'HIDE_DESCRIPTION_HEADER_BANNER': 'Y',
    '_ym_isad': '2',
    '_gat_UA-60065697-1': '1',
    '_userGUID': '0:kt5smln2:JPVxRN7~r5kd3Mv~_FCEEDn4M3hozQWx',
    '_fbp': 'fb.1.1630760384306.22966058',
    '_gaexp': 'GAX1.2.R4t285vKRSW2lBuD76A3kA.18956.1',
    '_dc_gtm_UA-60065697-1': '1',
    'dSesn': 'ddaaf97e-97ff-2fe5-7570-ccffb591bd28',
    '_dvs': '0:kt5smln2:1isUU_M1SpxD3te9lGkSQMPiumhAdA9D',
    'cto_bundle': 'PjiUPF9Cdjg1UzIyMEJmWVZjQzhJYThJM3ZBRFoxZGNvWWlMMVVIWmxJUXJSMzVPcDZEeVJYamFoJTJGMW5tJTJGRlBpMWY3SlUxQnZLeTZoMEZIb1MwWThxQlF2R2x0YjElMkJXWVdFR005cG9oWlE1OTkxRHlwb2hQcnVUcFc3QmphaCUyRjR1QTVyb0RNbVVkMFVRMjhDdmlhdjZUa2ZJdyUzRCUzRA',
    'tmr_detect': '0%7C1630760385875',
    '_gali': 'registration-new-phone',
    'lastRegData': 'sessid%3D806abc9ea18c056a75c0e117c4f87341%26enter_back_url%3D%26save%3DY%26send_message_drug_id%3D%26buyer_phone%3D%28922%29263-34-21%26tmpphone%3D9222633421%26sms_cod%3D%26buyer_name%3D%26buyer_surname%3D%26buyer_email%3D%26my_health_cart%3DY%26register_buyer%3DY',
    'd7a7fd7sa6': '-1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://zdravcity.ru',
    'Alt-Used': 'zdravcity.ru',
    'Connection': 'keep-alive',
    'Referer': 'https://zdravcity.ru/?&https://clickserve.dartsearch.net/link/click?lid=43700064500711762&ds_s_kwgid=58700007188080484&matchtype=b&utm_source=google&utm_medium=cpc&utm_campaign=g_srch_msk_Konkurenty_new%7c13555614473&utm_term=%D1%81%D0%B1%D0%B5%D1%80%20%D0%B0%D0%BF%D1%82%D0%B5%D0%BA%D0%B0&utm_content=k50id%7ckwd-1184463619606%7ccid%7c13555614473%7caid%7c543451584403%7cgid%7c127400384567%7cpos%7c%7csrc%7cg_%7cdvc%7cc%7creg%7c9040982%7crin%7c9047022%7c&k50id=127400384567%7ckwd-1184463619606&gclid=Cj0KCQjwssyJBhDXARIsAK98ITTkhDZP8IDI69AU6DSIoz2_g3bMfRfirXQQMrYHbeIUhoIf3N0zR6EaAprwEALw_wcB&gclsrc=aw.ds',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers',
}

data = {
  'phone': sys.argv[1][1:],
  'bxsid': '806abc9ea18c056a75c0e117c4f87341',
  'sms1': 'Y',
  'typeAction': 'regUser'
}

response = requests.post('https://zdravcity.ru/ajax/sendcode.php', headers=headers, cookies=cookies, data=data, proxies = proxy.getproxy())

print(response.status_code, response.text, "zdravcity")
