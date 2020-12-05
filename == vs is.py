#"checks" for equality
#"is" checks for identity

#-------------------------------
#    "==" example

"""
l1 = [1,2,3,4,5]
l2  = [1,2,3,4]

if l1 == l2:
    print(True)
else:
    print(False)     """

l1 = [1,2,3,4,5]
l2  = [1,2,3,4,5]

if l1 == l2:
    print(True)           #cause both are equal
else:
    print(False)

#---------------------------------
l1 = [1,2,3,4,5]
l2  = [1,2,3,4,5]

if l1 is l2:            #cause "is" checks for identity(simple id),may be both l1,l2 are equal in  values they are two different objects with different id's
    print(True)
else:
    print(False)
print(id(l1))    #both are different id's ,so that's why it returns false
print(id(l2))

#----------------------------
l1 = [1,2,3,4,5]
l2  = [1,2,3,4,5]
l1 = l2

if l1 is l2:
    print(True)                  #now both are eaual in identities
else:
    print(False)
print(id(l1))            #both are same id's ,because we equaliuze them at start of the code
print(id(l2))          #so,"is" checks for identity





