#assert keyword:
x = "hello"
assert x == "hello","x should be 'hello'"

#join():
mytuple = ("john")
mytuple2 = ("John","Peter","Vicky")
x = "#".join(mytuple)         #the first one should be a string and join contains iterable string elements
print(x)
print("2".join(("john","peter","vicky")))

myDict = {"name":"John","country":"Norway"}   #it will only join keys
mySeperator = "Test"
x = mySeperator.join(myDict)
print(x)

#slice():
a = ("a","b","c","d","e","f","g","h")
x = slice(2)
print(a[x])

#zip():
listA = [1,2,3,4]
listB = ["a","b","c","d"]
z1  = zip(listA,listB)
print(z1)     #returns zip object
z1 = list(z1)
print(z1)

#when using tuples:
lst1 = (1,2,3,4)
lst2 = ("a","b","c","d")
lst = zip(lst1,lst2)
print(tuple(lst))

letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters,numbers):
     print('Letter:',l)
     print('Number:',n)