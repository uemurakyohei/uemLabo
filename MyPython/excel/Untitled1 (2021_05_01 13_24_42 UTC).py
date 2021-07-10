#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from glob import glob


# In[8]:


filepaths=glob('source/*.xlsx')
filepaths


# In[9]:


filepath=filepaths[0]


# In[10]:


filepath


# In[11]:


_df = pd.read_excel(filepath)
_df


# In[14]:


colums=_df.iloc[10,[1,2,4,10,11,14]]


# In[29]:


colums


# In[18]:


df=_df.iloc[11:23,[1,2,4,10,11,14]]
df


# In[20]:


df.columns=colums
df


# In[21]:


df['企業名']=_df.iloc[2,0]


# In[22]:


df.head()


# In[31]:


df['企業コード']=_df.iloc[3,4]
df['請求No']=_df.iloc[2,12]
df['発行日']=_df.iloc[3,12]
df['発行者']=_df.iloc[4,12]
df['発行者コード']=_df.iloc[4,13]


# In[32]:


df


# In[33]:


df.head()


# In[39]:


def extract(filepath):
    _df = pd.read_excel(filepath)
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


# In[40]:


extract(filepath)


# In[48]:


sample_1 =pd.DataFrame([[1,2,3],[4,5,6]])
sample_2 =pd.DataFrame([[-1,2,5],[5,4,3,2]])


# In[49]:


sample_2


# In[52]:


pd.concat([sample_1,sample_2],axis=1)


# In[63]:


df =pd.DataFrame()
for filepath in filepaths:
    _df =extract(filepath)
    df = pd.concat([df,_df])


# In[65]:


filepaths


# In[66]:


df


# In[69]:


df=df.dropna()
df


# In[71]:


df=df.iloc[:,[6,7,8,9,10,1,2,3,4,5]]


# In[72]:


df


# In[74]:


df.to_excel('output/all_data.xlsx',index=False)


# In[ ]:




