line01 = '**************'
line02 = '*            *'
line03 = '*Hello World!*'

print('')
print(line01)
print(line02)
print(line03)
print(line02)
print(line01)

x = y = z = 'Hello Babai' # can assign same value to multiple variables
a,b,c = 'Hi', 2 , 'Hello' # Can assign values separated with commas for independent variables
print(a,b,c)
print(x , y , z)

fruits = ['apple', 'banana', 'cherry']

i,j,k = fruits # Same can be dome for list aswell
print(i,j,k)

#Python's print() function uses a default separator sep=' '
# (a space) between multiple arguments, so the comma that separates
# the arguments in code becomes a space in the output —
# you can change this behavior with print('Hello', 'World', sep='')
# to remove the space or use any custom separator

print('Hello','World') # ignored comma and added space in between

x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)

#Here we defined the function but the x is replaced inside function only outside
#it still takes global value

#inside function if we need to assign a variable to global
#we use
#global x

x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)

#For this as we declared the x as global inside function this fantastic will
#be replaced

## To convert a number into complex we use complex

moo = ' bo oo '

print(moo.strip()) # Strip is used to remove white spaces in start and end

x = 10        # x is still an int
print(f'The price is {x:.2f} dollars')
# Output: The price is 10.00 dollars

print(type(x))  # <class 'int'>  ← x is still an int!

print(bool("abc"))


# So "abc" is non-empty, therefore bool("abc") → True. Even bool("False") returns True because the string "False" is still a non-empty string!
# ​
#
# python
# print(bool("abc"))      # True  non-empty
# print(bool("False"))    # True  still non-empty!
# print(bool(""))         # False empty string
# What Returns False in Python
# bool() returns False only for "empty" or "zero" values:
# ​
#
# Value	Result
# "" (empty string)	False
# 0 (integer)	False
# 0.0 (float)	False
# [] (empty list)	False
# {} (empty dict)	False
# None	False

# # Without walrus (repetitive)
# data = input("Enter: ")
# while data != "quit":
#     print(data)
#     data = input("Enter: ")
#
# # With walrus (cleaner)
# while (data := input("Enter: ")) != "quit":
#     print(data)
#
# # USed to declare cleaner use it as expressions
# # is operator used for checking if the operator points to same or not

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y)   # True  ✅ same values
print(x is y)   # False ❌ different objects in memory
print(x is z)   # True  ✅ z points to the exact same object as x