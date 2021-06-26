#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter("ignore")


# In[2]:


os.chdir('C:\oppty')



# In[4]:


df = pd.read_csv('oppty.csv', encoding='cp949')


# In[5]:


df.head(3)


# In[6]:


y_col = 'Result'
x_col = ['NAME', 'SUM_WIN_PROB','INVST_STG_CD', 'X_OPTY_TYPE','MARKET_CLASS_CD', 'CREATED', 'CLOSE_DT', 'BEF_1M_SLNG_AMT', 'CIRCUIT_NUM', 'X_CODE', 'X_TEXT','SLNG_AMT', 'PURE_PRFIT_AMT', 'MIN_CH_DT', 'MAX_CH_DT']


# In[7]:


df.describe(include='all')


# In[8]:


df.head(5)


# In[9]:


df['X_STATUS_CD'].value_counts()


# In[10]:


odf = df.loc[df['X_STATUS_CD'].isin(['Win', 'Loss'])]


# In[11]:


odf['Result'] = odf['X_STATUS_CD'].apply(lambda x:  1 if x=='Win' else 0)


# In[12]:


odf.describe(include='all')


# In[13]:


odf['Result'].value_counts(), odf['X_STATUS_CD'].value_counts()


# In[14]:


odf.CREATED.min(), odf.CREATED.max()


# In[15]:


odf['CREATED_DATE'] = pd.to_datetime(odf.CREATED, format='%Y%m%d')


# In[16]:


odf.head(3)


# In[17]:


odf.CREATED_DATE.hist(xlabelsize=10)


# ### Train_Test Set 분리

# In[18]:


train = odf.loc[odf.CREATED_DATE < '20200901' ]
test = odf.loc[odf.CREATED_DATE >= '20200901']


# In[19]:


odf.shape,  train.shape, test.shape


# In[20]:


train.CREATED_DATE.hist(xlabelsize=8,  figsize = (10, 5))


# In[21]:


test.CREATED_DATE.hist(xlabelsize = 8, figsize = (10, 5))


# In[22]:


simple_x_col = ['NAME', 'INVST_STG_CD', 'X_OPTY_TYPE','MARKET_CLASS_CD', 'BEF_1M_SLNG_AMT', 'CIRCUIT_NUM']


# In[23]:


odf[simple_x_col].describe(include='all')


# In[24]:


train_x = train[simple_x_col]


# In[25]:


train_x.set_index('NAME', inplace = True)


# In[26]:


train_x.head(3)


# In[27]:


train_x = pd.get_dummies(train_x)


# In[28]:


train_x.info()


# In[29]:


train_x.describe()


# In[30]:


train_y = train[y_col]


# In[31]:


train_y.shape, type(train_y)


# In[32]:


train_y.value_counts()


# In[33]:


##train_y[train_y.isin(['Drop', 'Proposal Reject'])] = 'Loss'


# In[34]:


from sklearn.ensemble import RandomForestClassifier


# In[35]:


classifier = RandomForestClassifier(n_estimators=500)


# In[36]:


classifier.fit(train_x, train_y)


# In[37]:


test_x = test[simple_x_col]
test_x.set_index('NAME', inplace = True)


# In[38]:


test_y = test[y_col]
#train_y[train_y.isin(['Drop', 'Proposal Reject'])] = 'Loss'


# In[39]:


test_x  = pd.get_dummies(test_x)


# In[40]:


score = classifier.score(test_x, test_y)
print(score)


# In[41]:


train_x.head(3)


# ### Scaling

# In[42]:


from sklearn import preprocessing


# In[43]:


scaler = preprocessing.StandardScaler().fit(train_x)


# In[44]:


train_x_scaled = scaler.transform(train_x)


# In[45]:


test_x_scaled = scaler.transform(test_x)


# In[46]:


classifier.fit(train_x_scaled, train_y)


# In[47]:


score = classifier.score(test_x_scaled, test_y)
print(score)


