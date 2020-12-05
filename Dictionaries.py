#dictionaries are unordered,muttable,indexed:
x = {
    "brand":"ford",
    "model":"mustang",
    "year":1964
}

print(x["brand"])
#get():
print(x.get("hums","this is will execute if no match found"))
x["year"] = 2010
#---------
for a in x:
    print(a)
#--------
for a in  x:
    print(x[a])
#------
for a in  x.values():
    print(a)
#--------
for a,b in x.items():
    print(a,b)
print(len(x))
#----------
x["color"] = "blue"
print(x)

#pop():(REMOVE AN ITEM)
y = {
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
y.pop("model")
print(y)

#popitem(),removes last item:
y.popitem()
print(y)

del y["brand"]
print(y)

#creating copyof given dictionary:
z= dict(y)
print(z)
#we can use copy() method

#dict():
q = dict(brand="ford",model="mustang",year=1964)
print(q)

#update():
x.update(five =5)
print(x)