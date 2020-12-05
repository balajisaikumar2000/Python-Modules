nums = [1,2,3,4,5,6,7,8,9,10]

#ex-------------:
my_list =[]
for n in nums:
    if n%2 ==0:
        my_list.append(n)
print(my_list)

#with comprehension
my_list =[n for n in nums if n %2 ==0]
print(my_list)

#ex-------------------------
my_list =[]
for letter in "abcd":
    for num in range(4):
        my_list.append((letter,num))
print(my_list)

#with comprehension:
my_list =[(letter,num) for letter in "abcd" for num in range(4)]
print(my_list)

#ex----------------------------:
names = ["Bruce","Clark","Peter","Logan","Wade"]
heros = ["Batman","Superman","Spiderman","Wlovorine","Deadpool"]

my_dict ={}
for name,hero in zip(names,heros):
    my_dict[name] = hero
print(my_dict)

#with comprehension:
my_dict = {name:hero for name,hero in zip(names,heros)}
my_dict2 = {name:hero for name,hero in zip(names,heros) if name != "Peter"}
print(my_dict)
print(my_dict2)

#ex-----------------------------:
nums =[1,2,1,3,4,2,3,5,7,8,9,6,5,7,8,9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

#with comprehension:
my_set = {n for n in nums}
print(my_set)

#generator expressions
nums = [1,2,3,4,5,6,7,8,9,10]
def gen_func(nums):
    for n in  nums:
        yield n*n
my_gen = gen_func(nums)
for i in my_gen:
    print(i)

#with comprehension
my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)