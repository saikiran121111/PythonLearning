names = ['sai','kiran','jimi','tommy']

ages = [1,5,73,4,2,6,3,6]

print (len(names))
print(names.index('kiran'))
names.append('sarah')
names.remove('jimi')
#names.extend(ages)
# print(names)
names += ['Jack']
names.insert(3,'Chokie')
names[2:3] = ['Babre','Chopde']
names[0:1] = ['Sunday','Monday']
del names[1]
names.sort() #Used for sorting
print(names)
# del ages
# print(ages)
#ages.clear()
ages.sort()#Ascending order
ages.sort(reverse=True) #descending order
print(ages)
#You can use the constructor aswell to create the list etc