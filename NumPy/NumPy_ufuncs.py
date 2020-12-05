#ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements
#vectorization is Converting iterative statements into a vector based operation is called vectorization.
import numpy as np

#without function:
x = [1,2,3,4]
y = [4,5,6,7]
z =[]
for i,j in  zip(x,y):
    z.append(i+j)
print(z)

#NUMPY'S has a ufun for this,called add(x,y):
#add():
x =[1,2,3,4]
y =[4,5,6,7]
z = np.add(x,y)
print(z)