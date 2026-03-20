#Tuples are restricted files can't sort can't change the value etc like list
#But they can be changed by casting it to list adding whatever or modify you want
#and convert that into tuple again they basically like readonly arrays

mytuple = tuple((1,2,3,4,5,6))

mylist = list(mytuple)

mylist.insert(3,"Hey")

newTuple = tuple(mylist)
print(newTuple)