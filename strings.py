s= """rwgr        #multy line commenting
greg
reg
rg
rg
rtg"""
print(s)

a='''ffsfsd
sdv
dsvsdf
vsdf
vsdf
v s'''
print(len(a))       #length


#x = "hello world"
#print(x[0])

b= "hello world"       #slicing
print(b[1:2])

o ="   balaji sai kumar     "    #striping
print(o.lstrip())

u = "HELLO WORLD"         #upper and lower
print(u.lower())

j = "hello,fellas,what's up"      #split()
m = j.split(" ")
print(m)

n =  "balaji sai kumar"            #replace
print(n.replace("balaji","hello"))

txt ="the rain in spain stays mainly in the plain"      #in and not in
print("balaji" not in txt)
print("t" in txt)

#format() which is used to concat string + int
text = "my name is balajio,and i am {0} and  {1}"
print(text.format(20,34))

#escape character
l = "HEY \"balaji\" i'm  here"
print(l.lower())

met= "ascn  vw v wv wv wr vr wv rwv"
print(met.startswith("a"))

x = "d"
if bool(x) == False:
    print("yes")
else:
    print("No")