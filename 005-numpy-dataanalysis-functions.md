---
YamlDesc: CONTENT-ARTICLE
Title: Python NumPy Trigonometric Functions for Data Analysis
MetaDescription: Python NumPy Trigonometric Functions for Data Analysis
MetaKeywords: Python, NumPy, Trigonometric Functions, Data Analysis Functions
Author: (c) Venkata Bhattaram / tinitiate.com
ContentName: numpy-data-analysis-trigonometric-functions
---

# NumPy Trigonometric Functions
* In Right Angle Triangles
* sine:    opposite/hypotenuse
  * Trigonometric sine, element-wise.
  * This is implemented by numpy.sin
* cosine:  adjacent/hypotenuse
  * Cosine element-wise.
  * This is implemented by numpy.cos  
* tangent: opposite/adjacent
  * Compute tangent element-wise.
  * This is implemented by numpy.tan
* Here we demonstrate the SIN, COS, TAN data and its representation on a graph.


```
import numpy as np
import matplotlib.pyplot as plt

# SIN Data
##########
in_array = np.linspace(-np.pi, np.pi, 12)
out_array = np.sin(in_array)
print(out_array)

# red for numpy.sin()
plt.plot(in_array, out_array, color = 'red', marker = "o")
plt.title("numpy.sin() SET-1")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# COS Data
##########
in_array = np.linspace(-np.pi, np.pi, 12)
out_array = np.cos(in_array)
print(out_array)

# red for numpy.cos()
plt.plot(in_array, out_array, color = 'red', marker = "o")
plt.title("numpy.cos() SET-1")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# TAN Data
##########
in_array = np.linspace(-np.pi, np.pi/2, np.pi)
out_array = np.tan(in_array)
print(out_array)

# red for numpy.tan()
plt.plot(in_array, out_array, color = 'red', marker = "o")
plt.title("numpy.tan() SET-1")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

```
