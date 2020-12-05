#like in javascript try_catch_finally which are used for exception handling
#python also have try_except_finally which are useful for exception handling
try:
    print("Hello")
#except NameError:
#   print("variable is not defined")
except:
    print("something else went wrong")
#else:
#    print("Nothing went wrong")
finally:
    print("try_except is finished")

#raise:
#x = -1
#if x < 0:
#    raise Exception("Sorry, no numbers below zero")
#---------
x  = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")
