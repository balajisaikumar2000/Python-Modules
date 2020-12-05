#sets are unordered and unindexed and immutable:
#every time we run  a code the result will be different in output
#sets never allow duplicates ,even if we have two same items it will show only one
x = {"apple","banana","cherry","cherry"}
print(x)
print("banana" in x)

#add():
y = {"apple","banana","cherry"}
y.add("mango")
print(y)

#update():
z = {"apple","banana","cherry"}
z.update(["mango","grapes"])
print(z)

#to remove an item in  sets we have only two methods:
m = {"apple","banana","cherry"}
m.remove("apple")
print(m)

#discard():
n = {"apple","banana","cherry"}
n.discard("cherry")
print(n)

#n.clear() will clear set with remains empty set
#del x will delete set permanently

#update():
set1= {"a","b","c"}
set2 = {1,2,3}
set1.update(set2)
print(set1)

#union():
set3= {"a","b","c","c"}
set4 = {1,2,3}
set5 = set3.union(set4)
print(set5)

#intersection():  gives common to each set
print(set3 & set5)
#or we can use below method
set4 = {"a"}
print(set3.intersection(set5))
print(set3.intersection(set5,set4))
#if there is no common values we wil get empty set -----(set())

#difference:
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1.difference(s2)       #the result will have elements that are in s1 but not in s2
s4 = s3.difference(s1,s2)
print(s3)
print(s4)


#symmetric_difference:
s3 = s2.symmetric_difference(s1)          #will give the values other than common values in them
print(s3)



