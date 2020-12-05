#use of generators over normal  function is they do not consume memory
#Use yield instead of return when the data size is large
#Yield is the best choice when you need your execution to be faster on large data sets
#Use yield when you want to return a big set of values to the calling function
#Yield is an efficient way of producing data that is big or infinite
#yield returns a generator to the caller and the executioon of the code starts only when the generator is iterated

#this gives generator object:
def testyield():
    yield "Welcome to my World"
output = testyield()
print(output)

#this will print out the message:
#to print the message we have to iterate the generator object
def testyield():
    yield "Welcome to my World"
output = testyield()
for i in output:
    print(i)


#creating generator function:
def any_thing():
    yield "H"
    yield "E"
    yield "L"
    yield "L"
    yield "O"
test = any_thing()
for i in test:     #this will return all values
    print(i)
print(test)        #if we mention return there it will only return single value

#difference:
# Normal function
def normal_test():
    return "Hello World"
# Generator function
def generator_test():
    yield "Hello World"

print(normal_test())  # call to normal function
#alternatives to print generator  function
print(generator_test())  # call to generator function
for i in generator_test():
    print(i)
print(next(generator_test()))
print(list(generator_test()))     #it will print results in list


#normal function:
def even_numbers(n):
    for x in range(n):
       if (x%2==0):
           return  x
num = even_numbers(10)
print(num)

#what we observed is the function call only return first value because it came across a return  keyword

#generetor function:
def even_numbers(n):
    for x in range(n):
       if (x%2==0):
           yield x
num = even_numbers(10)
for i in num:
    print(i)
#here the all values are iterated

