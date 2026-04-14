import numpy as np
#1 way use arrays from list
nums = np.array([1,2,3,4,5]) #Numpy Arrays are advanced when compared to list
#Can do multiple calculations



nums *= 2

print(f'list array {nums}')

#Think of shape as "what does this array look like?" — you'll use it constantly in AI/ML.
print(f'says how many elements and dimension of the array {nums.shape}')
print(f'says data type of values in array {nums.dtype}')
print(f'says the size {nums.size}')
#2 way use All zeros (used alot in AI/ML)

b = np.zeros(5)
print(b)

#3 A range (like python's range [starting value , ending value , increment] but returns array)

rangearray = np.arange(0,10,2)

print(rangearray)

#4 evenly spaced numbers
evenspaced = np.linspace(0,1,5) # 0 to 1 we got evenly spaced
#we can get evenly spaced values between numbers

print(evenspaced)

#2D arrays

matrix = np.array([[1,2,3], # first row column starts from 0 not 1
                   [4,5,6]])
print(matrix.shape)
print(f'prints the first array {matrix[0]}')
print(f'this prints the value of exact place {matrix[0][1]}') # IT does have 0 based indexing so starts from 0


## Indexing slicing and Operations

indexing = np.array([1,2,3,4,5])

print(indexing[-2])

# slicing grabbing a chunk

print(indexing[1:4])

#The rule: arr[start : stop : step]
#stop is never included
#leave blank = go to the end/start

# Slicing 2D Array

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix[0:2,1:3])
print(matrix[:,0]) # entire first column
print(matrix[0,:])# entire first row

a = np.array([1,2,3,4])
b = np.array([10,20,30,40])

print(a+b) # adding two array lists

print(sum(a)) # sum of all values in array list

# We don't need loops if we use numpy array

#Reshape

arr = np.arange(1,10)

print(arr.reshape(3,3)) # reshapes the value to 3x3 matrix

#flatten
print(arr.flatten()) # flattens to a single list

# Boolean Masking
#Can print stuff by adding conditions

print(arr[(arr>3) & (arr<6) ])