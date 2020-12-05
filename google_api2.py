import requests
import json

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input("Enter location:")
    if len(address) < 1:
        break
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + requests.post(parms)

    print("Retrieving",url)
    uh = requests.get(url)            #http  request
    data = uh.read().decode()                        #it will read entire data and decode it,and data is in json formati.e string format
    print("Retrieved",len(data),"characters")

    try:
        js = json.loads(data)                  #here the json will convert into dictionaries
    except:
        js = None

    if not js or 'status' not in js or js["status"] != "OK":
        print('========Failure To Retrieve =======')
        print(data)
        continue
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat:",lat,"\n","lng:",lng)
    location = js["results"][0]["formatted_address"]
    print(location)
