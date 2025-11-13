#!/usr/bin/env python
# coding: utf-8

# In[1]:


## 1: Creating and Accessing Sets
#Create a set with the first 10 positive integers. Print the set.
s={1,2,3,4,5,6,7,8,9,10}
print(s,type(s))


# In[3]:


###  2: Adding and Removing Elements
#Add the number 11 to the set created in Assignment 1. Then remove the number 1 from the set. Print the modified set.
s={1,2,3,4,5,6,7,8,9,10}
s.add(11)
print(s,type(s))
s.remove(1)
print(s,type(s))


# In[10]:


### Assignment 3: Set Operations
#Create two sets: one with the first 5 positive integers and another with the first 5 even integers. Perform and print the results of union, intersection, difference, and symmetric difference operations on these sets.
####doubt
s1={1,2,3,4,5}
s2={0,2,4,6,8}
all=s1.union(s2)
print(all,type(all))
inter=s1.intersection(s2)
print(inter,type(inter))
diff=s1.difference(s2)
print(diff,type(diff))


# In[92]:


### Assignment 4: Set Comprehensions
#Create a new set containing the squares of the first 10 positive integers using a set comprehension. Print the new set.
s={1,2,3,4,5,6,7,8,9,10}
s2=set()
for i,val in enumerate(s):
    s2.add(val*val)
print(s2)


# In[85]:


###  5: Filtering Sets
#Create a new set containing only the even numbers from the set created in Assignment 1 using a set comprehension. Print the new set.
s={1,2,3,4,5,6,7,8,9,10}
s2=set()
for i,val in enumerate(s):
    if(val%2==0):
        s2.add(val)
print(s2)


# In[4]:


### Assignment 6: Set Methods
#Create a set with duplicate elements and remove the duplicates using set methods. Print the modified set.
s1={10,20,30,10,40,10}
s2=set()
s3=s2.union(s1)
print(s3)


# In[6]:


## 7: Subsets and Supersets
#Create two sets: one with the first 5 positive integers and another with the first 3 positive integers. Check if the second set is a subset of the first set and if the first set is a superset of the second set. Print the results.
##skip
s1={1,2,3,4,5}
s2={1,2,3}
print(s2.issubset(s1))
print(s1.issuperset(s2))


# In[46]:


##  8: Frozenset
#Create a frozenset with the first 5 positive integers. Print the frozenset.
##skipped


# In[49]:


## 9: Set and List Conversion
#Create a set with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a set. Print the resulting set.
s1={1,2,3,4,5}
print(s1,type(s1))
l1=list(s1)
l1.append(6)
print("list:",l1,type(l1))
s1=set(l1)
print("set",s1,type(s1))


# In[55]:


## 10: Set and Dictionary
#Create a dictionary with set keys and integer values. Print the dictionary.
d={1:100,2:200, 3:300, 4:400}
print(d,type(d))


# In[59]:


## 11: Iterating Over Sets
#Create a set and iterate over the elements, printing each element.
s={100,"Madhav",True,2+3j}
print("set:",s,type(s))
for val in enumerate(s):
    print(val)
    


# In[86]:


##  12: Removing Elements from Sets
#Create a set and remove elements from it until it is empty. Print the set after each removal.
s={100,"Madhav",True,2+3j}
print(s,type(s))
while(s!=set()):
    s.pop()
    print(s)


# In[93]:


## 14: Set Membership Testing
#Create a set and test if certain elements are present in the set. Print the results.
##skip topic



# In[83]:


## 15: Set of Tuples
#Create a set containing tuples, where each tuple contains two elements. Print the set.
s={(1,2),("madhav",True),(2+3j,44.5)}
print(s,type(s))


# In[ ]:




