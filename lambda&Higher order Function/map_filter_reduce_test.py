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

