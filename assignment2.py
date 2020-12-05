import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.stack((arr1,arr2),axis=0)
print(arr)

arr3 = np.array([[1, 2], [3, 4]])

arr4 = np.array([[5, 6], [7, 8]])

newarr = np.dstack((arr3,arr4))
print(newarr)

arr5 = np.array([41,42,43,44])
print(arr5[arr5 > 42])

