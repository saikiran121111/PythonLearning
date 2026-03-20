#String DataType
#Literal Assignment
firstName = 'Sai'
lastName = 'Kiran'

print(type(firstName))
print(type(firstName) == str)
print(isinstance(firstName, str))

#Constructor functions

age = str(26)
print('Type of age is', type(age))

#Concatenate
year = str(2000)

print('My name is '+firstName+' '+lastName+' '+'I was born in year '+year+' '+'My current age is '+age)

#Multiple Lines

multipleLines = f'''
My name is {firstName} {lastName}
I was born in year {year}
My current age is {age}'''
#f is used to declare variables inside the string using {}
print(multipleLines)

#Escaping Special Characters
print('I\'m saikiran\nI\'ve located this \\ in this sentence\tPlease check..!!!')

# String Methods
print(firstName.lower())
print(firstName.upper())

print('THIs iS a tITlE'.title())

print('Bakery'.center(20,'-'))
print('coffee'.ljust(15,' ') + str(7).rjust(2,' '))
print('Tea'.ljust(15,' ') + str(2).rjust(2,' '))
print('Cupcake'.ljust(15,' ') + str(10).rjust(2,' '))
print('ButterCake'.ljust(15,' ') + str(30).rjust(2,' '))
print('Bakery'.center(20,'-'))

print(multipleLines.replace('My name is ', 'Name\'s '))

print(len(multipleLines))

#strip() is used to remove spaces lstrip is for left rstrip is for right

#String Index values
print(' ')
print(firstName[0])#gets the first index value of the string
print(firstName[-1])#-1 gets the last value of the string
print(lastName[0:4])#Basically a range of what we need to print leave empty to print upto last

#Some methods return boolean data
print(' ')
print('Boolean')
print(firstName[0] == 's'.upper())
print(firstName.startswith('s'.upper()))

#Gates
# AND OR NOT

firstvalue = True
secondvalue = False
thirdvalue = True

print('and value '+ str(firstvalue and secondvalue))
print('or value '+ str(firstvalue or secondvalue))
print('not second value '+str(not secondvalue))
print('not first value '+str(not firstvalue))

#Numeric data types
integer = int(1)
floating = float(1)

#round() for rounding | abs() for absoulute