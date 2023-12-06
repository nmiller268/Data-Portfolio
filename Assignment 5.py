#!/usr/bin/env python
# coding: utf-8

# In[24]:


#Assign 5 Nicole Miller
import pandas as pd
temp_dict={'Maxine': [80,30,40],'James':[100,60,90],'Amanda': [60,70,80]}
temperature = pd.DataFrame(temp_dict)

temperature.index=['Morning', 'Afternoon', 'Evening']

temperature


# In[25]:


temperature['Maxine']


# In[27]:


temperature.loc['Morning']


# In[28]:


temperature.loc[['Morning','Evening']]


# In[29]:


temperature[['Amanda', 'Maxine']]


# In[30]:


temperature[['Amanda', 'Maxine']].iloc[[1,2]]


# In[31]:


temperature.describe()


# In[32]:


temperature.sort_index(axis=1)


# In[33]:


temperature.T


# In[ ]:




