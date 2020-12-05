#this a basic example whuch has a function inside there is another example,and inside it finally it returns inner_func
"""
def outer_func():
    message = "HI"

    def inner_func():
        print(message)

    return inner_func()

outer_func()                  """

"""
def outer_func():
    message = "HI"

    def inner_func():
        print(message)

    return inner_func

my_func = outer_func()
print(my_func)                   #here what it returns is function,now my_func is not variable ,it is a function
print(my_func.__name__)           #and it's name is inner_func

#-----------------------------------------------------
#if we now call the fucntion i.e my_func it will return the inner_func
#so,call to outer_func() assigns my_func as a function
#a closure is a inner function that remembers and has accesss to variabels outside of scope even the outer function has executed  """


#with parameters:
def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func

hi_func = outer_func("Hi")
hello_func = outer_func("Hello")

hi_func()
hello_func()