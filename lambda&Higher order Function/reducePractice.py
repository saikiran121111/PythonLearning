################################### Reduce Practice ######################################################
from functools import reduce

#1
list1 = [1, 2, 3, 4, 5]

sum = reduce(lambda acc,num : acc+num,list1)

print(sum)

#2
list2 = [1, 2, 3, 4, 5]

multiply = reduce(lambda acc,num : acc * num, list2)

print(multiply)

#3
list3 = [3, 7, 2, 9, 4]

def max_num(acc,num):
    if acc > num:
        return acc
    else :
        return num

maxx = reduce(max_num, list3)
print(maxx)

#4
list4 = [3, 7, 2, 9, 4]

def min_num(acc,num):

    if acc < num:
        return acc
    else:
        return num

mini = reduce(min_num,list4)

print(mini)

#5
list5 = ["Python", "is", "awesome"]

join_string = reduce(lambda acc,string : acc + ' ' + string,list5)
print(join_string)

#6
list5 = ["a", "b", "c", "d"]

concate_string = reduce(lambda acc,char : acc+char,list5)

print(concate_string)

#6
list6 = [1, 2, 3, 4, 5]

filtered_list = filter(lambda x : x % 2 == 0, list6)

largest_even = reduce(lambda acc, num : acc if acc > num else num , list(filtered_list))

print(largest_even)

#7

list7 = ["visakhapatnam", "hyderabad", "delhi"]

def long_name(acc,name):

    if len(acc) > len(name):
        return acc
    else :
        return name

longest_name = reduce(long_name,list7)

print(longest_name)