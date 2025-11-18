#!/usr/bin/env python
# coding: utf-8

# # Module 3: Data Structures Assignments
# ## Lesson 3.4: Dictionaries

# In[2]:


# 1: Creating and Accessing Dictionaries
# Create a dictionary with the first 10 positive integers as keys and their squares as values. Print the dictionary.
# d1={1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}
d1={x:x*x for x in range(1,11)}
print(d1,type(d1))


# In[15]:


#: Accessing Dictionary Elements
# Print the value of the key 5 and the keys of the dictionary created in Assignment 1
d1={x:x*x for x in range(1,11)}

print(d1[5])
for ks in d1:
    print(ks)


# In[18]:


# Qno 3: Dictionary Methods -->
# Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1. Print the modified dictionary.

d1.update({11:121})
print(d1)
d1.pop(1)
print(d1)


# In[22]:


# Qno 4: Iterating Over Dictionaries
# Iterate over the dictionary created in Assignment 1 and print each key-value pair.
d1={x:x*x for x in range(1,11)}
for k,v in d1.items():
    print(k,"===>",v)


# In[23]:


# Qno 5: Dictionary Comprehensions
# Create a new dictionary containing the cubes of the first 10 positive integers using a dictionary comprehension. Print the new dictionary.
d2={x:x**3 for x in range(1,11)}
print(d2,type(d2))


# In[25]:


# Qno 6: Merging Dictionaries
# Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, and another with keys as the next 5 positive integers and values as their squares. Merge these dictionaries into a single dictionary and print it.
d3={x:x**2  for x in range(1,6) }
d4={x:x**2 for x in range(6,11)}
d3.update(d4)
print(d3,type(d3))


# In[34]:


# 7: Nested Dictionaries
# Create a nested dictionary representing a student with keys 'name', 'age', 'grades', where 'grades' is another dictionary with keys 'math', 'science', and 'english'. Print the nested dictionary.
d5={'name':"madhav",'Age':24,'grades':{'math':'O','Science':'A+','English':'A'}}
print(d5)
for k,v in d5['grades'].items():
    print(k,"==>",v)


# In[35]:


# 8: Dictionary of Lists
# Create a dictionary where the keys are the first 5 positive integers and the values are lists containing the first 5 multiples of the key. Print the dictionary.
d6={x:[x*i for i in range(1,6)] for x in range(1,6)}
print(d6)


# In[36]:


# 9: Dictionary of Tuples
# Create a dictionary where the keys are the first 5 positive integers and the values are tuples containing the key and its square. Print the dictionary.
d7={x:(x,x**2) for x in range(1,6)}
print(d7)


# In[63]:


# 10: Dictionary and List Conversion
# Create a dictionary with the first 5 positive integers as keys and their squares as values. Convert the dictionary to a list of tuples and print it.
d8={x:x**2 for x in range(1,6)}
print(d8)
d9=list(d8)
print(d9)


# In[78]:


# Qno 11: Dictionary Filtering
# Create a dictionary with the first 10 positive integers as keys and their squares as values. Create a new dictionary containing only the key-value pairs where the key is even. Print the new dictionary.
d10={x:x**2 for x in range(1,11)}
print(d10)
d11={}
# d12={x:x**2 for x in range(1,11) if(x%2==0)}
# d12
for k,v in d10.items():
    if(k%2==0):
        d11.update({k:v})
print(d11)


# In[85]:


# 12: Dictionary Key and Value Transformation
# Create a dictionary with the first 5 positive integers as keys and their squares as values. 
#Create a new dictionary with keys and values swapped. Print the new dictionary.
d13={x:x**2 for x in range(1,6)}
print(d13)

d14={x**2:x for x in range(1,6)}
print(d14)


# In[100]:


# Qno 13: Default Dictionary
# Create a default dictionary where each key has a default value of an empty list. Add some elements to the lists and print the dictionary.
#doubt


# In[98]:


# 14: Counting with Dictionaries
# Write a function that takes a string and returns a dictionary with the count of each character in the string. Print the dictionary.
s1=input("enter a string")
def dictfun(s):
    d16=dict()
    for i in s:
        d16.update({i:s.count(i)})
    return d16
print(dictfun(s1))


# In[ ]:


# 15: Dictionary and JSON
# Create a dictionary representing a book with keys 'title', 'author', 'year', and 'genre'. Convert the dictionary to a JSON string and print it.
#Topic is not Discussed

