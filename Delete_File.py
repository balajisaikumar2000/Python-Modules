#inorder to remove file we have to import the os
import os
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else:
    print("The file does not exist")

#to delete the folder(empty folders only):
os.rmdir("myfolder")