#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[33]:


totals = pd.read_csv('totals.csv').set_index(keys=['name'])
counts = pd.read_csv('counts.csv').set_index(keys=['name'])


# In[35]:


totals


# In[36]:


counts


# In[19]:


print("City with lowest precipitation: ")
print(totals.sum(1).idxmin())


# In[40]:


print("Average precipitation in each month: ")
print(totals.sum(0)/counts.sum(0))


# In[42]:


print("Average precipitation in each month:")
print(totals.sum(1)/counts.sum(1))


# In[ ]:




