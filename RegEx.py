#RegEx can be used to check if a string contains the specified search pattern.
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$",txt)
if x:
    print("yes")
else:
    print("No")

y = "The rain in spain falls mainly in the plain!"
z = re.findall("aix+",y)
print(z)
if z:
    print("66666")
else:
    print("00000")