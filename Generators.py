"""
def square_numbers(nums):
    for i in nums:
        yield(i*i)

my_nums = square_numbers([1,2,3,4,5])

#print(next(my_nums))
#print(next(my_nums))
#print(next(my_nums))
#print(next(my_nums))
#print(next(my_nums))

for num in my_nums:
    print(num)              """

"""
my_nums = [x*x for x in [1,2,3,4,5]]

print(my_nums)

for num in my_nums:
    print(num)    """

#to create a generator:
my_nums = (x*x for x in [1,2,3,4,5])
print(my_nums)                            #now this is a generator
print(list(my_nums))                  #we can save generator as a list
#if we want result we have to loop over through