# ### Feature 중요성 보기

# In[48]:


classifier.feature_importances_


# In[49]:


plt.barh(test_x.columns, classifier.feature_importances_)


# In[50]:


test_predict = classifier.predict(test_x_scaled)


# In[51]:


test_predict_proba = classifier.predict_proba(test_x_scaled)


# In[56]:


test_predict[:20]


# In[57]:


test_y[:20]


# In[58]:


type(test_predict), type(test_y)


# In[59]:


test_predict = pd.Series(test_predict)


# In[94]:


test_y = test_y.reset_index()


# In[95]:


test_y_compare = pd.concat([test_y, test_predict], axis = 1, ignore_index = True)


# In[118]:


test_y_compare.columns = ['ID', 'REAL', 'PREDICT']


# In[119]:


test_y_compare.describe()


# In[122]:


test_y_compare['NAME'] = test_x.index


# In[129]:


test_y_compare.set_index('NAME', inplace = True)


# In[130]:


test_verify = pd.concat([test_y_compare, test_x], axis = 1)


# In[136]:


test_verify.loc[test_verify.REAL == test_verify.PREDICT , 'MATCH'] = 'MATCH'
test_verify.loc[test_verify.REAL != test_verify.PREDICT , 'MATCH'] = 'UNMATCH'


# In[138]:


test_verify.groupby('MATCH').count()


# In[155]:


old_customer  = test_verify.loc[test_verify['BEF_1M_SLNG_AMT']> 0,'MATCH'].value_counts()
new_customer  = test_verify.loc[test_verify['BEF_1M_SLNG_AMT'] == 0,'MATCH'].value_counts()


# In[168]:


new_old= pd.concat([old_customer, new_customer], axis = 1, keys =['OLD', 'NEW'])


# In[171]:


new_old = new_old.T


# In[173]:


new_old['match_rate'] = new_old['MATCH']/(new_old['MATCH']+new_old['UNMATCH'])


# In[187]:


new_old.index.name = 'customer_type'


# In[188]:


new_old


# In[198]:


new_old['match_rate'].plot(kind='bar')


# In[201]:


import pickle


# In[202]:


model_file =  'opty_randomforest.sav'


# In[204]:


pickle.dump(classifier, open(model_file, 'wb'))


# In[206]:


pwd


# In[207]:


scaler_file = 'opty_scaler.sav'


# In[208]:


pickle.dump(scaler,open(scaler_file, 'wb'))


# In[209]:


loaded_model = pickle.load(open(model_file, 'rb'))


# In[213]:


test_y.set_index('index', inplace = True)
loaded_model.score(test_x_scaled, test_y)


# In[249]:


type(test_x_scaled)
loaded_scaler = pickle.load(open(scaler_file, 'rb'))
sample_test = pd.DataFrame({'BEF_1M_SLNG_AMT': 816574, 'CIRCUIT_NUM': 40, 'INVST_STG_CD_A': 1,'INVST_STG_CD_B': 0,
               'X_OPTY_TYPE_A': 1, 'X_OPTY_TYPE_B':0, 'MARKET_CLASS_CD_201':0,'MARKET_CLASS_CD_402': 0, 'MARKET_CLASS_CD_701':1,
                           'MARKET_CLASS_CD_901':0, 'MARKET_CLASS_CD_201':0, 'MARKET_CLASS_CD_402':0, 'MARKET_CLASS_CD_404': 0,
                            'MARKET_CLASS_CD_701':1,'MARKET_CLASS_CD_901':0, 'MARKET_CLASS_CD_G01':0}, index=[0])

#sample_test = sample_test.reshape(-1, 1)
#sample_test[0:10]
#scaled_sample = loaded_scaler.transform(sample_test)


# In[250]:


sample_test.head(3)


# In[251]:


scaled_sample = loaded_scaler.transform(sample_test)


# In[242]:


test_x.head(3)
# %%
