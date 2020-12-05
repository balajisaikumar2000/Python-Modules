import numpy as np
arr1 = np.array([1,2,3,4])
print(arr1[3])

#accessing 2-D arrays:
arr2 =np.array([[1,2,3,4],[6,7,8,9]])
print(arr2)
print("2nd element on 1st dim:",arr2[0,1])

#accessing 3-D arrays:
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3[0,1,2])

#negative indexing:
arr2 =np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("Last element from 2nd dim: ",arr2[1,-1])