#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
from glob import glob


# In[55]:


filepaths=glob('sources/請求書*.xlsx')
filepaths


# In[56]:


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


# In[57]:


df = pd.DataFrame()

for filepath in filepaths:
    df=pd.concat([df,extract(filepath)])


# In[58]:


df


# In[59]:


df=df.dropna()


# In[60]:


df.reset_index(drop=True)


# In[61]:


df=df.iloc[:,[6,7,8,9,10,1,2,3,4,5]]


# In[62]:


df.to_excel('output/all_data02.xlsx',index=False)


# In[63]:


members=df['発行者'].unique()


# In[64]:


member=members[0]


# In[65]:


_df=df[df['発行者']==member]


# In[66]:


_df['金額'].sum()


# In[67]:


companies=_df['企業名'].unique()
companies


# In[83]:


companies[0]


# In[87]:


_df[_df['企業名']==companies[0]]['金額'].sum()


# In[88]:


tot_earnings=_df['金額'].sum()

def gokei():
    df = pd.DataFrame()
    for filepath in filepaths:
        df=pd.concat([df,extract(filepath)])
    df=df.dropna()
    df=df.reset_index(drop=True)
    df=df.iloc[:,[6,7,8,9,10,1,2,3,4,5]]
    members=df['発行者'].unique()
    for member in members:
        for hakko in df['発行者']:
            _df=df[df['発行者']==member]
            all_sum=_df['金額'].sum()
            return all_sum
                for kigyo in _df['企業名']:
                    small_sum=_df[_df['企業名']==companies[0]]['金額'].sum()
                    return small_sum
                
# In[92]:


pd.DataFrame({'担当者':member,'企業名':'全体','金額':tot_earnings},index=[0])


# In[95]:


company=companies[0]


# In[97]:


earnings=_df[_df['企業名']==companies[0]]['金額'].sum()


# In[ ]:





# In[99]:


pd.DataFrame({'担当者':member,'企業名':company,'金額':earnings},index=[1])


# In[100]:


{'担当者':member,'企業名':'全体','金額':tot_earnings}


# In[102]:


dict(企業名=company,金額=earnings)


# In[107]:


total_res =[]
for member in members:
    member=members[0]
    _df=df[df['発行者']==member]
    companies=_df['企業名'].unique()

    tot_earnings=_df['金額'].sum()
    total_res.append(dict(担当者=member,企業名='全体',金額=tot_earnings))
    
    for company in companies:
        earnings=_df[_df['企業名']==companies[0]]['金額'].sum()
        total_res.append(dict(企業名=company,金額=earnings))


# In[108]:


total_res


# In[109]:


pd.DataFrame(total_res,columns=['担当者','企業名','金額'])


# In[ ]:




