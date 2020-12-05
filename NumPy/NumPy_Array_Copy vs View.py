import numpy as np
#copy():
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

#view():
#ex1:
arr1 = np.array([1,2,3,4,5])
x = arr1.view()
arr[0] = 42

print(arr)
print(x)

#ex2:
arr2 = np.array([1,2,3,4,5])
x = arr2.view()
x[0] = 31

print(arr2)
print(x)

#base attribute:
#the one which owns data returns None ,otherwise base attribute refers to the original object
arr3 = np.array([1,2,3,4,5])
x = arr3.copy()
y = arr3.view()

print(x.base)          #returns None
print(y.base)          #returns original array

