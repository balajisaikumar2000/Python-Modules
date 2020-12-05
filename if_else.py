a = 200
b = 33
if b > a:
    print("b is graeter than a")
else:
    print("b is not greater than a")

#short hand:
x = 2
y = 30
print("yes") if x > y else print("no")  #ternary operator in python

#and:
m = 200
n = 33
o = 500
if m > n and o > m:
    print("both conditions are true")

#or:
p = 200
q = 33
r = 50
if p > q or r > p:
    print("atleast one is enough")

d = 4

if d > 10:
  print("Above ten,")
  if d > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#pass is used to assign no values in if statement:
a =33
b =200
if b >a :
    pass



