#Random numbers generated through a generation algorithm are called pseudo random.
#Yes. In order to generate a truly random number on our computers we need to get the random data from some outside source. This outside source is generally our keystrokes, mouse movements, data on network etc.
#to work with random we need to import random module from numpy
import numpy as np
from numpy import random
x = random.randint(100)       #randint() will generate integers
print(x)

#rand() method returns float between  0 and 1
x = random.rand()
print(x)

#creating random arrays:
#integers arrays
#1-D:
x = random.randint(100,size=(5))    #first parameter refers to number from 1-100,size refers to shape of array
print(x)

#2-D:
x = random.randint(100,size=(3,5))
print(x)

#1-D with rand():
y = random.rand(5)        #the parameter refers to elements in array
print(y)

#2-D with rand():
y  = random.rand(3,5)
print(y)

#generate random  numbers from an array:
#choice() is used to do that so:
#the array must be one-dimensional
arr = np.array([3,5,7,9])
x = random.choice(arr)
y = random.choice([1,4,7,8])
print(x)
print(y)

#it also returns an array with size parameter
z = random.choice([3,5,7,9],size=(3,5))
print(z)