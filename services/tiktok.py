import requests
import sys

response = requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":sys.argv[1][1:],"page":{"pageName":"home","launchMode":"direct","trafficType":""}})


print(response.status_code, response.text, "tiktok")
