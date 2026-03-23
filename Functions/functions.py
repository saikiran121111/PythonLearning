import sys


def hello(): # defining the function # All functions should be lowercase
    print('Hello World') # implementation
hello() # Calling the function

def addition(num1=0, num2=0): # added 0 as default values
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    return num1 / num2

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

operation = input(
'''Enter operation: \n
1. Addition
2. Subtraction
3. Multiplication
4. Division
''')
if operation == '1':
    print(addition(a, b))
elif operation == '2':
    print(subtraction(a, b))
elif operation == '3':
    print(multiplication(a, b))
elif operation == '4':
    print(division(a, b))
else:
    sys.exit('Wrong Input')


def multi_args(*args): # Used if we don't know how many arguments we get for a function
    print(args)
    print(type(args))
multi_args('Hey', 2,'There' ) # -> This prints as a tuple
#If we want to know the key and value of it then we need to use kwargs which is key word args

def multi_kwargs(**kwargs): # Used if we don't know how many arguments we get for a function
    print(kwargs)
    print(type(kwargs))
multi_kwargs(first = 'sai', last = 'kiran') # -> This prints as a dict