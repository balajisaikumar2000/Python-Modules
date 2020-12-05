price = 50
txt = "The price is {} dollars"
print(txt.format(price))
#----------------------------
price = 50
txt = "The price is {:.2f} dollars"
print(txt.format(price))
#more values:
quantity  = 3
itemno = 567
price =49
myorder= "I want {} pieces of item number {} for {:.2f} dollars."
#we can mention indexes "I want {0} pieces of item number {1} for {2:.2f} dollars
print(myorder.format(quantity,itemno,price))

#--------------
age = 20
name = "balaji"
text = "His name is {1}.{1} is {0} years old"
print(text.format(age,name))