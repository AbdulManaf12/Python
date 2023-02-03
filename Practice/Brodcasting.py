#Broadcasting
#In python, broadcasting refers to how numpy treats arrays with different dimensions during arithmetic operations,
#which lead to certain constraints, the smaller array is broadcast across the larger array so that they have compatible shapes.

import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([1, 5, 10, 15, 20])
result = array1 * array2
print(f'1. Arrays with same dimension: \narray1: {array1} \narray2: {array2}\nResult: {result}\n\n')

array1 = np.array([1, 2, 3, 4, 5])
array2 = 20
result = array1 * array2
print(f'2. Arrays with different dimension: \narray1: {array1} \narray2: {array2}\nResult: {result}')
