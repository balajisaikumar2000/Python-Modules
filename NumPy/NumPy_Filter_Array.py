#getting some elements out of an existing array and creating a new array out of them is called filtering
import numpy as np
arr = np.array([41,42,43,44])
x = [True,False,True,False]
newarr = arr[x]
print(newarr)

#creating array based on conditions:
arr1 = np.array([41,42,43,44])
filter_arr = []
for element in arr1:
    if element >  42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr1[filter_arr]
print(newarr)

#creating array with only even elements:
arr2 =np.array([1,2,3,4,5,6,7])
filter_arr = []
for element in arr2:
    if element%2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr  = arr2[filter_arr]
print(newarr)

#easy way to tackle above problem:
arr3 = np.array([41,42,43,44])
filter_arr = arr3 > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


#-----------------------------
arr4 = np.array([1,2,3,4,5,6,7])
filter_arr = arr4 % 2 ==0
newarr = arr4[filter_arr]
print(filter_arr)
print(newarr)