#a class is like an object constructor,or a "blueprint" for creating objects
#the below is an blueprint for object-constructor
class Myclass:
    x =5
print(Myclass)
#p1 is object
p1 = Myclass()
print(p1.x)

#__init__():
class Person:
    def __init__(self,name,age):
        self.name  = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John",36)

print(p1.name)
#p1.age =20
#del p1.age
#del p1
#we can pass  classes
print(p1.age)
p1.myfunc()