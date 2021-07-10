#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from glob import glob


# In[4]:


filepaths = glob('source/*')
filepaths


# In[6]:


filepaths[0]


# In[7]:


filepath =filepaths[0]
filepath


# In[9]:


_df=pd.read_excel(filepath)
_df


# In[88]:


colums=_df.iloc[10,[1,2,4,10,11,14]]
colums


# In[89]:


df=_df.iloc[11:23,[1,2,4,10,11,14]]
df


# In[90]:


df.columns=colums
df


# In[91]:


df['企業名']=_df.iloc[2,0]
df


# In[92]:


df['企業コード']=_df.iloc[3,4]
df['請求No']=_df.iloc[2,12]
df['発行日']=_df.iloc[3,12]
df['発行者']=_df.iloc[4,12]
df['発行者コード']=_df.iloc[4,13]
df


# In[98]:


def extract(filepath):
    _df=pd.read_excel(filepath)
    df=_df.iloc[11:23,[1,2,4,10,11,14]]
    colums=_df.iloc[10,[1,2,4,10,11,14]]
    df.columns=colums
    df['企業名']=_df.iloc[2,0]
    df['企業コード']=_df.iloc[3,4]
    df['請求No']=_df.iloc[2,12]
    df['発行日']=_df.iloc[3,12]
    df['発行者']=_df.iloc[4,12]
    df['発行者コード']=_df.iloc[4,13]
    return df

filepaths = glob('source/*xlsx')
for filepath in filepaths:
    extract(filepath)
for filepath in filepaths:
# In[99]:


pd.DataFrame([[1,2,3,5],[1,2,3,4]])


# In[100]:


abc=pd.DataFrame()

for filepath in filepaths:
    simple=extract(filepath)
    abc=pd.concat([abc,simple],axis=1)


# In[101]:


abc


# In[102]:


abc=abc.dropna()
abc


# In[103]:


abc=abc.iloc[:,[6,7,8,9,10,1,2,3,4,5]]


# In[104]:


abc


# In[106]:


abc.to_excel('output/all_data.xlsx',index=False)


# In[ ]:




