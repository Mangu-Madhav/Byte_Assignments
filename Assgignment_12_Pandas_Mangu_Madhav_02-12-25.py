#!/usr/bin/env python
# coding: utf-8

# In[76]:


# Assignment: Data Selection, Modification, and Operations in Pandas

# Part A: Data Selection

# 1.Create a DataFramedf with 10 rows and 5 columns containing random integers from 1 to 100.
# a. Select the value at the 3rd row and 2nd column.
# b. Select all rows but only columns ['A', 'C'].
# c. Select multiple rows [2, 4, 7] and all columns.
# d. Select rows [1, 3, 5] and columns ['B', 'D'].

import numpy as np
import pandas as pd
a=np.random.randint(1,101,50)
print(a)
b=a.reshape(10,5)
print(b)
df=pd.DataFrame(b,columns=["A","B","C","D","E"])
print("DataFrame:\n",df)
# a
print("The value at the 3rd row and 2nd column:",b[2,1])
print("all rows but only columns ['A', 'C']\n",df.loc[:,["A","C"]])
print("multiple rows [2, 4, 7] and all columns\n",df.iloc[[2,4,7],:])
print("rows [1, 3, 5] and columns ['B', 'D']\n",df.loc[[1,3,5],["B","D"]])


# In[75]:


# Part B: Data Modification
# 2.Using the same DataFramedf:
# a. Add a new column E with values [10,20,...] corresponding to row numbers.
# b. Remove the column C.
# c. Replace all values in column B with 0.
# d. Replace row 4 with [1,2,3,4,5].
# e. Replace rows [2,5] in column A with 99.
# f. Replace rows [0,1,2] with [ [1,1,1,1,1], [2,2,2,2,2], [3,3,3,3,3] ].
# df=df.drop(index="B")
df["E"]=[10,20,30,40,50,60,70,80,90,100]
print(df)
print("\nDataFrame After deleting column C\n",df.drop(columns="C"))
df.loc[:,"B"]=0
print("all values in column B with 0\n",df)
df.loc[3,:]=[1,2,3,4,5]
print("Replaced row 4 with [1,2,3,4,5]\n",df)
df.loc[[2,5],"A"]=99
print("Replaced rows [2,5] in column A with 99\n",df)
df.loc[[0,1,2]]=[[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3]]
print("Replace rows [0,1,2] with [ [1,1,1,1,1], [2,2,2,2,2], [3,3,3,3,3] ]\n",df)
df=df.drop(columns="B")
df


# In[ ]:





# In[ ]:




