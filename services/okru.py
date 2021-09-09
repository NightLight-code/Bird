import requests
import sys
import proxy

response = requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+"+sys.argv[1]}, proxies = proxy.getproxy())

print(response.status_code, "okru")
