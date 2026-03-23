#While loop
num = 1

# while num <= 10:
#     print(num)
#     # if num ==5 : This will break the loop when num is 5
#     #     break
#     num += 1

# while num <= 10:
#     print(num)
#     num += 1
#     if num == 5:
#         continue  # Continue is used to start the next loop when the condition satisfies


#For loop is used like variable in list,string,tuple etc

#1 using list
mylist = ['apple','banana','mango','strawberry']

for i in mylist:
    print(i)

#2 using string separates individual character in string
for i in 'Achukuchipie':
    print(i)

#3 using condition to print the specific value or character or whatever
for i in mylist :
    if i == 'banana' :
        print(i)

#We can also use range in for loop

for i in range(1,7): # range (1 - starting value , 7 - ending value(n-1) # single value considers as end range
    print(i)

print('Increment')
#Java for (i=1;<=100;i++5) we have increment here but in python
for i in range(5,101,5): # here i starts on 1 max goes up to 100 increment by 5
    print(i) # (start,end,increment)
else:
    print('loop Over')# checks else once the whole loop is done and prints

#Nested For loops
#Lets take list as example to see nested Loops

actions = ['codes','eats','sleeps']
users = ['sai','kiran','ruku']

for i in users:
    for j in actions:
        print(i + ' ' + j + '.')
