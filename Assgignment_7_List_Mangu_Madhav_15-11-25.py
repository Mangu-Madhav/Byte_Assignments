#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##  1: Creating and Accessing Lists
#Create a list of the first 20 positive integers. Print the list.
l1=list(range(1,21))
print(l1)


# In[5]:


## 2: Accessing List Elements
#Print the first, middle, and last elements of the list created in Assignment 1.
l1=list(range(1,21))
print("first element",l1[0])
print("middle element",l1[len(l1)//2])
print("last element",l1[-1])


# In[11]:


## 3: List Slicing
#Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in Assignment 1.
l1=list(range(1,21))
print("first 5 elements are:",l1[0:6])
print("last 5 elements are:",l1[-5::+1])
print("elements from index 5 to 15 are",l1[5:16])


# In[18]:


##  4: List Comprehensions
#Create a new list containing the squares of the first 10 positive integers using a list comprehension. Print the new list.
l=list(range(1,11))
l2=list()
for i,val in enumerate(l):
    l2.append(val**2)
print(l2)


# In[19]:


### 5: Filtering Lists
#Create a new list containing only the even numbers from the list created in Assignment 1 using a list comprehension. Print the new list.
l1=list(range(1,21))
l2=[]
for i,val in enumerate(l1):
    if(val%2==0):
        l2.append(val)
print(l2)


# In[32]:


##  6: List Methods
#Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from the list and print the modified list.
l1=[1,385,38,356,7,2,7,38,378,3,6,5,2,7,12,45,76,0]
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)


# In[41]:


## 7: Nested Lists
#Create a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
l=[[1,2,3],[4,5,6],[7,8,9]]
for i,val in enumerate(l):
    for j,val in enumerate(l):
        print(l[i][j],end=" ")
    print("\n")
print("element at the second row and third column:",l[1][2])


# In[39]:


###  8: List of Dictionaries
#Create a list of dictionaries where each dictionary represents a student with keys 'name' and 'score'. Sort the list of dictionaries by the 'score' in descending order and print the sorted list.
##doubt
l=[{"madhav":100},{"X":90},{"Y":80}]
print(l)


# In[ ]:


## 9: Matrix Transposition
#Write a function that takes a 3x3 matrix (nested list) as input and returns its transpose. Print the original and transposed matrices.
##doubt
r,c=int(input("enter row  size of the matrix")),int(input("enter the column size of the matrix"))
l=[]
for i in range(0,r):
    for j in range(0,c):
        l[i][j].append(input())
print(l)

# print("Original Matrix")
# for i,val in enumerate(l):
#     for j,val in enumerate(l):
#         print(l[i][j],end=" ")
#     print("\n")

# print("Transpose of the Matrix is")
# for i,val in enumerate(l):
#     for j,val in enumerate(l):
#         print(l[j][i],end=" ")
#     print("\n")


# In[ ]:


##  10: Flattening a Nested List
#Write a function that takes a nested list and flattens it into a single list. Print the original and flattened lists.


# In[52]:


### 11: List Manipulation
#Create a list of the first 10 positive integers. Remove the elements at indices 2, 4, and 6, and insert the element '99' at index 5. Print the modified list.
l1=list(range(0,10))

l1.remove(l1[2])
l1.remove(l1[4])
l1.remove(l1[6])
l1.insert(5,99)
print(l1)



# In[ ]:


## Assignment 12: List Zipping
#Create two lists of the same length. Use the `zip` function to combine these lists into a list of tuples and print the result.
#Topic not covered


# In[5]:


##  13: List Reversal
#Write a function that takes a list and returns a new list with the elements in reverse order. Print the original and reversed lists.
#
l=[1,2,3,4,5,6,8,19]
print("original list:",l)

def listfun(l):
    l2=list(l[-1::-1])
    return l2
print("reversed list",listfun(l))


# In[ ]:


###  14: List Rotation
#Write a function that rotates a list by n positions. Print the original and rotated lists.
l=[1,2,3,4,5,6,8,19]
n=int(input("enter number of rotations"))
l2=list()

def rotationlist(l,n):
    while(n>0):
        temp=l[0]
        for i,val in enumerate(l):
            if(i<len(l)-2):
                l[i]=l[i+1]
        l[len(l)-1]=temp
    return l



# In[ ]:


### Assignment 15: List Intersection
#Write a function that takes two lists and returns a new list containing only the elements that are present in both lists. Print the intersected list.

