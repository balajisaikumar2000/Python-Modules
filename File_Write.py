f = open("demofile2.txt","a")
f.write("\nNow the file has more content!")
f.close()

f = open("demofile2.txt","r")
y = f.read()
print(y)


#overwrite the content:
x  = open("demofile2.txt","w")
x.write("oops..!I have deleted the content!")
f.close()

x =open("demofile2.txt","r")
print(x.read())

#create a file with "x" ,"a","w":
z =open("demo.txt","x")


