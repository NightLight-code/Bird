import requests

import os

import sys

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
  'phone': '+' + sys.argv[1],
  'returnUrl': '/connect/authorize/callback?client_id=www&amp;scope=openid%20offline_access%20email%20phone%20profile%20roles%20Sravni.Reviews.Service%20Sravni.Osago.Service%20Sravni.QnA.Service%20Sravni.FileStorage.Service%20Sravni.Memory.Service%20reviews%20Sravni.PhoneVerifier.Service%20Sravni.Identity.Service%20Sravni.VZR.Service%20messagesender.sms%20Sravni.Affiliates.Service%20esia%20orders.r&amp;response_type=code%20id_token%20token&amp;redirect_uri=https%3A%2F%2Fwww.sravni.ru%2Fopenid%2Fcallback%2F&amp;response_mode=form_post&amp;state=Q_60LeZi1vkySKYnmEd8oYjnwAruhwjsrE4DB6iY-j0&amp;nonce=35MNGvxjcpSW5ZVZipX_50xZABdmVMPoA-Tv8mafR7E&amp;login_hint&amp;acr_values'
}


response = requests.post('https://my.sravni.ru/signin/code', headers=headers, cookies=cookies, data=data, timeout=5)

print(response.status_code, response.text, "sravni")
