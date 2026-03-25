from random import randint

city = 'Hyderabad'
country = 'India'

rand = randint(0,2)

def randomFunFact():
    details = ['Good city', 'okay city', 'I don\'t know']

    txt = details[rand]

    return txt

