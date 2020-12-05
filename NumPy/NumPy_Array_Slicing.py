import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:4])
print(arr[-4:])
print(arr[:-4])
print(arr[2])

#step:
print(arr[1:5:2])
print(arr[::2])

#negative steping indicates it should start from back:
print(arr[::-1])
print(arr[::-2])

#2-D Arrays:
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2[1,1:4])

#from both elements :
print(arr2[0:2,2])