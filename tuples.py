#immutable
x = tuple(("apple","banana","cherry"))
y = list(x)
y[0] = "mango"
x = tuple(y)
print(x)

#creating single tuple
a = ("balaji")             #this will cause an error
print(type(a))

b= ("balaji",)       #correct process
print(type(b))

#count():
z = (1,2,4,1,2,6,7,8,4,6)
print(z.count(2))


#index():
m = (1,2,3,6,3,5,6,3,9,6,1)
print(m.index(6))