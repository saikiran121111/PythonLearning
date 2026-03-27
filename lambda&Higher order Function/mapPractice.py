from shlex import join

numbers = [1, 3, 5, 7, 9]

def double_it(x):
    return x * 2

double = map(double_it,numbers)

print(tuple(double))


double_lambda = map(lambda c: c * 2 , numbers)
print(list(double_lambda))


# Practice of Map

#1
list_to_be_squared = [1,2,3,4,5]

def square_the_list(x):
    return x * x

squared_list = map(square_the_list,list_to_be_squared)

print(list(squared_list))


#2

list_to_be_subtracted = [10,20,30]

sub_list = map(lambda x: x - 5, list_to_be_subtracted)

print(list(sub_list))

#3

list_to_be_titlecased = ["hello","world","python"]

title_cased = map(lambda x : x.title(),list_to_be_titlecased)
print(list(title_cased))

#4

list_to_be_removed_spaces = [' apple ',' banana ',' grape ']

removed_spaces = map(lambda x : x.strip(),list_to_be_removed_spaces)
print(list(removed_spaces))

#5

string_list = ['1','2','3','4']

convert_int = map(lambda x : int(x),string_list)
print(list(convert_int))

#6

usd = [100,200,300]

inr = map(lambda x : x*86 , usd)
print(list(inr))

#7
cities = ["visakhapatnam", "hyderabad", "bangalore"]

reversed_cities = map(lambda x : x[::-1], cities)

print(list(reversed_cities))

#8
animals = ["dog", "cat", "fish"]

length_animals = map(lambda x : len(x), animals)

print(list(length_animals))


############### String Manipulations ########################
#split() vs split(' ') try empty split if you are stuck

#1

string1 = 'MY NAME IS RAVI'

correct_string = map(lambda x : x.title(),string1.split())

fixed_list = list(correct_string)

fixed_list[1:3] = [fixed_list[1].lower(),fixed_list[2].lower()]

print(join(fixed_list))

#2

string2 = " python java rust "

fixed_list = map(lambda x : x,string2.split())

print(" ".join(list(fixed_list)))

#3

string3 = 'i love coding in python'

fixed_list = map(lambda x : x.title(),string3.split())

print(" ".join(fixed_list))

#4

string4 = 'hello world foo bar'

fixed_list = map(lambda x : x[::-1] , string4.split())

print(" ".join(fixed_list))


#5

string5 = "name:alice age:25 city:hyderabad"

fixed_list = map(lambda x : x.split(':')[1], string5.split())

print(list(fixed_list))

#6

string6 = "the dog ate the cat and the rat"

def remove_the(x):

    if x == 'the':
        x = ""
    return x

fixed_list = map(remove_the,string6.split())

print(list(fixed_list))

#7
string7 = " hELLo wORLd pYtHoN "

fixed_list = map(lambda x : x.title(),string7.split())

print(" ".join(fixed_list))

