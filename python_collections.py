list1= ['apple',"banana","cherry"]
some = list1[1:3]
print(some)

list2 = ["apple","banana","cherry"]
if  "a" in list2:
    print("yes")

#append():
list3 = ["apple","banana","cherry"]
list3.append("mango")
print(list3)

#insert():
list4 = ["apple","banana","cherry"]
list4.insert(2,"mango")
print(list4)

#remove():
list5 = ["apple","banana","cherry"]
list5.remove("banana")
print(list5)

#pop():
list6 = ["apple","banana","cherry"]
list6.pop(0)
print(list6)

#del:
list7 = ["apple","banana","cherry"]
del list7[0]
print(list7)

list8 = ["apple","banana","cherry"]
list9 = list8
print(list9)
list8.append("mango")
print(list8,list9)

#copy:
list10 = ["apple","banana","cherry"]
list11 = list10.copy()
print(list11)

#extend():
list12 = ["a","b","c"]
list13 = [1,2,3]
list13.extend(list12)
print(list13)
list13.reverse()
print(list13)














