import numpy as np
#the sorted is a copy of the original array
arr = np.array([3,2,0,1])
print(np.sort(arr))

#strings:
arr1 = np.array(["banana","cherry","apple"])
print(np.sort(arr1))

#boolean:
arr = np.array([True,False,True])
arr1 = np.array([True,False,True,1])
print(np.sort(arr1))
print(np.sort(arr))

#2-D:
arr2 =np.array([[3,2,4],[5,0,1]])
print(np.sort(arr2))

#3-D:
arr3 =np.array([[[1, 3, 2], [5, 4, 6]], [[7, 8, 9], [10, 11, 12]]])
print(np.sort(arr3))