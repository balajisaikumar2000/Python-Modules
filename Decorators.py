#see the closures class before coming to this
#simply a decorator is a function which takes a function as parameter and add's some functionality and returns another fucntion all of these which changing the source code of  function that we passed in
#Decorators

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args,**kwargs)
    return wrapper_function













#@decorator_function(below symbol) is similar to decorated_display = decorator_function(display)
@decorator_function
def display():
    print("display function ran")
display()                               #we have to give this file name only

"""
decorated_display = decorator_function(display)
decorated_display()      """

@decorator_function
def display_info(name,age):
    print("display_info ran with arguments({} ,{})".format(name,age))

display_info("John",25)
