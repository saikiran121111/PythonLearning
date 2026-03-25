# modules can be imported and used

#import math # math is a module here
#import random
#To pull what we need we use
from enum import Enum
from math import pi
from random import randint # etcc
import my_City_Details

# Can change the names of modules aswell
import random as rnd # changed the name random to rnd

print(pi)# we used pi inside math module
print(rnd.randint(1,7))

print(my_City_Details.city) # I got this from the file I have created
print(my_City_Details.country)
print(my_City_Details.randomFunFact()) # using randiant for random list fetch

print(my_City_Details.__name__) # usually prints the name of the module