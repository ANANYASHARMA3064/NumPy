import numpy as np
#each of these array need to have the same number of values
array = np.array([[['A','B','C'], ['D','E','F'], ['G','H','I']],[['A','B','C'], ['D','E','F'], ['G','H','I']],[['A','B','C'], ['D','E','F'], ['G','H','I']]])
# print(array.ndim)
# print(array.shape) number of layers, number of rows number of columns
# print(array[0,0,0])layer 0, column 0,row 0
word = array[0,0,0] + array[2,0,0]
print(word)

