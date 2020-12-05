import numpy as np
arr = np.array([1,2,3,4])
print(arr.dtype)

arr1 = np.array(["apple","banana","cherry"])
print(arr1.dtype)

#creating arrays with a defined data type:
arr2  =np.array([1,2,3,4],dtype ="S")
print(arr2)
print(arr2.dtype)

#defining size:
arr2 = np.array([1,2,3,4],dtype ="i4")
print(arr2)
print(arr2.dtype)

#astype():
arr = np.array([1.1,2.1,3.1])
print(arr)
print(arr.dtype)
newarr = arr.astype("i")
print(newarr)
print(newarr.dtype)
   #or
arr = np.array([1.1,2.1,3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

#from integer to boolean:
arr = np.array([1,0,3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)
