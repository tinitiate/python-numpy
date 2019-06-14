""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python NumPy Array Operations
MetaDescription: Python NumPy Array Operatons, reshape, flatten, hstack, vstack, Array Slicing
MetaKeywords: Python NumPy Array Operatons, reshape, flatten, hstack, vstack, Array Slicing
Author: (c) Venkata Bhattaram / tinitiate.com
ContentName: numpy-array-operations
---
MARKDOWN """

""" MARKDOWN
# Python NumPy Array Operations
* `reshape` Transpose MultiDimensional Array Matrix
* `flatten` Flattens a given MultiDimensional Array Matrix into a 1-D array
* `vstack` Append data vertically
* `hstack` Append data horizontally
* Array Slicing with indexes, by ROW and COLUMN, and the colon (:) operator
MARKDOWN """

# MARKDOWN ```

import numpy as np 


##########################################
# reshape
# Transpose MultiDimensional Array Matrix
# Here we have 3 X 2 matrix
##########################################
arr1 = np.array([[1, 2], 
                 [1, 2],
                 [1, 2]])

# ReShape into 2 X 3
print(arr1.reshape(2,3))


##########################################
# Flatten
# Flattens a given MultiDimensional 
# Array Matrix into a 1-D array
##########################################
arr1 = np.array([[1, 2], 
                 [1, 2],
                 [1, 2]])

print(arr1.flatten())


##########################################
# HStack
# Append ARRAYs horizontally
##########################################
a1 = np.array([1,2,3])
a2 = np.array([7,8,9])

print(np.hstack((a1,a2)))


##########################################
# VStack
# Append ARRAYs vertically
##########################################
a1 = np.array([1,2,3])
a2 = np.array([7,8,9])

print(np.vstack((a1,a2)))


##########################################
# Array Slicing
# Extract Parts of NumPy Array
##########################################
sarr = np.array([[1,  2,  3,  4],
                 [11, 22, 33, 44],
                 [111,222,333,444]])

# ROWS
print(sarr[0])
print(sarr[1])
print(sarr[2])

# COLUMNS after the COMMA
print(sarr[:,0])
print(sarr[:,1])

# Single Value
print(sarr[1,0])


# Array Slicing with Colon (:) Operator and indexes
# 1. The colon operator (:) indicates the position from 
#    where the part of the array needs to be selected
# 2. Number Before Colon indicates include those values
# 3. Number after Colon indicates exclude those values
print(sarr[:2,:2])
#  [[ 1  2]
#   [11 22]]

print(sarr[:,:2])
#  [[  1   2]
#   [ 11  22]
#   [111 222]]

print(sarr[:,2:])
#  [[  3   4]
#   [ 33  44]
#   [333 444]]

print(sarr[1:,2:])
#  [[ 33  44]
#   [333 444]]

print(sarr[:13,:2])
#  [[  1   2]
#   [ 11  22]
#   [111 222]]

# MARKDOWN ```
