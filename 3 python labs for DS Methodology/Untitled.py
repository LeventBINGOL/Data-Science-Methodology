#!/usr/bin/env python
# coding: utf-8

# In[1]:


# check Python version
get_ipython().system('python -V')


# In[2]:


import pandas as pd # download library to read data into dataframe
pd.set_option('display.max_columns', None)

recipes = pd.read_csv("https://ibm.box.com/shared/static/5wah9atr5o1akuuavl2z9tkjzdinr1lv.csv")

print("Data read into dataframe!") # takes about 30 seconds


# In[3]:


recipes.head()


# In[ ]:


recipes.shape

