#shape of the array is the number of elements in dimension:
#by reshaping we can add or remove dimensions or change number of elements in each dimension
import numpy as np
#1-D-----2-D:
arr1 =np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr =arr1.reshape(4,3)
print(newarr)
print(arr1)

#1-D---------3-D:
arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr =arr1.reshape(2,3,2)
print(newarr)

#error:
arr2 = np.array([1,2,3,4,5,6,7,8,9])
newarr = arr2.reshape(3,3)
print(newarr)
print(newarr.base)   #it is view so it's returns original array instead of None

#unknown dimension:
arr3 = np.array([1,2,3,4,5,6,7,8])
newarr = arr3.reshape(-1,2,2)           #here we can use any negatiive number it works,but we cannot pass more than two neagtive signs
print(newarr)                        #we can pass negative position number anyware

#Flattening the arrays:
#converting multidimensional array into 1-D array:
arr = np.array([[1,2,3],[4,5,6]])
newarr   = arr.reshape(-1)    #here  also we can use any number
print(newarr)