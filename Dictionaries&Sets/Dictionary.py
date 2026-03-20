 #Well dictionary is nothing but json in simple terms

fruits = {
    "apple": "Apple",
    "banana": "Banana",
    "orange": "Orange",
    "mango": "Mango",
}

seeds = dict(watermelon = 'Watermelon',onion = 'Onion')

print(seeds)
print(fruits)

#Access Items
print(fruits['banana'])
print(fruits.get('apple'))

#list all keys
print(fruits.keys())
#list all values
print(fruits.values())
#shows key and values as tuples
print(fruits.items())

#verify key in dictionary
print('mango' in fruits)

#Change values in dictionary
fruits['banana'] = 'Sappota'
fruits.update({'blueberry' : 'Blueberry'},)

#Remove items
print(fruits.pop('banana'))

print(fruits.popitem()) # it will remove the last added item as tuple

#Delete Items
del fruits['apple'] # deletes the key and value

print(fruits) #.clear() is used to clear the dictionary del to delete

#Copy Dictionary

rottenFruits = fruits.copy()
rottenFruits.update({'rottenMango': 'RottenMango'})
print(rottenFruits)