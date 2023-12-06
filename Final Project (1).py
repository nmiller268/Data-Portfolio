#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Final Project- Nicole Miller
# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# load the diabetes dataset
diabetes = load_diabetes()

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.2, random_state=0)

# create a linear regression object
lr = LinearRegression()

# fit the linear regression model to the training data
lr.fit(X_train, y_train)

# predict the test set results using the trained model
y_pred = lr.predict(X_test)

# calculate the mean squared error and r-squared value
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# print the results
print("Mean squared error: %.2f" % mse)
print("Coefficient of determination (r-squared): %.2f" % r2)

# plot the actual vs predicted values
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.show()


# In[ ]:




