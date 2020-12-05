#trunc():
#removes the decimal numbers and return float number
import numpy as np
arr  = np.trunc([-3.16666,3.16666,4.9,0.000])
print(arr)
print(arr.dtype)

#fix():
arr  = np.fix([-3.16666,3.16666,4.9,0.000])
print(arr)
print(arr.dtype)
#both trunc(),and fix() behaves same

#floor():
#rounds off to decimal to nearest lower integer
arr = np.floor([-3.1666,3.9667])
print(arr.dtype)

#ceil:
#rounds off to decimal to nearest upper integer
arr  =np.ceil([-3.1666,3.6667])
print(arr)

arr =np.around(3.1666,1)
print(arr)

