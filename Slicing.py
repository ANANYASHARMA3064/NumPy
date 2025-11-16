import numpy as np
array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]
                  ])
# array[start:end:step]

# print(array[::-1]) to reverse
# print(array[:,0]) access column zeroes for all rows
# print(array[:,0:3]) first 3 columns of all rows
# print(array[:, ::2])   [[ 1  3]
#  [ 5  7]
#  [ 9 11]
#  [13 15]] this is basically using steps in columns
print(array[0:2,0:2])




