import numpy as np
arr = np.array([1,2,3,4,5])   #array() is method which is used to create ndarray object
print(arr)

#type:
print(type(arr))

#creating array using tuple:
arr = np.array((1,2,3,4,5))
print(arr)
print(type(arr))

#0-D:
arr0 = np.array(42)
print(arr0)

#1-D:
#each element in 1-D is a 0-D array
arr1 =np.array([1,2,3,4,5])
print(arr1)

#2-D:
#the array which contains 1-D arrays
#these are used to represent matrices or 2nd order tensors
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

#3-D:
#an array that has 2-D arrays(matrices) as its elements is called 3-D array
arr3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr3)

#checing how many dimensions:
print(arr0.ndim)          #ndim is a attribute
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

#ndmin():
arr_mul = np.array((1,2,3,4),ndmin=5)
print(arr_mul)
print(arr_mul.ndim)
