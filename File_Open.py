f = open("demofile.txt","r")
print(f.read())
#print(f.read(5))-------Hello
#readline():
print(f.readline())
print(f.readline())

#looping line by line:
for x in f:
    print(x)
f.close()
#print(f.read())   now this will raise an exception
