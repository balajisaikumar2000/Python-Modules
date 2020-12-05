#json is a format for storing data:
#json format is in string type we need to convert it to pythin's dictionary so we use loads() function
import json
#json
x =  '{"name":"John","age":30,"city":"New York"}'
print(x)
#parse x
y = json.loads(x)
print(y)
print(y["age"])
#now convert the python object(dict) into string by using dumps() function:
z = json.dumps(y)
print(z)
print(type(z))
print(type(y))

#converting python objects to json
import json

a = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
b = json.dumps(a,indent=4)
#indent is optional

# the result is a JSON string:
print(b)