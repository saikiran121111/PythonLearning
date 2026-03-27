
squared = lambda num: num * num

print(squared(2))


addTwo = lambda num1, num2: num1 + num2 # using lambda two params

print(addTwo(4, 9)) # value input for respected variables


def funcBuilder(x):
    return lambda num: num + x

add10 = funcBuilder(10) # creating a new func and calling at bottom for num value assignment
add20 = funcBuilder(2)

print(add10(5))
print(add20(5))


##############################################################################################

#lambda a: a * a

listnum = (2,3,4,5,6)

var = map(lambda num : num * num, listnum) # map is function that receives function as argument and list as values
#it goes through all the list separately and do the necessary

print(list(var))

##############################################################################################

lambda num: num%2 != 0

odd_numbers = filter(lambda num : num % 2 != 0, listnum) # filters only the true condition values and gives the response
# This condition basically gives true or false map prints true or false but filter prints true values
print(tuple(odd_numbers))

#############################################################################################


from functools import reduce

#reduce accepts two parameters one is accumulator and 2nd is current



names = ['sai','kiran','ruku']

char_count = reduce(lambda acc,num : acc + len(num),names,0)

print(char_count)