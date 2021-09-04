import requests
import sys
import os


cookies = {
    '_JHASH__': '236',
    '_JUA__': 'Mozilla%2F5.0%20%28X11%3B%20Fedora%3B%20Linux%20x86_64%3B%20rv%3A91.0%29%20Gecko%2F20100101%20Firefox%2F91.0',
    '_HASH__': '86df034cc0c5360be7c06f212dc88a92',
    'MVID_CITY_ID': 'CityCZ_975',
    'MVID_GUEST_ID': '18084020112',
    'MVID_VIEWED_PRODUCTS': '',
    'SameSite': 'None',
    'wurfl_device_id': 'generic_web_browser',
    'JSESSIONID': 'QPfYhvKGf4yTz5wQqn2cJCTwM6PQxnGTvRSGJLgnVcQVbnrsLDdJ!1819081101',
    'MVID_GET_LOCATION_BY_DADATA': 'DaData',
    'MVID_REGION_ID': '1',
    'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
    'HINTS_FIO_COOKIE_NAME': '1',
    'MVID_YA_BLOCKER': '1',
    'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
    'searchType2': '3',
    'COMPARISON_INDICATOR': 'false',
    'CACHE_INDICATOR': 'true',
    'flacktory': 'no',
    'BIGipServeratg-ps-prod_tcp80': '2936331274.20480.0000',
    'bIPs': '672961728',
    'MVID_GTM_BROWSER_THEME': '1',
    'MVID_GEOLOCATION_NEEDED': 'true',
    'deviceType': 'desktop',
    '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VKWyNGHxV0NnlZHiVvHlggNGFROiVuYRASeUlcNVt2aydBZmxnHVxXNzIUSQlFTSZZVSkVGjxtHmhHYSBEVU5qJh8Ud3AlUA8UX0BCbWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzdilAZx5nUGIjSF5Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=eXZTXw==',
    'BIGipServeratg-ps-prod_tcp80_clone': '2936331274.20480.0000',
    'SMSError': '',
    'authError': '',
    '_ga_CFMZTSS5FM': 'GS1.1.1630521899.1.1.1630521903.0',
    '_ga': 'GA1.2.1496370263.1630521900',
    '_ga_BNX5WPP3YK': 'GS1.1.1630521899.1.1.1630521903.56',
    'cfidsgib-w-mvideo': 'c42sXRvtuyaaLYFCXcslT1Ogl+EdGygITrw3TkAtNOpRWi8b+GqQ6MTgsBQd2DwQKJsjo8Aq9suptPTXHmUgn/rnyPsLHWAmqwyeLa60wWNm7LDeHV97ioohNjtXHY4azXSrc0Y5d1sVB2r/3TbZpSBNAh4LUuCJwto/',
    '_gid': 'GA1.2.322387676.1630521900',
    'st_uid': '3cdb53c5e158ad53c511235f2abd33d8',
    'gsscgib-w-mvideo': '4Vj8jBpCd9KzuOZpjv9WOKgK0qgmeG/5lXxYL5Ky0nvP43dD0uUZt7NUM1gTsjwiFKGTOvQ0kmtjEYLu54wTbgMh9eM7qknz/KLnWagueuckp5HVjtnKEXl3ISgSAUjay0o9YQ0LmMtYm7buSQPQLWJqsJT/9Ueh7UmPLomNq0fRgT9xT0ptXnddh9Kb9TLcBaJB+fF8PD2INKeGClpfVDD0OpaRJFeaEhI2zrnnyJ+x2AXpZ5V8VixOPYjinA==',
    'fgsscgib-w-mvideo': 'HI895c47ee2e819833f9fda181722435eb244a4c',
    '_gaexp': 'GAX1.2.vVIPilFiQDm1r2lTJzCaJQ.18888.0!fG1AKyiuQ-6vh5P-I5pnCA.18921.0!Im3AcpciSjOJ4uNYUXTi2A.18963.2',
    '_dc_gtm_UA-1873769-1': '1',
    '_gat_owox37': '1',
    '_fbp': 'fb.1.1630521902751.1573066217',
    'blueID': '67ffe8b7-7057-486b-bc00-bcc0b255f0d6',
    'afUserId': 'f9863ecc-3e73-4f6d-b255-8de2b3f11fd8-p',
    'AF_SYNC': '1630521903162',
    '_gcl_au': '1.1.8475697.1630521904',
    '_dc_gtm_UA-1873769-37': '1',
    '_gat_UA-1873769-44': '1',
    'uxs_uid': 'b8c0e350-0b54-11ec-baa1-894616759d23',
    '_ym_uid': '1630521905754980217',
    '_ym_d': '1630521905',
    '_ym_isad': '2',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'X-GIB-GSSCgib-w-mvideo': '4Vj8jBpCd9KzuOZpjv9WOKgK0qgmeG/5lXxYL5Ky0nvP43dD0uUZt7NUM1gTsjwiFKGTOvQ0kmtjEYLu54wTbgMh9eM7qknz/KLnWagueuckp5HVjtnKEXl3ISgSAUjay0o9YQ0LmMtYm7buSQPQLWJqsJT/9Ueh7UmPLomNq0fRgT9xT0ptXnddh9Kb9TLcBaJB+fF8PD2INKeGClpfVDD0OpaRJFeaEhI2zrnnyJ+x2AXpZ5V8VixOPYjinA==',
    'X-GIB-FGSSCgib-w-mvideo': 'HI895c47ee2e819833f9fda181722435eb244a4c',
    'ADRUM': 'isAjax:true',
    'Origin': 'https://www.mvideo.ru',
    'Connection': 'keep-alive',
    'Referer': 'https://www.mvideo.ru/login?type=individual',
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

response = requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', headers=headers, params=params, cookies=cookies, data=data)

print(response.status_code, response.text, "mvideo")
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp?pageName=loginByUserPhoneVerification&fromCheckout=false&fromRegisterPage=true&snLogin=&bpg=&snProviderId=', headers=headers, cookies=cookies, data=data)
