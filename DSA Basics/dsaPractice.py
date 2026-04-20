# my_toys = ["car", "ball", "doll", "car"]
#
# store = {}
#
# for i in my_toys:
#
#     if i in store:
#         print('Duplicate found')
#
#     else:
#         store[i] = i
from functools import reduce

pit_stops = ["Petrol Pump", "Dhaba", "Toll Gate"]

pit_stops.insert(1,'Mechanic')
pit_stops.append('Hotel')
print(pit_stops)

inventory = ["Flask", "Sword", "Broken Rune", "Shield", "Broken Rune"]

storeItems = []

for i in inventory:
    if i != 'Broken Rune':
        storeItems.append(i)

print(storeItems)


gears = [1, 2, 3, 4, 5]

descendingGears = []

for i in range(len(gears)):

    maxvalue = reduce(lambda acc,num : acc if acc> num else num,gears)
    descendingGears.append(maxvalue)
    gears.remove(maxvalue)

print(descendingGears)


nums = [0, 0, 1]
count = 0
for i in nums:
    if i != 0:
        continue
    else:
        nums.remove(i)
        count +=1

if count != 0:
    for i in range(count):
        nums.append(0)

print(nums)