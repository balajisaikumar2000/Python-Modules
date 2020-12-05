import numpy as np
#splitting means opppsoite of joining,,we split one array into multiple
#1-D:
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,3)   #if the input value exceeds the elements it will give empty array
newarr1 = np.array_split(arr,3)
newarr2= np.array_split(arr,10)
newarr3 = np.array_split(arr,5)
#newarr4 = np.array_split(arr,-3)
print(newarr)

#accessing result arrays is like as normal:
print(newarr[0])
print(newarr3[4])
print(newarr[0][1])

#2-D:
#all the arrays that were splitted will have 2-D arrays
arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
newarr = np.array_split(arr,2)
newarr1 = np.array_split(arr,4)
newarr2 = np.array_split(arr,5)
newarr3 = np.array_split(arr,50)     #if we include the number more than elements it's min  array will have atleast 2 elements
newarr4 = np.array_split(arr,25)

print(newarr2)

#using axis=1:
arr =np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
newarr = np.array_split(arr,3,axis=0)
print(newarr)

#split():
arr =  np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
newarr = np.hsplit(arr,3)
print(newarr)


