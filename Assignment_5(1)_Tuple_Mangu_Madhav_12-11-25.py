#!/usr/bin/env python
# coding: utf-8

# In[1]:


##1:Creating and Accessing Tuples
#Create a tuple with the first 10 positive integers. Print the tuple.
t=(1,2,3,4,5,6,7,8,9,10)
print(t,type(t))


# In[2]:


#2: Accessing Tuple Elements
#Print the first, middle, and last elements of the tuple created in Assignment 1.
t=(1,2,3,4,5,6,7,8,9,10)
l=len(t)
print(t[0],t[l//2],t[l-1])


# In[3]:


#3: Tuple Slicing
#Print the first three elements, the last three elements, and the elements from index 2 to 5 of the tuple created in Assignment 1.
t=(1,2,3,4,5,6,7,8,9,10)
print(t[0:3],t[-1:-4:-1],t[2:5])


# In[4]:


###  4: Nested Tuples
#Create a nested tuple representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
t=((1,2,3),(4,5,6),(7,8,9))
for i,val1 in enumerate(t):
    for j,val2 in enumerate(t):
        print(t[i][j], end=" ")
    print("\n")
print("The element at the second row and third column:",t[1][2])


# In[5]:


###  5: Tuple Concatenation
#Concatenate two tuples: (1, 2, 3) and (4, 5, 6). Print the resulting tuple.
t=(1,2,3)
t2=(4,5,6)
t3=t+t2
print(t3)


# In[6]:


## 6: Tuple Methods
#Create a tuple with duplicate elements and count the occurrences of an element. Find the index of the first occurrence of an element in the tuple.
t1=(20,10,30,40,10,50,60,10,70)
print("count:",t1.count(10))
print("index:",t1.index(10))


# In[7]:


###  7: Unpacking Tuples
#Create a tuple with 5 elements and unpack it into 5 variables. Print the variables.
t=(1,2,3,4,5)
a,b,c,d,e=t
print(a,b,c,d,e)


# In[8]:


## 8: Tuple Conversion
##Convert a list of the first 5 positive integers to a tuple. Print the tuple.
l1=[1,2,3,5,6]
t1=tuple(l1)
print("tuple",t1)


# In[9]:


## 9: Tuple of Tuples
#Create a tuple containing 3 tuples, each with 3 elements. Print the tuple of tuples.
t1=((1,2,3),(4,5,6),(7,8,9))
print(t1)


# In[10]:


###  10: Tuple and List
#Create a tuple with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a tuple. Print the resulting tuple.
t1=(1,2,3,4,5)
l1=list(t1)
l1.append(6)
t1=tuple(l1)
print(t1)


# In[11]:


## 11: Tuple and String
#Create a tuple with the characters of a string. Join the tuple elements into a single string. Print the string.
#############################
t=('M','A','D','H','A','V')
s="".join(t)
print(s)


# In[12]:


## 12: Tuple and Dictionary
#Create a dictionary with tuple keys and integer values. Print the dictionary.
####################

x={(1):12,(3):50}
print(x,type(x))


# In[13]:


## 13: Nested Tuple Iteration
#Create a nested tuple and iterate over the elements, printing each element.
##################
t=((1,(2,3),(4,5,6),(7,8,9)))
for i,val in enumerate(t):
    for j,val in enumerate(t):
        print(t[1:3][j])
    


# In[14]:


###  14: Tuple and Set
#Create a tuple with duplicate elements. Convert it to a set to remove duplicates and print the resulting set.
t1=(10,20,30,20,50,20,40,30,20,45,50)
s1=set(t1)
print(s1)


# In[24]:


###  15: Tuple Functions
#Write functions that take a tuple and return the minimum, maximum, and sum of the elements. Print the results for a sample tuple.
t=(10,3,56,20,15,45)
# print(sum(t))
def Minimun(t1):
    return min(t1)
  
def Maximum(t1):
    return max(t1)

def sumoft(t1):
    return sum(t1)  

    
print("tuple:",t)
print("Minimum value of the tuple is:",Minimun(t))
print("Maximum value of the tuple is:",Maximum(t))
print("sum of the value of the tuple is: ",sumoft(t))
    


# In[ ]:




