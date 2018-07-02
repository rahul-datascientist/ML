


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')


train=pd.read_csv('../data/raw/Train_UWu5bXk.csv')
test=pd.read_csv('../data/raw/Test_u94Q5KV.csv')


# In[3]:


train['source']='train'
test['source']='test'
data = pd.concat([train, test],ignore_index=True,sort=True)
print(train.shape, test.shape, data.shape)


# In[4]:


data.info()


# In[5]:


data.apply(lambda x:sum(x.isnull()))


# In[6]:


data.describe(include='all')


# In[7]:


data.describe()


# In[8]:


data.apply(lambda x:len(x.unique()))


# In[9]:


data.dtypes


# In[10]:


categorical_columns = [x for x in data.dtypes.index if data.dtypes[x]=='object']


# In[11]:


categorical_col = [x for x in  data.dtypes.index if data.dtypes[x]=='object']
categorical_col = [x for x in  categorical_col if x not in ['Item_Identifier','Outlet_Identifier','source']] 


# In[12]:


data['Item_Fat_Content'].value_counts()


# In[13]:


for col in categorical_col:
    print('Frequency of Category for variable %s'%col)
    print(data[col].value_counts())


# ## Data Cleaning

# In[14]:


from sklearn.preprocessing import Imputer


# In[15]:


#Determine the average weight per item:
item_avg_weight = data.pivot_table(values='Item_Weight', index='Item_Identifier')


# In[16]:


miss_bool =data['Item_Weight'].isnull()


# In[17]:


#Impute data and check #missing values before and after imputation to confirm
print ('Orignal #missing: %d'% sum(miss_bool))


# In[20]:


data.loc[miss_bool,'Item_Weight'] = data.loc[miss_bool,'Item_Identifier'].apply(lambda x:item_avg_weight[x])

