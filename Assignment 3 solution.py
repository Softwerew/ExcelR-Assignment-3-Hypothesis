#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm


# In[2]:


# Q1 cutlets hypothesis
# Null Hypothesis=No significant difference in the diameter of the cutlet b/w 2 units
# Alternate Hypothesis=There is significant difference in the diameter of the cutlet b/w 2 units


# In[3]:


data=pd.read_csv(r"C:\Users\Lovely_Ray\Desktop\data science\Assignment 3\Cutlets.csv")


# In[4]:


data


# In[6]:


unitA=pd.Series(data.iloc[:,0])
unitA


# In[7]:


unitB=pd.Series(data.iloc[:,1])
unitB


# In[9]:


pvalue=stats.ttest_ind(unitA,unitB)
pvalue


# In[10]:


# as alpha=0.05(at 5% significance level), we compare p value with it.
# Clearly p value @ 0.47 is greater than alpha, hence we accept null hypothesis.


# In[11]:


# Q2 LabTat hypothesis
# Null Hypothesis=There is no difference in avg TAT among the different laboratories
# Alternate Hypothesis=There is significant difference in avg TAT among the different laboratories.


# In[12]:


Labdata=pd.read_csv(r"C:\Users\Lovely_Ray\Desktop\data science\Assignment 3\LabTat.csv")


# In[13]:


Labdata.head()


# In[14]:


lab1=pd.Series(Labdata.iloc[:,0])
lab1


# In[15]:


lab2=pd.Series(Labdata.iloc[:,1])
lab2


# In[16]:


lab3=pd.Series(Labdata.iloc[:,2])
lab3


# In[17]:


lab4=pd.Series(Labdata.iloc[:,3])
lab4


# In[19]:


import scipy.stats as stats


# In[20]:


stats.f_oneway(lab1,lab2,lab3,lab4)


# In[ ]:


# as alpha=0.05(at 5% significance level), we compare p value with it.
# Clearly the p value here is far less than alpha, hence we reject null hypothesis.


# In[23]:


# Q3 Buyer Ratio hypothesis
# Null Hypothesis=male female buyer ratios are similar across regions
# Alternate Hypothesis=not all ratios are equal


# In[24]:


import pylab


# In[25]:


data3=pd.read_csv(r"C:\Users\Lovely_Ray\Desktop\data science\Assignment 3\BuyerRatio.csv")


# In[26]:


data3


# In[27]:


data_final=data3.drop(['Observed Values'],axis=1)


# In[28]:


data_final


# In[29]:


from scipy.stats import chi2_contingency


# In[33]:


obs_data=np.array([[50,142,131,70],[435,1523,1356,750]])
obs_data


# In[34]:


chi2_contingency(obs_data)


# In[35]:


# p value is 0.66, which is greater than alpha value. Hence we accept null hypothesis.


# In[36]:


# Q4 Customer Order Form hypothesis
# Null Hypothesis=The defective % doesn't vary by centres
# Alternate Hypothesis=The defective % varies by centres


# In[39]:


data=pd.read_csv(r"C:\Users\Lovely_Ray\Desktop\data science\Assignment 3\CostomerOrderForm.csv")


# In[40]:


data.head()


# In[42]:


data.Phillippines.value_counts()


# In[43]:


data.Indonesia.value_counts()


# In[44]:


data.Malta.value_counts()


# In[45]:


data.India.value_counts()


# In[46]:


obs_data=np.array([[271,267,269,280],[29,33,31,20]])
obs_data


# In[47]:


chi2_contingency(obs_data)


# In[ ]:


# p value is 0.27, which is greater than alpha value. Hence we accept null hypothesis.

