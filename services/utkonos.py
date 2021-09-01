import requests

cookies = {
    'Utk_DvcGuid': '2F97556025C03451CBE1F511201957CB',
    'Utk_LncTime': '2021-09-01+21%3A37%3A23%7C0AAFC2BA78F97FF34C19E7B7C6B8E8F8',
    'low_vision': 'false',
    'store': 'utk',
    'SGM_210714_1000': '892',
    'SGM_VAR': 'G',
    'Utk_SessionToken': '4C2F9B9DAD0EF432EF39A8EF44D1B1AB',
    '_gcl_aw': 'GCL.1630521444.CjwKCAjwybyJBhBwEiwAvz4G75TDbDIQ5XPW7rM8MvNR2WVoheyqP_SrpD0O5RmljA85wVsWhQGAABoCM1IQAvD_BwE',
    '_gcl_au': '1.1.257775071.1630521444',
    '_ym_debug': '1',
    'gtm_source': 'google',
    'gtm_medium': 'cpc',
    'Utk_MrkGrpTkn': 'EAF41BF0BBE407E97B174819018143C0',
    'uxs_uid': 'a6763ac0-0b53-11ec-a8da-1d4827ee0c18',
    '_tm_lt_sid': '1630521444569.497240',
    '_ga': 'GA1.2.882259656.1630521448',
    '_gid': 'GA1.2.1203245658.1630521448',
    '_gac_UA-8149186-8': '1.1630521448.CjwKCAjwybyJBhBwEiwAvz4G75TDbDIQ5XPW7rM8MvNR2WVoheyqP_SrpD0O5RmljA85wVsWhQGAABoCM1IQAvD_BwE',
    '_ym_uid': '1630521448466408708',
    '_ym_d': '1630521448',
    'cto_bundle': 'OMkjdV96dkNUYklSc3dYbHJOUU1sUUZ2VU00M0hTWCUyQjVxJTJCaGpLVjhYNEd1S1klMkJxYW5NaVpaTXN4U2ZvNk5nem4xOFY5NlprMmlGUGpwbUJXbWZQamlkTjlWQiUyQlFJMFBSeFBIMWVZNmZZMG5rZXdFNjVqa0pDMFIlMkJndmpwMiUyQlZjNTZEb09NMEYxJTJCeHFYRkdMcVNla0xvNU1FZyUzRCUzRA',
    '_fbp': 'fb.1.1630521448518.49525242',
    'uid': '6838902636192727040',
    '_ym_isad': '2',
    'flocktory-uuid': '893c61c9-37d4-4db4-9104-4f3956203a96-0',
    '_dc_gtm_UA-8149186-8': '1',
    'agree_with_cookie': 'true',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'ADRUM': 'isAjax:true',
    'Content-Type': 'multipart/form-data; boundary=---------------------------24439940449263771463516322237',
    'Origin': 'https://www.utkonos.ru',
    'Connection': 'keep-alive',
    'Referer': 'https://www.utkonos.ru/?utm_medium=cpc&utm_source=google&utm_campaign=desktop_competitors_p_newcus_perekrestok%7C1586251126&utm_term=%D0%BF%D0%B5%D1%80%D0%B5%D0%BA%D1%80%D0%B5%D1%81%D1%82%D0%BE%D0%BA&utm_content=k50id%7Ckwd-353511533167%7Ccid%7C1586251126%7Caid%7C514416609795%7Cgid%7C65329815488%7Cpos%7C%7Csrc%7Cg_%7Cdvc%7Cc%7Creg%7C9040982%7Crin%7C%7C&k50id=65329815488%7Ckwd-353511533167&gclid=CjwKCAjwybyJBhBwEiwAvz4G75TDbDIQ5XPW7rM8MvNR2WVoheyqP_SrpD0O5RmljA85wVsWhQGAABoCM1IQAvD_BwE',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

data = '$-----------------------------24439940449263771463516322237\\r\\nContent-Disposition: form-data; name="request"\\r\\n\\r\\n{"Head":{"DeviceId":"2F97556025C03451CBE1F511201957CB","Domain":"www.utkonos.ru","RequestId":"fd947996c73548e3f5fe1cb65ec88da8","MarketingPartnerKey":"mp-cc3c743ffd17487a9021d11129548218","Version":"angular_web_0.0.2","Client":"angular_web_0.0.2","Method":"sendSmsAuthCode","Store":"utk","SessionToken":"4C2F9B9DAD0EF432EF39A8EF44D1B1AB"},"Body":{"phone":"9222633421","requestToken":"03AGdBq27uV0N0zLOS_IyNDMxCsIXuBq8ZVO87m0te4JZN0c58Hn1CEiuixfdjnHjMl6_cj4FYAYXq01nee2V15HwKkpzZSp2q6RjHL1v1oszRdSubHb8vHtktU9yTfYve-xTXCvQXXHmmAZ7NMkg4qmIt5FXQdKcrDV9YZjhWnpeRPZBqDMNaWhlDZceqV1FLwWxTdJCT7l7bW2BV206DV17jBxBuwS_yqT3XK4nhGEjcFcMpQGYxttBYOE-1bYVrc6yg8i3cw0poPgBi7IVAuPnjceY6hRSZZQCjJ_7ILJGoYn91-mJNb2NHbKnrJw1gAtKYvJRySk9AdAsJAHEpu_OzhwTAgB67W4RkeJ6YMQNZowE8kWaymoqbpJ9Kzf2VmhuUcc_U45fwikraI2UbHpPzjzVEdVoOILlLpYwqR6zAWcQhIeIudMVrKbRFjTkFJRyIuv9BCEx2_W1mPLqPhnYMPmFCgQxqiw"}}\\r\\n-----------------------------24439940449263771463516322237--\\r\\n'

response = requests.post('https://www.utkonos.ru/api/v1/sendSmsAuthCode', headers=headers, cookies=cookies, data=data)
