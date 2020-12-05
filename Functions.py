#functions are defined using "def" keyword
# args
def my_function(fname,lname):
    print(fname + " " +  lname)
my_function("balaji",'sai kumar')

# *args:
def my_function(*kids):
    print("The youngest child is " + kids[0])
my_function("emil","tobias","linus")

# kwargs:
def my_function(child3,child2,child1):
    print("The youngest child is " + child2)
my_function(child1 ="Emil",child2 = "Tobias",child3 = "Linus")

# **kwargs
def my_function(**kid):
    print("The youngest child is " + kid["child1"])
my_function(child1 ="Emil",child2 = "Tobias",child3 = "Linus")

#default parameter:
def my_function(country = "Norway"):
    print("I am from " + country)
my_function("India")

#return statement:
def my_function(x):
    return (5 * x)
print(my_function(3))

