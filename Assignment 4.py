#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Assignment 4 Nicole Miller
import numpy as np
from collections import Counter

def median(arr, axis=None):
    return np.median(arr, axis=axis)

def mode(arr, axis=None):
    if axis is None:
        arr = arr.flatten()
        counts = Counter(arr)
        mode = counts.most_common(1)[0][0]
        return mode
    else:
        modes = []
        if axis == 0:
            arr = arr.T
        for row in arr:
            counts = Counter(row)
            mode = counts.most_common(1)[0][0]
            modes.append(mode)
        return np.array(modes)


#usage of these functions:-

# Test arrays of different shapes
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# Calculate median
print("Median of arr1: ", median(arr1))
print("Median of arr2: ", median(arr2, axis=0))
print("Median of arr3: ", median(arr3, axis=1))

# Calculate mode
print("Mode of arr1: ", mode(arr1))
print("Mode of arr2: ", mode(arr2, axis=0))
print("Mode of arr3: ", mode(arr3, axis=1))


# In[ ]:





# In[ ]:




