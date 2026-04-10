# #1 Basic
# #swap two numbers without using third variable
#
# a = 10
# b = 20
#
#
# a = a+b
# b = a-b
# a = a-b
#
# print(a,b)
#
# #2 Basic
# #even or odd
# def evenrodd():
#     try:
#         userinput = int(input('Enter a number:'))
#         if userinput % 2 == 0:
#             print('even')
#         else :
#             print('odd')
#     except ValueError:
#         print('This is not a valid Input')
#
# evenrodd()
from functools import reduce
from unittest import expectedFailure


# #3 Basic
# #Captialize every word that is longer than 3 characters
#
# sentence = 'the quick brown fox jumps over the lazy dog'
#
# list1 = sentence.split()
#
# capitalize = map(lambda x : x.capitalize() if len(x) > 3 else x, list1)
#
# print(' '.join(list(capitalize)))

# #4 Basic
# #Print each piece on a new line with label
#
# data = 'Sai:21:Hyderabad:Developer'
# list1 = data.split(':')
# list2 = ['Name','Age','City','Role']
#
# for i,j in zip(list2,list1):
#     print(i+ ': '+j)
#
# #5 Basic
# #students who passed > = 50
# students = [("Sai", 85), ("Ravi", 42), ("Priya", 91), ("Arjun", 55), ("Meena", 38)]
#
# passedStudents = filter(lambda x : x[1] >= 50, students)
#
# studentNames = map(lambda x : x[0],passedStudents)
# print(', '.join(list(studentNames)))

# #6 Basic
# #Print only items that are in stock (quantity > 0) in format "apples: 50 units".
#
# inventory = {"apples": 50, "bananas": 0, "grapes": 30, "mangoes": 0, "oranges": 15}
#
# fruitsAvailable = filter(lambda x : inventory[x]>0,inventory)
#
# for i in list(fruitsAvailable):
#     print(f'{i}: {inventory[i]} units')


# #7 Medium
# # *
# # **
# # ***
# # ****
# # *****  <-- print this pattern
# # ****
# # ***
# # **
# # *
#
# for i in range(1,6):
#     for j in range(i):
#         print('*', end="")
#     print()
# for i in range(1,6):
#     for j in range(5-i):
#         print('*', end="")
#     print()

# #8 Medium
# # find the top 3 largest numbers using loops only.
# list1 = [4, 7, 2, 9, 1, 5, 8, 3, 6, 10]
# list2 = []
#
# largest = 0
# for i in list1:
#     if i > largest:
#         largest = i
# list2.append(largest)
# list1.remove(largest)
#
# largest = 0
# for i in list1:
#     if i > largest:
#         largest = i
# list2.append(largest)
# list1.remove(largest)
#
# largest = 0
# for i in list1:
#     if i > largest:
#         largest = i
# list2.append(largest)
# list1.remove(largest)
#
# print(list2)

# #9 Medium
# # Write a function is_palindrome(word) that returns True if the word reads the same forwards and backwards. Test with "racecar", "hello", "madam".
# def is_palindrome(word):
#
#     if word == word[::-1]:
#         print('It is palindrome')
#     else:
#         print('Not a palindrome')
#
# is_palindrome('madam')
#
# #10 Medium
# # counting vowels
#
# def count_vowels(sentence):
#     vowels = ['a','e','i','o','u']
#     count = 0
#     for i in sentence.lower():
#         if i in vowels:
#             count += 1
#
#     print(count)
#
# count_vowels('Hyderabad is a great city')
#
# #11 Medium
#
# employees = ["alice:45000", "bob:32000", "charlie:67000", "dave:28000", "eve:55000"]
#
# splitting = map( lambda x : x.split(':'),employees)
#
# filtering = filter(lambda x : int(x[1]) > 40000,list(splitting))
#
# fetching_names = map(lambda x : x[0],list(filtering))
#
# final_string = ', '.join(list(fetching_names))
#
# print(final_string.title())

# #12 Medium
#
# list1 = [3, 6, 2, 8, 1, 9, 4, 7, 5, 10]
#
# divided = filter(lambda x : x%2 == 0 or x%3 == 0,list1)
#
# totalsum = reduce(lambda acc,n : acc+n, list(divided))
#
# print(totalsum)

# #13 Hard
# # Build a library class
# class Library:
#
#     def __init__(self,books):
#         self.books = books
#
#     def add_book(self,title):
#         return self.books.append(title)
#
#     def remove_book(self,title):
#         return self.books.remove(title)
#
#     def show_books(self):
#         if len(self.books) > 0:
#             print(self.books)
#         else:
#             print('No books available')
#
# library1 = Library(['title','summit','praneet'])
#
# library1.add_book('babit')
# library1.remove_book('praneet')
# library1.show_books()


# #14 Inheritance and Polymorphism
#
# class Vehicle:
#     def __init__(self,brand,speed):
#         self.brand = brand
#         self.speed = speed
#
#     def describe(self):
#         pass
#
#
# class Car(Vehicle):
#     def __init__(self,brand,speed,doors):
#         super().__init__(brand,speed)
#         self.doors = doors
#
#     def describe(self):
#         print(f'{self.brand} has {self.speed} speed and {self.doors} doors')
#
#
# class Motorcycle(Vehicle):
#     def __init__(self,brand,speed,sidecar):
#         super().__init__(brand,speed)
#         self.sidecar = sidecar
#
#     def describe(self):
#         print(f'{self.brand} has {self.speed} speed and sidecar is available: {self.sidecar}')
#
# car = Car('suzuki',120,4)
#
# bike = Motorcycle('RoyalEnfield',120,True)
#
# list1 = [car,bike]
#
# for i in list1:
#     i.describe()

# #15 passwordManager class
#
# class PasswordManager:
#     def __init__(self,password):
#
#         self.password = password
#
#     @property
#     def password(self):
#         return '********'
#
#     @password.setter
#     def password(self,password):
#         if len(password) > 7:
#             self.__password = password
#         else:
#             print('Password should be atleast 8 characters')
#
#     def check_password(self,attempt):
#         if attempt == self.__password:
#             return True
#         else:
#             return False
#
#     def change_password(self,old,new):
#         if old == self.__password:
#             if len(new) > 7:
#                 self.__password = new
#                 print('password changed')
#             else:
#                 print('New Password should be atlease 8 characters')
#         else:
#             print('Old Password Incorrect')
#
# pass1 = PasswordManager('Babresed')
#
# print(pass1.check_password('Babresed'))
#
# pass1.change_password('Babresed','Kakressed')
#
# print(pass1.check_password('Babresed'))


