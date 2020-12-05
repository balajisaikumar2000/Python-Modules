import json
data = """{
"name" : "Chuck",
"phone":{
  "type" : "int1",
  "number":"9182698988"
  },
  "email":{
   "hide":"yes"
   }
}"""
info = json.loads(data)
print("Name:",info["name"])
print("Hide:",info["email"]["hide"])

#str is converted to dict
print(type(data))
print(type(info))

