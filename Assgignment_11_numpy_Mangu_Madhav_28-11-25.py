#!/usr/bin/env python
# coding: utf-8

# # Module: NumPy Assignments

# In[43]:


### Assignment 1: Array Creation and Manipulation
# 1. Create a NumPy array of shape (5, 5) filled with random integers between 1 and 20. Replace all the elements in the third column with 1.
import numpy as np
a=np.random.randint(1,21,[5,5])
print(a)
a[:,2]=1
print("after replace of all elements in 3rd column with 1:\n",a)


# In[44]:


# 2. Create a NumPy array of shape (4, 4) with values from 1 to 16. Replace the diagonal elements with 0.
b=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
c=np.array(b)
for i in range(0,4):
    for j in range(0,4):
        if i==j:
            c[i][j]=0
print(c)
print(c.shape)


# In[45]:


# Assignment 3: Array Operations
# 1. Create two NumPy arrays of shape (3, 4) filled with random integers. Perform element-wise addition, subtraction, multiplication, and division.
a=np.random.randint(1,13,[3,4])
print(a)
print("addition:\n",a+10)
print("subtraction\n",a-5)
print("multiplication\n",a*3)
print("division\n",a/3)


# In[46]:


# 2. Create a NumPy array of shape (4, 4) with values from 1 to 16. Compute the row-wise and column-wise sum.
a=np.arange(1,17)
print("elements of a:",a)
b=a.reshape(4,4)
print(b)
for i in range(0,4):
    sum=0
    sum1=0
    for j in range(0,4):
        sum=sum+b[i,j]
        sum1=sum1+b[j,i]
    print(f' row-wise sum of row {i} is {sum}')
    print(f' column-wise sum of col {i} is {sum1}')


# In[49]:

# Assignment 7: Advanced Array Manipulation
# # 1. Create a NumPy array of shape (3, 3) with values from 1 to 9. Reshape the array to shape (1, 9) and then to shape (9, 1).
a=np.arange(1,10)
print(a)
b=a.reshape(3,3)
print("3x3 arrya\n",b)
c=b.reshape(1,9)
print("1x9 array:\n",c)
d=b.reshape(9,1)
print("9x1 arrya:\n",d)


# In[51]:


# 2. Create a NumPy array of shape (5, 5) filled with random integers. Flatten the array and then reshape it back to (5, 5).
a=np.random.randint(1,20,[5,5])
print("5x5 arrya:\n",a)
b=a.ravel()
print("Flatten array is\n",b)
c=b.reshape(5,5)
print("reshape of 5x5 is:",c)


# In[52]:


# Assignment 8: Fancy Indexing and Boolean Indexing
# 1. Create a NumPy array of shape (5, 5) filled with random integers. Use fancy indexing to extract the elements at the corners of the array.
a=np.random.randint(1,20,[5,5])
print(a)
print("elements at corner of the matrix:\n",a[0,0],a[0,4],a[4,0],a[4,4])


# In[42]:


# 2. Create a NumPy array of shape (4, 4) filled with random integers. Use boolean indexing to set all elements greater than 10 to 10.
a=np.random.randint(1,20,[4,4])
print(a)
for i in range(0,4):
    for j in range(0,4):
        if a[i,j]>10:
            a[i,j]=10
print("After replacing all the elements greater than 10 to 10 is \n",a)

