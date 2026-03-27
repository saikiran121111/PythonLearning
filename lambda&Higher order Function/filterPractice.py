############################## Filter Practice ########################################
#1
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


fixed_list = filter(lambda x : x > 5,list1)

print(list(fixed_list))

#2
list2 = [-3, -1, 0, 2, 4, 7]

fixed_list = filter(lambda x : x>0 , list2)

print(list(fixed_list))

#3

list3 = ["apple", "banana", "kiwi", "fig", "watermelon"]

fixed_list = filter(lambda x : len(x)>4 , list3)

print(list(fixed_list))

#4

list4 = ["Alice", "bob", "Charlie", "dave"]

fixed_list = filter(lambda x : x[0].isupper(), list4)

print(list(fixed_list))

#5

list5 = [250, 999, 1500, 3000, 499, 750]

fixed_list = filter(lambda x : x<1000 , list5)

print(list(fixed_list))

#6
list6 = ["", "hello", "", "world", " ", "python"]

fixed_list = filter(lambda x : len(x.strip()) > 0 ,list6)

print(list(fixed_list))

#7
list7 = ["visakhapatnam", "hyderabad", "bangalore", "mumbai", "delhi"]

fixed_list = filter( lambda x : 'a' in x ,list7)

print(list(fixed_list))

#8
list8 = [1, 4, 9, 16, 25, 36]

fixed_list = filter(lambda x : x%2 == 0 and x > 10,list8)

print(list(fixed_list))

#9
list9 = [" alice ", "", " bob ", " ", "charlie"]

def remove_space(x):

    x = x.strip()
    if len(x) > 0:
        return x
    else:
        return None

filter_list = filter(remove_space, list9)

def fixed_list(x):

    x = x.strip()
    x = x.title()
    return x

fixed_list_map = map(fixed_list, list(filter_list))

print(list(fixed_list_map))
