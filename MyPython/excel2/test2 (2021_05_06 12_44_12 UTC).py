#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from glob import glob


# In[2]:


filepaths = glob('sources/請求書*.xlsx')


# In[3]:


filepaths


# In[4]:


filepath=filepaths[0]


# In[5]:


filepath


# In[6]:


_df=pd.read_excel(filepath)
_df


# In[7]:


columns=_df.iloc[10,[1,2,4,10,11,14]]
columns


# In[8]:


df=_df.iloc[11:21,[1,2,4,10,11,14]]
df


# In[9]:


df.columns=columns
df


# In[10]:


df['企業名']=_df.iloc[2,0]
df['企業コード']=_df.iloc[3,4]
df['請求No']=_df.iloc[2,12]
df['発行日']=_df.iloc[3,12]
df['発行者']=_df.iloc[4,12]
df['発行者コード']=_df.iloc[4,13]


# In[11]:


df


# In[22]:


def extract(filepath):
    _df=pd.read_excel(filepath)
    columns=_df.iloc[10,[1,2,4,10,11,14]]
    df=_df.iloc[11:21,[1,2,4,10,11,14]]
    df.columns=columns
    df['企業名']=_df.iloc[2,0]
    df['企業コード']=_df.iloc[3,4]
    df['請求No']=_df.iloc[2,12]
    df['発行日']=_df.iloc[3,12]
    df['発行者']=_df.iloc[4,12]
    df['発行者コード']=_df.iloc[4,13]
    return df


# In[23]:


df = pd.DataFrame()

for filepath in filepaths:
    df=pd.concat([df,extract(filepath)])


# In[24]:


df=df.reset_index(drop=True)


# In[25]:


df=df.dropna()
df


# In[26]:


df.to_excel('output/all_data02.xlsx',index=False)


# In[27]:


df


# In[47]:


members=df['発行者'].unique()
members


# In[31]:


member=members[0]


# In[36]:


_df=df[df['発行者']==member]
_df


# In[37]:


_df['金額'].sum()


# In[49]:


companies=df['企業名'].unique()
companies


# In[51]:


earnings=_df[_df['企業名']==companies[0]]['金額'].sum()
earnings


# In[52]:


tot_earnings=_df['金額'].sum()


# In[53]:


tot_earnings


# In[54]:


earnings=_df[_df['企業名']==companies[0]]['金額'].sum()


# In[55]:


pd.DataFrame({'担当者':member,'企業名':'全体','金額':tot_earnings},index=[0])


# In[57]:


total_res=[]
for member in members:
    _df=df[df['発行者']==member]
    tot_earnings=_df['金額'].sum()
    companies=_df['企業名'].unique()
    total_res.append(dict(担当者=member,企業名='全体',金額=tot_earnings))
    
    for company in companies:
        earnings=_df[_df['企業名']==company]['金額'].sum()
        total_res.append(dict(担当者=member,企業名=company,金額=earnings))


# In[58]:


total_res


# In[60]:


pd.DataFrame(total_res,columns=['担当者','企業名','金額'])


# In[ ]:




