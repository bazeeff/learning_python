import requests
#url = 'https://vk.com/bazeeff'
url = 'http://127.0.0.1:9999/echo/Egorova'
resp = requests.get(url)
data = resp.text

for key, value in resp.headers.items():
    print(key, value)
