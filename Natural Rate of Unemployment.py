#!/usr/bin/env python
# coding: utf-8

# In[9]:


import quandl
import pandas as pd
import matplotlib.pyplot as plt
quandl.ApiConfig.api_key = "TQUQzkUTBHrerch_9RnN"


# In[10]:


nru = quandl.get("FRED/NROUST")


# In[11]:


type(nru)


# In[17]:


plt.plot(nru)
plt.xlabel('Year')
plt.ylabel('NRU')
plt.title('Natural rate of unemployment over the years')
nru.describe()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




