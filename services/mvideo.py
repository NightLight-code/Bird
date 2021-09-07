import requests
import sys
import os


cookies = {
    'MVID_CITY_ID': 'CityCZ_975',
    'MVID_GUEST_ID': '18084020112',
    'MVID_VIEWED_PRODUCTS': '',
    'wurfl_device_id': 'generic_web_browser',
    'MVID_GET_LOCATION_BY_DADATA': 'DaData',
    'MVID_REGION_ID': '1',
    'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
    'HINTS_FIO_COOKIE_NAME': '1',
    'MVID_YA_BLOCKER': '1',
    'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
    'searchType2': '3',
    'COMPARISON_INDICATOR': 'false',
    'deviceType': 'desktop',
    '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VAfWk3H0pfO0lvGx0mGS4RNGNyRSd3QF91dGc7F0MtEnw/fmgdeW5aOn1yRGkvEypUaHMcGjhmIWJQXh9FXk59FhoXemwjUwkNXEZFb3kbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueSw8ZSFhSVsjQ1pNdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIWZzLyZw==',
    '_ga_CFMZTSS5FM': 'GS1.1.1631042220.2.1.1631042223.0',
    '_ga': 'GA1.2.1496370263.1630521900',
    '_ga_BNX5WPP3YK': 'GS1.1.1631042220.2.1.1631042223.57',
    'cfidsgib-w-mvideo': 'imvUtz/Kbovboi01Cf2mjveCw5yTbQ/5U9XNDkIlcN+ItcPWItoqATZbrd5gXI/VOVU1KP4OcWhbAuBUhCN3kHKCKJ1SPbR/u/l18Wb2mtQmCR/6l7yfVqgyDNAuEvz26NZXgx312rkvLc+wXOLrmrspYk1IAkAvP2FHpg==',
    'gsscgib-w-mvideo': 'KnvOAVjE7z1wpG+igH99O1j/q5ovwNEs7/zxEbDqpm3LhqdW1MSh92DJXGE4Gj4eecEJnAspCvmqs0x7eDb4Br2FrcBcMJcQBt7+SiV7RZr0L6bqhAf7hn4hEIOa7ykVbLxuIvnWVtCuRRuoq0moIm2cWN8DA+ALeZmliQeM96bu8ospdmsYVq4gOw5ZhNEJvHv75r8Wmp+/pzHY/WWhQuK7tI+PTLemE4vo1UnflzVHayR05OtEQddwE+tvtA==',
    'fgsscgib-w-mvideo': '904Ja823587ec8c35e358f126bf0788d30f66500',
    '_gaexp': 'GAX1.2.vVIPilFiQDm1r2lTJzCaJQ.18888.0!fG1AKyiuQ-6vh5P-I5pnCA.18921.0!Im3AcpciSjOJ4uNYUXTi2A.18963.2',
    '_fbp': 'fb.1.1630521902751.1573066217',
    'blueID': '67ffe8b7-7057-486b-bc00-bcc0b255f0d6',
    'afUserId': 'f9863ecc-3e73-4f6d-b255-8de2b3f11fd8-p',
    'AF_SYNC': '1630521903162',
    '_gcl_au': '1.1.8475697.1630521904',
    'uxs_uid': 'b8c0e350-0b54-11ec-baa1-894616759d23',
    '_ym_uid': '1630521905754980217',
    '_ym_d': '1630521905',
    '_RE__': 'Y359eHQ8Kit0dXYua2JhaHx0PHB7eDk=',
    '_HASH__': 'c4fa98ffd5cad1fc4d5be53c10d4324b',
    'SameSite': 'None',
    'JSESSIONID': 'Gr4Jh36L6JvL10MBqpSnLL3N81n0ZVvsSPkCx0yqY67QJX8wGW6Q!-1439502914',
    'CACHE_INDICATOR': 'true',
    'flacktory': 'no',
    'BIGipServeratg-ps-prod_tcp80': '2416237578.20480.0000',
    'bIPs': '1949759381',
    'MVID_GTM_BROWSER_THEME': '1',
    'MVID_GEOLOCATION_NEEDED': 'false',
    '_gid': 'GA1.2.415839980.1631042221',
    '_gac_UA-1873769-1': '1.1631042221.Cj0KCQjwm9yJBhDTARIsABKIcGarQeCuNhR1NyM9Olatl8dwq0OAI5em-opTNlJ6vvk1hybk5IhAYEEaAi5kEALw_wcB',
    'BIGipServeratg-ps-prod_tcp80_clone': '2416237578.20480.0000',
    'utm_source': 'adwords',
    '__SourceTracker': 'google__cpc',
    'admitad_deduplication_cookie': 'google__cpc',
    '__cpatrack': 'google_cpc',
    '__sourceid': 'undefined',
    '__allsource': 'undefined',
    '_dc_gtm_UA-1873769-1': '1',
    '_gat_UA-1873769-1': '1',
    'SMSError': '',
    'authError': '',
    '_gac_UA-1873769-37': '1.1631042221.Cj0KCQjwm9yJBhDTARIsABKIcGarQeCuNhR1NyM9Olatl8dwq0OAI5em-opTNlJ6vvk1hybk5IhAYEEaAi5kEALw_wcB',
    '_gat_owox37': '1',
    '_gcl_aw': 'GCL.1631042221.Cj0KCQjwm9yJBhDTARIsABKIcGarQeCuNhR1NyM9Olatl8dwq0OAI5em-opTNlJ6vvk1hybk5IhAYEEaAi5kEALw_wcB',
    '_dc_gtm_UA-1873769-37': '1',
    'tmr_reqNum': '10',
    'tmr_lvid': '385cfcaa46b07f037cf3c279a92f44c5',
    'tmr_lvidTS': '1631042221489',
    '_ttgclid': 'Cj0KCQjwm9yJBhDTARIsABKIcGarQeCuNhR1NyM9Olatl8dwq0OAI5em-opTNlJ6vvk1hybk5IhAYEEaAi5kEALw_wcB',
    '_gac_UA-1873769-44': '1.1631042222.Cj0KCQjwm9yJBhDTARIsABKIcGarQeCuNhR1NyM9Olatl8dwq0OAI5em-opTNlJ6vvk1hybk5IhAYEEaAi5kEALw_wcB',
    '_gat_UA-1873769-44': '1',
    'ADRUM': 's=1631042222200&r=https%3A%2F%2Fwww.mvideo.ru%2F%3F-868051077',
    '_ym_isad': '2',
    'tmr_detect': '0%7C1631042226834',
    'ADRUM_BTa': 'R:27|g:dca86c24-0f13-4d2c-b924-855502f0ff0b|n:customer1_ae7323db-e756-48ff-9e85-91c314c4b57e',
    'ADRUM_BT1': 'R:27|i:3878|e:0',
}


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'X-GIB-GSSCgib-w-mvideo': 'KnvOAVjE7z1wpG+igH99O1j/q5ovwNEs7/zxEbDqpm3LhqdW1MSh92DJXGE4Gj4eecEJnAspCvmqs0x7eDb4Br2FrcBcMJcQBt7+SiV7RZr0L6bqhAf7hn4hEIOa7ykVbLxuIvnWVtCuRRuoq0moIm2cWN8DA+ALeZmliQeM96bu8ospdmsYVq4gOw5ZhNEJvHv75r8Wmp+/pzHY/WWhQuK7tI+PTLemE4vo1UnflzVHayR05OtEQddwE+tvtA==',
    'X-GIB-FGSSCgib-w-mvideo': '904Ja823587ec8c35e358f126bf0788d30f66500',
    'ADRUM': 'isAjax:true',
    'Origin': 'https://www.mvideo.ru',
    'Connection': 'keep-alive',
    'Referer': 'https://www.mvideo.ru/login',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers',
}

params = (
    ('pageName', 'loginByUserPhoneVerification'),
    ('fromCheckout', 'false'),
    ('fromRegisterPage', 'true'),
    ('snLogin', ''),
    ('bpg', ''),
    ('snProviderId', ''),
)

data = {
  'phone': '+' + sys.argv[1],
  'g-recaptcha-response': '',
  'recaptcha': 'on'
}

response = requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', headers=headers, params=params, data=data, cookies = cookies)

print(response.status_code, response.text, "mvideo")
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp?pageName=loginByUserPhoneVerification&fromCheckout=false&fromRegisterPage=true&snLogin=&bpg=&snProviderId=', headers=headers, cookies=cookies, data=data)
