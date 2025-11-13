#!/usr/bin/env python
# coding: utf-8

# In[73]:
#add 10 to all elements in the list l1=[10,11,13,14]

l1=[10,11,13,14]
print("list 1",l1)
l2=[]
for i,val in enumerate(l1):
    l2.append(val+10)
print("list-2",l2)


# In[72]:
#store the resultant of l1+l2 in l3 l1=[10,11,13,14] , l2=[5,6,7,8,9]

l1=[10,11,13,14]
l2=[5,6,7,8,9]
print("list-1",l1)
print("list-2",l2)                    
l3=l2
for i,val in enumerate(l1):
        l3.insert(i,val+l2[i])
        del l3[i+1]
print("list-3",l3)


# In[60]:
#Extract the elements >=40 in the given list l1=[10,11,23,45,78,90,42,41]

l1=[10,11,23,45,78,90,42,41]
print("list-1",l1)
l2=[]
for i,val in enumerate(l1):
    if(val>=40):
        l2.append(val)
print("list-2",l2)


# In[64]:
#Extract the values of the indices [0,1,5,7] from the list l1=[10,20,15,45,89,90,11,34]

l1=[10,20,15,45,89,90,11,34]
print("list-1",l1)
l2=[]
for i,val in enumerate(l1):
    if(val%2==0):
        l2.append(val)
print("list-2",l2)


# In[ ]:




