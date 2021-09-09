import requests
import random


def getproxy():

    getlist = requests.get('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt')

    proxylist = getlist.text.splitlines()

    proxy = random.choice(proxylist)

    print(proxy)


    proxies = {
        "http": 'http://' + proxy,
        "https": 'https://' + proxy
    }

    print(proxies)

    return proxies


getproxy()
