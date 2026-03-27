from functools import reduce

# Warmed UP
#1

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_filter = filter(lambda x : x%2==0,list1)

total = reduce(lambda acc,num : acc + num,list(even_filter))

print(total)

#2

list2 = ["apple", "banana", "kiwi", "fig", "mango"]

filter_char = filter( lambda x : len(x) > 4,list2)

convo_to_upper = map(lambda x : x.upper(),list(filter_char))

print(list(convo_to_upper))

#3

list3 = [10, 15, 20, 25, 30]

filter_div = filter(lambda x : x%10 == 0,list3)

multiply_list = reduce(lambda acc,num : acc*num,list(filter_div))

print(multiply_list)

#Getting Warmer
#4

list4 = [" alice ", "", " bob ", " ", "charlie", "dave"]

def cap_list(x):
    x = x.strip()
    x = x.title()
    return x

map_list = map(cap_list,list4)

filter_list = filter(lambda x : len(x) > 0,list(map_list))

joined_string = ", ".join(list(filter_list))

print(joined_string)

#5

list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_odd = filter(lambda x : x%2 != 0,list5)

squared_list = map(lambda x : x**2,list(filtered_odd))

print(list(squared_list))

#6

list6 = ["hello", "world", "python", "is", "great"]

longest_word = reduce(lambda acc,word : acc if len(acc)>len(word) else word,list6)

print(longest_word)

#7

list7 = [100, 200, 300, 400, 500]

filter_prices = filter(lambda x : x> 200,list7)

inr_conversion = map(lambda x : x * 86,list(filter_prices))

print(list(inr_conversion))

#Now it burns

#8

list8 = ["visakhapatnam", "hyderabad", "delhi", "bangalore", "mumbai"]

filtered_list = filter(lambda x : len(x) > 6 ,list8)

def revers_str(x):
    x = x[::-1]
    x = x.title()
    return x
map_list = map(revers_str,list(filtered_list))

print(" | ".join(list(map_list)))

#9

list9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_filtering = filter(lambda x : x%2 != 0,list9)

squares = map(lambda x : x**2,list(odd_filtering))

total = reduce(lambda acc,num : acc + num , list(squares))

print(total)

#10
list10 = ["the cat", "the dog", "a fish", "the bird", "a cow"]

filtered_string = filter(lambda x : 'the' in x,list10)

def remove_the_text(x):
    x = x.split()[1]
    x = x.title()
    return x

remove_the = map(remove_the_text,list(filtered_string))

print(list(remove_the))

#11
list11 = [3, 7, 1, 9, 2, 8, 4, 6, 5]

max_num = reduce(lambda acc,num : acc if acc > num else num , list11)

filter_max = filter(lambda x : x != max_num,list11)

max_second_num = reduce(lambda acc,num : acc if acc > num else num , list(filter_max))

print(max_second_num)

#12

list12 = ["name:alice", "age:30", "city:visakhapatnam", "job:developer"]

def caps_convert(x):

    x = x.split(':')
    x[0:2] = x[0].title(), x[1].title()
    x = ': '.join(x)
    return x

map_list = map(caps_convert,list12)

print(" | ".join(list(map_list)))

#13

list13 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filter_list = filter(lambda x : x%3 == 0 or  x > 8 ,list13)

multiplying_list = reduce(lambda acc,num : acc * num , list(filter_list))

print(multiplying_list)

#14

list14 = [" Hello ", " wORLD ", "", " pYtHoN ", " ", " iS ", " AWESOME "]

def clear_text(x):

    x = x.strip()
    x = x.lower()
    return x

clear_list = map(clear_text,list14)

filter_list = filter(lambda x : len(x)>0,list(clear_list))

finalStr = " ".join(list(filter_list))

finalStr = finalStr.capitalize()

print(finalStr)

#Boss Fight
#15

students = [
    "alice:85", "bob:42", "charlie:91",
    "dave:55", "eve:78", "frank:38"
]

def students_pass(x):

    x = x.split(':')
    if int(x[1]) > 50:
        x = x[0].title()
        return x
    else:
        return ''

map_list = map(students_pass,students)

filter_list = filter(lambda x : len(x)> 0 ,list(map_list))

passed_students = reduce(lambda acc,stud : acc+', '+stud,list(filter_list))

print(f'Passed students: {passed_students}')


#16

list15 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_list = filter(lambda x : x%2==0 or x%3==0,list15)

squared_list = map(lambda x : x**2 , list(filtered_list))

total = reduce(lambda acc,num : acc+num,squared_list)

print(total)