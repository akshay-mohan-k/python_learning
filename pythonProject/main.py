import numpy as np

array = np.array([1, 2, 3, 4, 5])

print(array)

print(type(array))

#2-D array
array2 = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15]])

#3-D Array
array3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
                   [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])

print(array3.shape)


