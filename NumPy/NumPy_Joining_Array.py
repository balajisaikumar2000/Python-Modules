#for more clear explanation of numpy axes check this site"https://www.sharpsightlabs.com/blog/numpy-axes-explained/"
import numpy as np


#1-D:
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.concatenate((arr1,arr2))
print(arr)

#2-D:
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
print(arr1)
print(arr2)
arr = np.concatenate((arr1,arr2),axis=1)
print(arr)

#stack():
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.stack((arr1,arr2),axis=0)
print(arr)


#along rows------hstack():
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
arr = np.hstack((arr1,arr2))
print(arr)

#along columns------vstack():
#arr1 = np.array([1,2,3])
#arr2 = np.array([4,5,6])
#arr = np.vstack((arr1,arr2))
#print(arr)

#along height-------dstack:
#arr1 = np.array([1,2,3])
#arr2 = np.array([4,5,6])
#arr = np.dstack((arr1,arr2))
#print(arr)