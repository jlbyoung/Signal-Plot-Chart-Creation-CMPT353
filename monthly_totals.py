#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd


# In[57]:


def date_to_month(d):
    # You may need to modify this function, depending on your data types.
    return '%04i-%02i' % (d.year, d.month)


# In[58]:


data = pd.read_csv('precipitation.csv', parse_dates=[2])


# In[60]:


data['month'] = data.date
data.month = data['date'].apply(date_to_month)
monthly = data.groupby(['name', 'month'])['precipitation'].agg('sum').reset_index()
monthly = monthly.pivot(index='name', columns='month')    
counts = data.groupby(['name', 'month'])['precipitation'].agg('count').reset_index()
counts = counts.pivot(index='name', columns='month')


# In[62]:


print(monthly)


# In[63]:


print(counts)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




