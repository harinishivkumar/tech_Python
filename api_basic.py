import requests
from pprint import pprint
with open('city.txt','r') as C:
  city = C.read()
with open('key.txt','r') as K:
  key = K.read()
K.close()
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city,key)
res = requests.get(url)
data = res.json()
print(res)
pprint (data)

///this is added for demo purpose///
