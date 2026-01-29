#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 Find the mean of first 10 odd integers?
import numpy as np
import pandas as pd
import statistics as st
a=list(2*i+1 for i in range(10))
df=pd.DataFrame(a)
df=df.rename(columns={0:"x"})

μ=df["x"].mean()
df["μ"]=μ
df["x-μ"]=df["x"]-df["μ"]
df["[x-μ]^2"]=df["x-μ"]**2
print(df)
print("\ntotal sum:",df["x"].sum())
print("\nMean of first 10 odd numbers :",μ)
df
# # x̄

# x


# In[2]:


#2. What is the median of the following data set?
# data=[32.6,21,10,8,11,12,36,17,16,15,18,40,24,21,23,24,24,29,16,32,31,10,30,35,32,18,39,12,20]
data=[32.6,21,10,8,11,12,36,17,16,15,18,40,24,21,23,24,24,29,16,32,31,10,30,35,32,18,39,12,20]
df=pd.DataFrame(data)

df=df.rename(columns={0:"x"})
print(df)
print("median\t:",df["x"].median())
df


# In[3]:


#3.Identify the mode for the following data set:
data=[21,19,62,21,22,22,66,28,66,48,79,59,28,62,63,63,48,66,59,66,94,79,19,94]
df=pd.DataFrame(data)
df=df.rename(columns={0:"x"})
print(df["x"].mode)


# In[4]:


#4 given a Dataset, calculate the mean,median,and mode.Interpret the results adn determine which measure of central tendency is most appropriate for the dataset
#Test Scores of 10 Students:[65,70,75,80,85,90,95,100,105,110]
df1=pd.DataFrame([65,70,70,80,85,90,95,100,105,110])
print(df1.mean())
print(df1.median())
print(df1.mode())


# In[18]:


#5.Calculate the the mean,median,and mode for the following dataset. Then add an outlier value of 100 and 
# recalculate the measures.Discuss how the outlier affects the mean compared to the median and mode
# originalDataset:[50,52,53,55,57,60,62,64,65]
# Modified Dataset with Outlier:[50,52,53,55,57,60,62,64,65,100]
df1=pd.DataFrame([50,52,53,55,57,60,62,64,65])
df1
print("mean of the data is \n",df1.mean())
print("mode of the data is \n",df1.mode())
print("median of the data is \n",df1.median())
print(df1)
df1=df1.rename(columns={0:"x"})
df1.loc[9,"x"]=100
print("====>\n",df1)
print("mean of the data is \n",df1.mean())
print("mode of the data is \n",df1.mode())
print("median of the data is \n",df1.median())


# In[ ]:





# In[ ]:




