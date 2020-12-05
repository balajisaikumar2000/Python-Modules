#to search an array we use where() method,and it returns index it is somewhat similar to find:
#it returns indexes in a tuple which contains array
import numpy as np
arr = np.array([1,2,3,4,5,4,4])
x = np.where(arr == 4)#if we mention a element that is not in array it will give empty
print(x)

#where values are even:
arr1 =np.array([1,2,3,4,5,6,7,8])
x = np.where(arr1%2 == 0)
print(x)

#where the values are odd:
arr2 = np.array([1,2,3,4,5,6,7,8])
y = np.where(arr2%2 ==1)
print(y)

#searchsorted:
arr = np.array([6,7,8,9])
x = np.searchsorted(arr,7)
print(x)

#searchsorted    side="right":
#on using right side the index starts from 1 not 0
arr =np.array([6,7,8,9])
x = np.searchsorted(arr,7,side="right")
print(x)

#multiple values:
#if multilple values include then they will iterate from first element and the index in the array with which it will don't miss the sort order
arr = np.array([1,3,5,7])
x = np.searchsorted(arr,[2,4,6])
print(x)


