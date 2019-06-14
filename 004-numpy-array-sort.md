---
YamlDesc: CONTENT-ARTICLE
Title: Python NumPy Sort
MetaDescription: Python, NumPy, sort, ArgSort, LexSort
MetaKeywords: Python, NumPy, sort, ArgSort, LexSort
Author: (c) Venkata Bhattaram / tinitiate.com
ContentName: python-numpy-sort
---

# Python NumPy Sort
* Here we demonstrate Printing Array Values
* `sort` Sorts Datas of a a give Array.
* `ArgSort` Sorts array and returns the sorted index of the array.
* `lexsort` Sorts multiple arrays, and returns the sorted Index of the array.
* `partition` 
* `sorted` 

```
import numpy as np

# Test Array
sarr = np.array([[6,2,8],
                 [4,3,9],
                 [5,1,7]])

########################
# Print Data
########################
for x in np.nditer(sarr):
   print(x)


#######################
# Sort Data
#######################
# Sorts the Array Data Ascending
print(np.sort(sarr, axis=0))

# Sorts the Array Data Descending
print(np.sort(sarr, axis=0)[::-1])


#######################
# ArgSort Data
#######################
# Sorts the Index Ascending
print(np.argsort(sarr))

# Sorts the Index Descending
print(np.argsort(-sarr))


#######################
# LexSort Data
#######################
# Sort by multiple arrays, returns the Index of the sorted arrays

# Sorts A2 First and then A1, In case of a samevalue, then A1, values are used 
# to do a tie breaker, where A1's values are sorted to get the final values
A1 = (1,1,3)
A2 = (3,1,1)
print(np.lexsort((A1, A2)))
# 1,2,0

A1 = (4,5,6)
A2 = (2,3,4)
print(np.lexsort((A1, A2)))
# 0,1,2

A1 = (4,3,6)
A2 = (2,2,4)
print(np.lexsort((A1, A2)))
# 1,0,2

# Descending Order Sort

```
