#iterating means going through  elements one by one:
import numpy as np
#1-D:
arr1 = np.array([1,2,3])
for x in arr1:
    print(x)

#2-D:
arr2 = np.array([[1,2,3,],[4,5,6]])
for x in arr2:
    for y in x:
        print(y)

#3-D:
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr3:
    for y in  x:
        for z in y:
            print(z)

#nditer():
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for x in np.nditer(arr):
    print(x)

#changing data type:
arr = np.array([1,2,3])
for x in np.nditer(arr,flags=["buffered"],op_dtypes=["S"]):
    print(x)


#ndenumerate():
#when we require corresponding index of the element while iterating ,the ndenumerate method can be used for those usecases:
#1-D:
arr1 = np.array([1,2,3])
for i,x in np.ndenumerate(arr):
    print(i,x)

#2-D:
arr2 = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
for idx,x in np.ndenumerate(arr2):
    print(idx,x)

