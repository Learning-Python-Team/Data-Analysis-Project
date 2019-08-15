#!/usr/bin/env python
# coding: utf-8

# In[22]:


#Import libraries
import quandl
import pandas as pd
import matplotlib.pyplot as plt

#Personal API Key
quandl.ApiConfig.api_key = "TQUQzkUTBHrerch_9RnN"


# In[31]:


#Pull data from quandl

#Short term
nru_st = quandl.get("FRED/NROUST")
#Long term
nru_lt = quandl.get("FRED/NROU")


# In[27]:


#Check the data structures
type(nru_st)
type(nru_lt)


# In[72]:


#Plot the data

#Short term plot
plt.plot(nru_st, label='st')
#long term plot
plt.plot(nru_lt, label='lt')

#x/y axis labels
plt.xlabel('Year',fontsize=20)
plt.ylabel('NRU',fontsize=20)

#Title for plot
plt.title('Natural rate of unemployment over the years',fontsize=20)

#Legend for short-term and long-term
plt.legend(fontsize=20)

#plt.gcf() allows you to get a reference to the current figure when using pyplot
fig = plt.gcf()
#Set the figure/plot size
fig.set_size_inches(16, 8)

#Display the plot
plt.show()

#Provide some summary statistics
nru.describe()[1::]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




