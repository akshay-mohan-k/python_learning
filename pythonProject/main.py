import numpy as np

array = np.array([1, 2, 3, 4, 5])

print(array)


#2-D array
array2 = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15]])

#print an element
print(array2[0,1])

#print a subarray
print(array2[1:3])

#3-D Array
array3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
                   [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])


#scalar arithmetic

print(array + 1)
print(array -1)
print(array * 2)
print(array / 2)
print(array ** 2)

print(np.sqrt(array))

