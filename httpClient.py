import urllib.request as ur
url = 'https://vk.com/bazeeff'
conn = ur.urlopen(url)
data = conn.read()
print(conn.status)

#print(conn.getheader('Content-Type'))
#print(data)

for key, value in conn.getheaders():
    print(key, value)
