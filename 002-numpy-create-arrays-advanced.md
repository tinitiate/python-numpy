---
YamlDesc: CONTENT-ARTICLE
Title: Python NumPy
MetaDescription: Python NumPy
MetaKeywords: Python Pandas create using np.arange, np.linspace, np.logspace
Author: (c) Venkata Bhattaram / tinitiate.com
ContentName: python-numpy-advanced-array-creation
---

# Python NumPy
* NumPy is a general-purpose array-processing Python package, for scientific 
  data computing.
* The array is a multidimensional object with high-performance and provides 
  power tools out of the box for array data processing.

## NumPy Array
* Here we demonstrate various advanced ways for array creation
* `arange` creates numbers between 0,30 with distance of 5
* `linspace` Create 10 even spaced numbers between 0 and 5
* `logspace` Create 10 even spaced numbers on log scale between 0 and 5

```
import numpy as np

# arange create numbers between 0,30 with distance of 5
a1 = np.arange(0, 36, 6) 
print(a1)

# Create 10 even spaced numbers between 0 and 5
a2 = np.linspace(0, 5, 10) 
print(a2)

# Create 10 even spaced numbers on a log scale between 0 and 5
a2 = np.logspace(0, 5, 10) 
print(a2)

```
