set1 = {1,2,3,4}
set2 = {5,6,7,8}

set3 = set1.copy()
#Adding elements from one set to another
#Can use update with list,tuples,dictionaries too
set3.update(set2)

print(set1)
print(set2)
print(set3)
print(type(set1))
print(len(set2))

#In sets No duplicates are allowed
dupset = {1,2,2,3,4,4}
dupset2 = {3,4,5,6,6,7}

print(dupset) # -> {1,2,3,4}

#Remember 1 is dupe of true and 0 is dupe of false
boolset = {1,True,0,False}
print(boolset) #-> if no 1 and 0 we print true and false if they exist we print {0,1}

#check if value is available in set
print(1 in set1) # -> True
#We can't refer index in set cause it doesn't have one
#adding new element
set2.add(9)
print(set2)

#Merge two sets
newset = set1.union(set2)
print(newset) #->{1,2,3,4,5,6,7,8,9}

#intersection show the common

newset2 = dupset.intersection(dupset2)
print(newset2) #-> shows the common only {3,4}

#Show only non duplicates values
newset3 = dupset.symmetric_difference(dupset2)
print(newset3) # -> {1, 2, 5, 6, 7} show only non common values

#difference is used to show the values that are not available in other set

newset4 = dupset.difference(dupset2)

print(newset4) #->{1,2}