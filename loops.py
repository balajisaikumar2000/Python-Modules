#while:
i = 1
while i < 6:
    print(i)
    i += 1

#else:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#for:
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x == "apple":
        break

#range:
for x in range(2,30,3):
    print(x)

#---------------
for x in range(6):
    print(x)
else:
    print("Finally Finished")

#pass
#we can pass(move on) for loop if we do not want to execute
for x in [0,1,2]:
    pass
