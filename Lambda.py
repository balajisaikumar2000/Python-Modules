#lambda function is small anonymous function.
x = lambda a : a + 10
print(x(5))

#------------------
x = lambda a,b,c : a + b + c
print(x(5,10,15))

#---------------
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))