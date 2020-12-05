#functional scope:
def myfun():
    x = 300
    print(x)
myfun()
#this is not possible print(x)

#global scope:
x = 300
def fun2():
    print(x)
fun2()

#global keyword:
def fun3():
    global x
    x =300
fun3()
print(x)