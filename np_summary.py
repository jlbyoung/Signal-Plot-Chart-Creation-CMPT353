#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[22]:


data = np.load('monthdata.npz')


# In[4]:


totals = data['totals']


# In[5]:


counts = data['counts']


# In[6]:


leastTotal = np.argmin(np.ndarray.sum(totals, 1))
print("Row with the least precipitation: " )
print(leastTotal)


# In[7]:


print("Average precipitation in each month: ")
print(np.ndarray.sum(totals, 0)/np.ndarray.sum(counts, 0))


# In[8]:


print("Average preciptation in each city: ")
print(np.ndarray.sum(totals, 1)/np.ndarray.sum(counts, 1))


# In[21]:


reshape = totals.reshape(-1, 3).sum(1).reshape(9, 4)
print(reshape)


# In[ ]:




