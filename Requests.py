import requests
payload = {'key1':'value',
           'name':'balaji'}
r = requests.get("https://httpbin.org/get",params= payload)             #get() is used to request data from url
print(r.text)

#post():
payload2 =  {'keys1':'value1'}
res = requests.post("http://httpbin.org/post",data = payload2)
print(res.text)

#status_code:
print(r.status_code)

#cookies:
cookies = dict(key1="value1")
y=  requests.get("http://httpbin.org/cookies",cookies=cookies)
print(y.text)

#headers:
print(y.headers)
