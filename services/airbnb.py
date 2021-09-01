import os
import requests



cookies = {
    'bev': '1630519056_NzEwMzg1MDE4MDA4',
    'country': 'UA',
    '_abck': '7632F553CFC80E5AE60D187F2CF8198D~-1~YAAQTgoQAlM2zKB6AQAAR1mCogZvkxDmYSbjxJYIZFjVOndxOalwolXOUlDwylvjlR2Mxll+7eHFHtLvjNmWsj81M2C4e444IAXXGOugruO7x3uzBytMdRm72pOs+Y1XbmPqS90ghxIq/uJGmZYqQXbhr4U0/9HxpzRJymGhrX9GdViEe+gZmI96RWXr2BNK4hY6sy4hzxEeWT2PvuMZmyEwYLHx/61Ds1vNC1pjt2y6bcLmbITWZs6FP4AguAJa2CztNzofX5ExTnQYaUKAYseJc8/oQ+LW36X7+QXhmybTy29iubhqs8aX05SZevGiSgXaDtLXZIetkKm1uvftVzdxnzVwTuqL6XRva0/m6QxOcOFkmf4EkDc=~-1~-1~-1',
    'ak_bmsc': '842F82FA7379446D556305F3697E32D6~000000000000000000000000000000~YAAQTgoQAlQ2zKB6AQAAR1mCogxOLCibBw5ZBMIKxSnsKZsBMOI+n165Lm23zcBen5BhdO4XOo5cnurVA1EcDJGj96VNH3owsqaW+3/6hOJSThk4siNOhPjkObmXL2i6a/DoipNgFamBkOso534eDoqxGQX20tuXeGYwRmImDrDom0M4KAaceChY1abGGEPs6zKVVmyPUbPE5uFA8bmb2wT9KgtxijtfU34ZYmrSFBIEDkUJxO9d8PA41nkR6QmQi4RBkMexBvqtQ3Lc313k/gO+yGIClsexxceMGOH9f7OOGQ5QiunZ+rhKa3T5/2CZBFDulYoliMvAQ5TuM35KLA7nJasF9+Jc+q1dAeveGoxjeZQiBPJ2DctuNSVuJTJRxkumhqtPgiV5pQ==',
    'bm_sz': 'FBE2A1FE4048EB0C29AABF1BE6DC966F~YAAQTgoQAlU2zKB6AQAAR1mCogxe714HVqF2AiakaaLH9sBfiFbG9l3mBZiLrrKLAyEBQngf2vscKZMbd63IIl0gsFIC53JiwlqaIop1fSnNHThFn78lF3Sa0QGMHmBLEYKVaJ8A0w3SVLWng5pnAaO9qGJK8WmJNpPWBf2qM+cmVxVK7XlRTA19iHTq0jeety9QOtuIXWT7eoj87CwKDBnFULr9W+1XmO5N8SCtRrZXw6Mx/Wu9mkqKZ5o2QgwMzNM+eBSQdpVWHgPSGZglrS2JHJmhDqt+fgiu5nAk9Px7ayc=~3421509~3162681',
    '_airbed_session_id': 'bc13e975f19be3fbc3afb2e84509ce20',
    '_user_attributes': '%7B%22curr%22%3A%22USD%22%2C%22guest_exchange%22%3A1.0%2C%22device_profiling_session_id%22%3A%221630519057--1c83230b40e703cf0087f71c%22%2C%22giftcard_profiling_session_id%22%3A%221630519057--c54a3941133bc7156266450f%22%2C%22reservation_profiling_session_id%22%3A%221630519057--45550be8292e51028d19bfb0%22%7D',
    'bm_sv': '3248BDB178949F121ED0BA846E36CD6C~0a69XQiWltC15mYoU3pXd3PBBos6YWomkc6zWzoGs/Kw0JGAcCA0+RULYCuYvL7xRAZCpoWRdyl+hKyQ7KbzJrVGuXkoXVh27mh+Vw7bSsFYqvdX4Pey2Hd6i5Fl7FGH0cyjiI6st4OIuxQm0Pct5uBIA525/7BMoaGQ8ozxbYo=',
    '_csrf_token': 'V4%24.airbnb.com%24IBO95PbmPwo%24Ti0cfJFqSflLMlcdwxWFAIpzJIWhhLJDCteTHHpeM_c%3D',
    'jitney_client_session_id': '3b4e7f3b-a647-452a-b88b-e54c4c5c2295',
    'jitney_client_session_created_at': '1630519744',
    'jitney_client_session_updated_at': '1630519745',
    'flags': '0',
    'previousTab': '%7B%22id%22%3A%225ccf9faa-87f9-4f31-a752-877145d92a2e%22%2C%22url%22%3A%22https%3A%2F%2Fru.airbnb.com%2F%3F_set_bev_on_new_domain%3D1630519056_NzEwMzg1MDE4MDA4%22%7D',
    'frmfctr': 'wide',
    'OptanonAlertBoxClosed': 'NR',
    'cfrmfctr': 'DESKTOP',
    'cbkp': '3',
    'cdn_exp_66b445b2c5988d404': 'treatment',
    'cdn_exp_e417cda70bdc6d8bc': 'control',
    '__ssid': 'a8817a82283410d11958b4748a2d5ee',
    'auth_jitney_session_id': '135fdfde-7eff-4133-a2da-bd3aad7d2a64',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://ru.airbnb.com/?_set_bev_on_new_domain=1630519056_NzEwMzg1MDE4MDA4',
    'X-Airbnb-Supports-Airlock-V2': 'true',
    'X-AIRBNB-RECAPTCHA-TOKEN': 'WEB-V3:03AGdBq24Vpp43QlY6zEWJUu1n3OC4UGVi09zDIxd6ZE9ah3KfxuI3LHhsE5nrks4UIWPfF8-WyQo99cLEc3PeZMY1LMQn8M-vrqw6p69dqYIe3N-3lVxfRiIiJT4ztVqMp8FE7Yt6xCaQhV13VRkdWkJfRRynBy_M2orLOpVElirfyHOBzph2NEPi2jLJ3kuI1czdoNdhUit7dxQ1GiW6aCaZbn1jX-X4s6ao8zcOa8bejq8bA2cVThM9VvGMBanbEM-mWl7MijjPm6M-4pXpRUDbNJRtt7sOz40GJCVRtVWMqxhO9pubLBhPb1jxYNZpU28IRQOY-z5CvpKf84oJIctn7yjkp0n48NfH-PgOe573g3su9zTsr8V5sN6NUK0AfjZ89YAs0NIhTQYYQ3YdcZHjk7CEHqakwQzP3J2VIjTOmPLCblkMKCGxrzNHpT28zLW3sA-YYTysRLMikpnZNetfElih_C5p04aFT2ziZf4salRcIfrJHRYv9c-OmCxc_jbP4zaUepigpbghyOAmweGAGTGusjPGBjHeTMc40Q-bwzS2aGimL50cTF2OLY45AbYCFkowbIv0RWgFCaEy--fiA35C59YC7ItqT2vMxSi_ZbRFk8C9TFA0YTdT2AYI2E6QOgqR21OdWyKspkoKaYIOW4GrCYyESsfxkpTNpIgWLhhhwm8Km2OovTk3Co_kMrRrNTfalLsFz282Acb8y838IfopcMybT2z4cb_Y4Aztm4bEa0cvYw122kXag8cBY6kAZWG9j9bTy2mwND94k2GkwgazL_DkqX6xPfNSydHMGhQVE9XzmWV4Y2oCkQ8nnsBCHgRVi44AntN5ZHuKEX5NwcBeXPGuWoytsF8FpPWUOG9YSKra1ViJDv7qVYzhvpDq4zafKsEsVBTrzezoViCvfmF4PYiPNHCCr8hpGFd8stBsTseyOuxSybZeFd3NJutgOAmXVyYO5lCzk32eX6A3PtsjBdeu7Nz9TntylGWBncJudN5T8Np0pTwRv95F_tI79-DaPcQA4NHd0BfeLrsaBpBs1mG3aYlx_2IJV04Ij_Vbvr92bYpgqb4RjUyep9D65v02F-lto6JLNGyvMLbRploxkk_2IIdS9AJ-Pgh69DEOwBQfa0ahxeFpctHs0XVuU_HhDbKYMLWmT0JTWAwWIgYS8BoBItYGNvJis3Vo-uU8rutquRY',
    'X-CSRF-Without-Token': '1',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/json',
    'Origin': 'https://ru.airbnb.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers',
}

params = (
    ('currency', 'USD'),
    ('key', 'd306zoyjsyarp7ifhu67rjxn52tv0t20'),
    ('locale', 'ru'),
)

data = '{"phoneNumber":"79222633421","workFlow":"GLOBAL_SIGNUP_LOGIN","otpMethod":"AUTO","accountIdentifier":"","accountIdentifierType":"PHONE"}'

response = requests.post('https://ru.airbnb.com/api/v2/phone_one_time_passwords', headers=headers, params=params, cookies=cookies, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://ru.airbnb.com/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=ru', headers=headers, cookies=cookies, data=data)
