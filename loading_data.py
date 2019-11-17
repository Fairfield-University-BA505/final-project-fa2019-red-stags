#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Objectives:
    - Find out the characteristics of a murderer or a victim
        - Murderer: mental history, history of abuse/trauma, income, relationship status, drug use, age, sex, state, race etc for both, past records... YEAR!!!!!
    - The chances you could be one of those depending on a state or all? (check box lets say you puched someone your prob. goes up)
        - we could run some model like machine learning for classification 


# In[21]:


import pandas as pd
import numpy as np


# In[13]:


# uploading data and looking at its structure and contents 
# easiest way is by subsetting rows/columns 
# looking for patterns 
# CSV is seperated by commas 
df1 = pd.read_csv("US HOMOCIDE REPORT.csv", sep=",")
head = df1.head()
tail = df1.tail()
join = pd.concat([head,tail])
join


# In[6]:


# type function checking type of data
type(df1)


# In[8]:


# number of rows and column of df1
# shape is an attribute (result is tuple)
df1.shape


# In[45]:


# checking column names of data set
# data type pd core indexes base index
col = df1.columns
print(col)


# In[12]:


# remember each column series has t be same type in df, each row can be mixed 
# checking the type of data in the dataset 
# Results: record ID, year, incident, victim age, victim count, perpertrator count are whole numbers (int64)
# object most common data type 
df1.dtypes


# In[37]:


# subsetting data 
# MISTAKE there are only 50 states !!!
unique_state = df1["State"].unique()
print(unique_state)
print("Number of states:", len(unique_state))


# In[39]:


# 2 types of crime 
unique_crime = df1["Crime Type"].unique()
unique_crime


# In[40]:


victim_sex = df1["Victim Sex"].unique()
victim_sex


# In[44]:


# all unique values in the rows 
for el in col:
    uniques = df1[el].unique()
    print(el, uniques)


# In[52]:


# cunting for murderers 
df1.loc["Male", "Perpetrator Sex"].count()


# In[ ]:




