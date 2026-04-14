import numpy as np
#1
arr = np.array([5,10,15,20,25])
print(arr * 3)

#2
matrix = np.zeros((3,3,3))
print(matrix.shape)


#Task1
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

#1. Print the last element of the first row using negative indexing
print(matrix[0,-1])

#2. Slice and print the entire second column
print(matrix[:,1])

#3. Slice rows 0 and 1, columns 1 and 2 (should give [[20,30],[50,60]])

print(matrix[0:2,1:3])

#4. Print the mean of the entire matrix
print(np.mean(matrix))

#########################################################################

arr = np.arange(1,13)

print(arr.reshape(3,4))

flattened = arr.flatten()
print(flattened.shape)


scores = np.array([45, 72, 38, 90, 55, 68, 81, 29])

print(scores[scores>60])

print(scores[(scores>50) & (scores<80)])


###########################################################################

#1
np.random.seed(7)
print(np.random.randint(1,50,5))

#2
data = np.array([15, 88, 42, 67, 23, 91, 55, 38])

print(np.mean(data))
print(np.median(data))
print(np.std(data))

print(np.where(data> np.mean(data),'High','Low'))