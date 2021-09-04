import requests
import sys

response = requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+"+sys.argv[1]})

print(response.status_code, "okru")
