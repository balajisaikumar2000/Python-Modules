#date is a module which is used to get time ,etc..,:
import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.strftime("%A"))

#create dateobject:
y = datetime.datetime(2020,5,17,12,50,40)#year,month,date,hours,mins,sec
print(y)

#strftime:
print(x.strftime("%d"))