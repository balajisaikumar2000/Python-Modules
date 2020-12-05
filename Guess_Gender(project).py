import json
from urllib.request import urlopen
name = input("Enter your name:")
myKey = "Place Your Key Here"    #we want key to execute the programme
url = "https://gender-api.com/get?key="
url=url + myKey + f"&name={name}"
response = urlopen(url)
decoded = response.read().decode('utf-8')
data =  json.loads(decoded)
print("Gender:" + data["gender"])