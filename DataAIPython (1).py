#!/usr/bin/env python
# coding: utf-8

# In[1]:


def squareIT(x):
    return x * x

print(squareIT(2))


# In[2]:


import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np


# In[6]:


affairs_df= pd.read_csv('Downloads/Affairs.csv')

affairs_df.info()


# In[ ]:




