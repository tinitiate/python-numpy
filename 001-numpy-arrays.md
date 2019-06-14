---
YamlDesc: CONTENT-ARTICLE
Title: Python NumPy
MetaDescription: Python NumPy
MetaKeywords: Python Pandas create array, random array, zeros array, arange, linspace
Author: (c) Venkata Bhattaram / tinitiate.com
ContentName: python-numpy-arrays
---

# Python NumPy
* NumPy is a general-purpose array-processing Python package, for scientific 
  data computing.
* The array is a multidimensional object with high-performance and provides 
  power tools out of the box for array data processing.

## NumPy Array
* Here we demonstrate various array creation methods that are commonly used.
* Simple array creation
* Creating array from list with type (float , int, complex)
* Create all ZEROS and ONES arrays
* Create N X N array of complex type
* Fill N X N with random numbers
* Create N X N array of type INT
* Create N X N array of type FLOAT

```
import numpy as np

# array
###############################
# Simple array creation
array1 = np.array([1,2,3,4,5])
print(array1)


# array: 
####################################
# Creating array from list with
# type float 
a1 = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float') 
print(a1)


# zeros: All Zeros
####################################
a2 = np.zeros((3, 4), dtype = 'int') 
print(a2)

# Ones: All Ones
###################################
a2 = np.ones((3, 4), dtype = 'int') 
print(a2)

# full
####################################
# Create N X N array of complex type
a3 = np.full((3, 3), 10, dtype = 'complex')
print(a3)

# random.random
####################################
# Fill N X N with random numbers
a4 = np.random.random((5, 5))
print(a4)


# random.randn
####################################
# Create N X N array of type INT
a5 = np.random.randn(3, 3).astype('i')
print(a5)


# random.randn
####################################
# Create N X N array of type FLOAT
a6 = np.random.randn(3, 3).astype('f')
print(a6)

```
