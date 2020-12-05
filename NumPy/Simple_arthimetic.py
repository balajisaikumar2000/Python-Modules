import numpy as np
#add():
arr1 = np.array([10,11,12,13,14,15])
arr2  =np.array([20,21,22,23,24,25])

newarr =np.add(arr1,arr2)

print(arr1+arr2)
#or
print(newarr)

#subtract:
arr1 = np.array([10,11,12,13,14,15])
arr2  =np.array([20,21,22,23,24,25])
newarr = np.subtract(arr1,arr2)   #the second parameter is removed from first parameter
print(newarr)

#multiply:
arr1 = np.array([10,11,12,13,14,15])
arr2  =np.array([20,21,22,23,24,25])

newarr = np.multiply(arr1,arr2)
print(newarr)

#divide():
arr1 = np.array([10,11,12,13,14,15])
arr2  =np.array([20,21,22,23,24,25])
newarr = np.divide(arr1,arr2)
print(newarr)

#power:
arr1 = np.array([10,20,30,40,50,60])
arr2  =np.array([3,5,6,8,2,33])

newarr = np.power(arr1,arr2)
print(newarr)

#remainder:
#mod(),remainder():
arr1 = np.array([10,20,30,40,50,60])
arr2  =np.array([3,5,6,8,2,33])

newarr = np.mod(arr1,arr2)
print(newarr)
#we can use remainder() instead of mod()

#quotient and mod:
#divmod() returns teo arrays ,first contains quotient ,and second contains the mod
arr1 =np.array([10,20,30,40,50,60])
arr2 = np.array([3,7,9,8,2,33])
print(np.divmod(arr1,arr2))

#absolute():
arr = np.array([-1,-2,1,2,3,-4])
newarr =np.absolute(arr)
print(np.absolute([-1,-2,1,2,3,-4]))