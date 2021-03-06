import requests
import sys
import os

import proxy


cookies = {
    'suuid': '895f381c-e4ee-4fe3-a61f-4d461bca20b9',
    'luuid': '895f381c-e4ee-4fe3-a61f-4d461bca20b9',
    'split_segment': '1',
    'split_segment_amount': '10',
    'XSRF-TOKEN': 'eyJpdiI6ImVKbG5ENVAzT3d6NHhLVGcwc2JlaUE9PSIsInZhbHVlIjoieGw1SkI2bFZcL3p5TzlOUVNlbVpoNUpVYk1PNUlaaG9HcUhPWUhBa1pcL3VMdUVyYnAxbWxKc2lZMUNnSzFCWndZNkdFZjdDbkd2UUt1OE11R2xqM2RKQT09IiwibWFjIjoiNDE4ZWM2NWNjOGNlZWU5OTM4NGQ2NjVkZWY3YjFkMjBiYjEyN2EzZTA5NzBmNTEwMDFmOWYxYjc1ZjliMjg3YyJ9',
    'aid': 'eyJpdiI6ImZPY200NEw4enNWYmpPWklYVTdWV1E9PSIsInZhbHVlIjoidGtRSFlaSU1xY0dES0JzZ0lcL3Q1VHFqdFwvaStXVnJ4UVF0SCtwOStvczJ3dE1xbVB0ZGdkWUtxOUVyRFJzZDFTN0hYcTRHblAxczRDMnNCSlRnQWNpUT09IiwibWFjIjoiZTdmNDBjZmU2YzM0YjI1YzIxNmRlMGFjMWZiZWJkNTZmMDEzMzRkMGQxYmY5ZTIwYjBlMmU4NDQzOGI0Y2RmYyJ9',
    'utm_source': 'eyJpdiI6IitGWFRzcktHKytKemhnbWp3aWxIeFE9PSIsInZhbHVlIjoiRG9SN1RWbDdBNVR3bnB3b1U1WUFndz09IiwibWFjIjoiMjI5Njc4ZDI3OTcyYTU1YzVmODAzZDRiMTEzMjQ4ZGVlMDQ0ODFlZWExYjdhNTI4Y2E4ZDZmZDc0NTAyNTRlZSJ9',
    'utm_medium': 'eyJpdiI6IlRtakNmT0pTTmJMT1EyS2RMTHAxSUE9PSIsInZhbHVlIjoic1ZuK2c4cU9QUXI4ODZ6VU9CVnIxUT09IiwibWFjIjoiZmZjZWFjYWI4OGFmNDA5ZDU0ZmQ2OTA4MDFjMTIyZDU3Y2Q1ZDlkMWUxYWVjMTVmNzc5ZDE1MzY2YjRlMWE0MSJ9',
    'utm_campaign': 'eyJpdiI6IkxnOEl6TE9SeWZQRnRIZm1aQzc3a3c9PSIsInZhbHVlIjoieXdJUmJDMDd6aU5PalBNeWMzXC9OYWRyUEdrRGpQUTNkNUhkdlwvM3lZU2laMmg1K01WRlJJM3FvODFpK2VYU2V0bDgzSnkzMzJ3Z0xvZTZLYkp4ZjY1dz09IiwibWFjIjoiYzkwMTVhODcwODE1ZTkzODBjMjFkOWVjZjczNTUyMDM3M2QxMmYwYTc4YWFiZWI2NDlkMDIxMTJkYjhkMTJlOCJ9',
    'http_referer': 'eyJpdiI6Imw1RlBUdDVRRXV4dkZpbFVcL3FkVnpnPT0iLCJ2YWx1ZSI6IlFkeDdjZ0tEVW14XC9WQk82Q2xqUWVYdVZKUFlNbGl1SVY2NFRGMXFSOURZPSIsIm1hYyI6ImZhOTgxMDY2MjhhMmZkOTU5ZjlhY2YxYzc4NmZiOTUwYzRmOTc2Y2YwMzdhOWZjOGVmODJiMjk4ZjJhMTc0NTcifQ%3D%3D',
    'noHouse': '0',
    'fcf': '3',
    'st_uid': '70ce968df585f6a5b1b318a29d4389e9',
    '_dy_ses_load_seq': '42403%3A1630521452017',
    '_dy_csc_ses': 't',
    '_dy_c_exps': '',
    '_dy_soct': '401501.688468.1630521441*589389.1135101.1630521441*464250.838985.1630521441*476329.867264.1630521448*484922.888305.1630521448*487393.1048570.1630521448*496179.916906.1630521448*498939.1024559.1630521448*548865.1058483.1630521448*560084.1081069.1630521448*566508.1094300.1630521448*577986.1114752.1630521448*580747.1119541.1630521448*581384.1120797.1630521448*366287.608896.1630521448*588312.1133175.1630521448*497022.1137459.1630521448*590076.1136181.1630521448*534782.1026816.1630521448*534269.1025321.1630521448',
    '_gcl_aw': 'GCL.1630521441.CjwKCAjwybyJBhBwEiwAvz4G76iWHMD41KJMOefqXLBKwabpW74qZj-bgeDbfROvzjG-iQk9cVWSEhoCP6wQAvD_BwE',
    '_gcl_au': '1.1.1693615679.1630521441',
    'splitVar': 'test01-B',
    '_dycnst': 'dg',
    '_dyid': '7102177687735420352',
    '_dyfs': '1630521448600',
    '_dyjsession': 'd4ef4de4a0d81e761eab513f9311a487',
    'dy_fs_page': 'www.vprok.ru%2F%3Futm_source%3Dgoogle%26utm_medium%3Dcpc%26utm_campaign%3Dg-search-tgo-brand-aud_nonbuy-all-day-msk%26utm_term%3D%25d0%25bf%25d0%25b5%25d1%2580%25d0%25b5%25d0%25ba%25d1%2580%25d0%25b5%25d1%2581%25d1%2582%25d0%25be%25d0%25ba%26utm_content%3Drw%7Ccampaign-g-search-tgo-brand-aud_nonbuy-all-day-msk%7Ccampaignid-14333881115%7Ckeyword-%25d0%25bf%25d0%25b5%25d1%2580%25d0%25b5%25d0%25ba%25d1%2580%25d0%25b5%25d1%2581%25d1%2582%25d0%25be%25d0%25ba%7Cgroupid-130027625230%7Cdevice-c%7Cregionid-9040982%7Cad-540277687808%7Cplacement-%7Cphraseid-kwd-353511533167%7Cadvar-dafault%7Cother%7Cdevicemodel-%26gclid%3Dcjwkcajwybyjbhbweiwavz4g76iwhmd41kjmoefqxlbkwabpw74qzj-bgedbfrovzjg-iqk9cvwsehocp6wqavd_bwe',
    '_dy_lu_ses': 'd4ef4de4a0d81e761eab513f9311a487%3A1630521452018',
    '_dycst': 'dk.l.f.ms.',
    '_dy_geo': 'UA.EU.UA_30.UA_30_Kyiv',
    '_dy_df_geo': 'Ukraine..Kyiv',
    '_dy_toffset': '0',
    '_ga_B122VKXXJE': 'GS1.1.1630521441.1.1.1630521454.47',
    '_ga': 'GA1.2.449316677.1630521442',
    'isUserAgreeCookiesPolicy': 'true',
    '_dyid_server': '7102177687735420352',
    'flocktory-uuid': '6d887e2b-a159-42b9-ac3e-fe9fa44c46c8-6',
    '_gid': 'GA1.2.269460244.1630521445',
    '_gac_UA-93122031-1': '1.1630521447.CjwKCAjwybyJBhBwEiwAvz4G76iWHMD41KJMOefqXLBKwabpW74qZj-bgeDbfROvzjG-iQk9cVWSEhoCP6wQAvD_BwE',
    '_ym_uid': '1630521445990977050',
    '_ym_d': '1630521445',
    '_gat_UA-93122031-1': '1',
    '_ym_isad': '2',
    '_fbp': 'fb.1.1630521446387.1962220188',
    '_dy_c_att_exps': '',
    'cto_bundle': 'nWjyjV9tOW8lMkJtT1lsVVA4ZWhlcjUlMkZOQWN5WkVxR05pc2ZEY1JFaSUyQjhmM21qZHMzb1FucmJMZnRBSTQ0bzZidThTNHpFWUZoMkhpV2JzY0JaTlkzWTNITDBRTDNJMVVCbUFudEltQmJ4SFJaTE9TUjRJc1NqTW1oeWE2c3BvazR2UUVoMw',
    'mindboxDeviceUUID': '12a7bb8d-048b-40a0-ad08-96e69c5dcbcb',
    'directCrm-session': '%7B%22deviceGuid%22%3A%2212a7bb8d-048b-40a0-ad08-96e69c5dcbcb%22%7D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'application/json',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://www.vprok.ru/cart',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5IiwianRpIjoiYjcyNGI0YzFmZTQ3ZmM2NTYxNmZlMTVmOGI4ZjIxY2MwMWU3YTc2MTdmYmExMTkwYTgyMDM0OTIyMGUxYTI5ZTU2MGVkOGI3OWYzNzEzYTEiLCJpYXQiOjE2MzA1MTA0MjUsIm5iZiI6MTYzMDUxMDQyNSwiZXhwIjoxNjMwNTk2ODI1LCJzdWIiOiIiLCJzY29wZXMiOltdfQ.PkMO55WPuuPAVbf5mcS-D0C7YHA7i_YG3Y2OjUvQkO9wuyAhxEATdnqrHm03qEYovM4i_xCToZVF_euocQOXl6fwUj953s8p3DzhXTvUDsYk_Je5eDouXmM17MPcyhfI6Te-plXAjMTvmbcN6nF3Lk5UEyR-NWbJGGGzvv5SxIiownB2GCvIdk4bANWDEmEee5U3McuxW5KF7ooc3gxiCYHE8xBW9L8IrP6S4kT1eaHeS2GLhkvYJWRGiSs_FVV1Zss00UD9P_DemBswjOWMoIGoNy8cDBZwxGsXHsYPV8UX0tA1zZJ02WBP4b2K-S-CY_movM7RVQyXuMphqGJYUdCUdMD78wIavKE4K5PmKbrwNn2rlAhbcmAsqNiPvhxuo-1sosMXSfkxuy77hRrUoZWD0qN7tR-RfcQddwSKPtyfKwFvPIKLI5vHI41W67WVSJFVQFUY9TXj7G9HXK5oko_CLmLxHU8u4dOYDcVnSeXeYR-bPG337S7YGaQWljq5jFMTj2d3RQzy47cw63MLRBrnzLOVCzInQOW3dRHEMoEtYN19E8k1TQkq5UJmfrJDfe8reEF5gM0P7mcE8359NR9JU3Q7fU4zlbrO4SESJ5ciF8VRnqS2XeJQTh3r9qQLoD_vai2kmnXIC0Mfas_iYg_WSYiCi2jrXG4EVM687AQ',
    'X-CSRF-TOKEN': 'Mi5uorLdHYvNQpnLggzZ8FEpRk33wDcCjbmFWfk4',
    'X-API-Context-Shop-Id': '2527',
    'X-API-Context-Region-Id': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-type': 'application/x-www-form-urlencoded charset=UTF-8',
    'Origin': 'https://www.vprok.ru',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

data = {
  'phone': sys.argv[1]
}

response = requests.post('https://www.vprok.ru/as_send_pin', headers=headers, cookies=cookies, data=data, proxies = proxy.getproxy())


print(response.status_code, response.text, "perekrestok")
