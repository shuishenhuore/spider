import requests

url =
res = requests.get(url).json()['data']
name = res.split('/')[-1]
imgUrl = res.strip()