""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python NumPy Statistical Functions, Min, Max, Mean, Median, Standard deviation
MetaDescription: Python NumPy Statistical Functions, Min, Max, Mean, Median, Standard deviation
MetaKeywords: Python NumPy Statistical Functions, Min, Max, Mean, Median, Standard deviation
Author: (c) Venkata Bhattaram / tinitiate.com
ContentName: python-numpy-statistical-functions
---
MARKDOWN """

""" MARKDOWN
# Python NumPy Statistical functions
* Min np.min()
* Max np.max()
* Mean np.mean(), "mean" is the "average"
* Median np.median(), The "median" is the "middle" value in the list of numbers
* Standard deviation np.stdt(), is the measure that quantifies the amount of 
  variation or dispersion of a set of data values
MARKDOWN """

# MARKDOWN ```
import numpy as np

num_arr = np.linspace(0, 5, 10) 
print(num_arr)

## Min, Get MIN from the array 
print(np.min(num_arr))

## Max, Get Max from the array 
print(np.max(num_arr))

## Mean, Get Mean from the array  
print(np.mean(num_arr))

## Median, Get Median from the array 
print(np.median(num_arr))

## SD, Get Standard deviation from the array 
print(np.std(num_arr))

# MARKDOWN ```
