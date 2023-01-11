#!/usr/bin/env python
# coding: utf-8

# In[6]:


name = input("Enter your name ")
weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter your height in inches: "))
BMI = (weight * 703) / (height * height)
             
print (BMI)


# In[7]:


if BMI>0:
    if (BMI<18.5):
        print(name +", you are underweight.")
    elif (BMI<=24.9):
        print(name +", you are normal weight.")
    elif (BMI<29.9):
        print(name +", you are overwieght.")
    elif (BMI<34.9):
        print(name +" , you are obese.")
    elif (BMI<39.9):
        print(name +", you are severly obese. Make sure you are getting as much excersice as needed. ")
    else: 
        print(name +", you are morbidly obese")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




