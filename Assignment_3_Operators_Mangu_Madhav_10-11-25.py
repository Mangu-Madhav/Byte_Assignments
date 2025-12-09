#!/usr/bin/env python
# coding: utf-8

# # Lesson 1.2: Python Basics
# # Topics Covered:
# - Syntax and Semantics
# - Variables and Data Types
# - Basic Operators (Arithmetic, Comparison, Logical)
# 

# # 1. Syntax and Semantics
# 
# **Question 1:** Write a Python program to print "Hello, World!".

# In[1]:


print("Hello, World!")


# **Question 2:** Write a Python program that takes a user input and prints it.

# In[3]:


userInput=input("enter input")
print(userInput)


# **Question 3:** Write a Python program to check if a number is positive, negative, or zero.

# In[12]:


a=float(input("enter any number"))
if(a>0):
    print(a,"is positive number")
if(a<0):
       print(a," is Negative number:")
if(a==0):
    print(a,"is Zero")


# **Question 4:** Write a Python program to find the largest of three numbers.

# In[18]:


print("Enter any three numbers to find largest of them")
a=float(input())
b=float(input())
c=float(input())
if(a>c and a>b):
    print(a," is the largest numbers")
elif(b>c and b>a):
    print(b," is the largest number")
else:
    print(c," is the largest number")


# **Question 5:** Write a Python program to calculate the factorial of a number.

# In[122]:


a=int(input("enter a number to find its factorial"))
fact=1
while(a>0):
    fact=fact*a
    a=a-1
print(fact)


# # 2. Variables and Data Types
# 
# **Question 6:** Create variables of different data types: integer, float, string, and boolean. Print their values and types.

# In[21]:


a,b,c,d,e=10,0.5,2+3j,"hello",True
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))


# **Question 7:** Write a Python program to swap the values of two variables.

# In[22]:


a=10
b=30
print("The values of a and b before swapping",a,b)
a,b=b,a
print("The values of a and b after swapping :", a,b)


# **Question 8:** Write a Python program to convert Celsius to Fahrenheit.

# In[30]:


# Your code here
C=float(input("enter Celsius to convert it into Fahrenheit"))
F=(C*1.8) + 32
print(F,"'s fahrenheit")


# **Question 9:** Write a Python program to concatenate two strings.

# In[31]:


a=input("enter first string")
b=input("enter second string")
print(a+b)


# **Question 10:** Write a Python program to check if a variable is of a specific data type.

# In[33]:


a=5
print(a,type(a))


# ## 3. Basic Operators (Arithmetic, Comparison, Logical)
# 
# **Question 11:** Write a Python program to perform arithmetic operations: addition, subtraction, multiplication, and division.

# In[36]:


a=20
b=5
print(f'Addition of {a} and {b} is {a+b}')
print(f'Subtraction of {a} and {b} is {a-b}')
print(f'Multiplication of {a} and {b} is {a*b}')
print(f'floor Division of {a} and {b} is {a/b}')
print(f'Integr Divison of {a} and {b} is {a//b}')
print(f'MOdulus of {a} and {b} is {a%b}')


# **Question 12:** Write a Python program to demonstrate comparison operators: equal to, not equal to, greater than, less than.

# In[48]:


a=10
b=20
print("b is greater than a:\t\t",b>a)
print("b is less than   a: \t\t",b<a)
print("a is less than equal to b:\t",a<=b)
print("a is greater than equal to b:\t",a>=b)
print("a is  equal to b:\t\t",a==b)
print("a is  equal to b:\t\t",a!=b)


# **Question 13:** Write a Python program to demonstrate logical operators: and, or, not.

# In[51]:


a=20
b=5
c=not b
print(f'{a} and logical_AND of {b} is {a and b}')
print(f'{a} and logical_OR of {b} is {a or b}')
print(f'logical_NOT of {a} is {c}')


# **Question 14:** Write a Python program to calculate the square of a number.

# In[56]:


a=float(input("enter a number to find it's Square"))
print(f'square of {a} is {a**2}')


# **Question 15:** Write a Python program to check if a number is even or odd.

# In[68]:


a=float(input("enter a number"))
if(a%2==0):
    print(f'{a} is EVEN')
else:
    print(f'{a} is ODD')


# **Question 16:** Write a Python program to find the sum of the first n natural numbers.

# In[67]:


a=int(input("enter no.of first n natural numbers to find their sum"))
print((a*(a+1))/2)


# **Question 17:** Write a Python program to check if a year is a leap year.

# In[82]:


year=int(input("Enter the Year"))
if(year%4==0 or year%100==0):
    print(f'{year} is leap year')
else:
    print(f'{year} is NOT leap year')


# **Question 18:** Write a Python program to reverse a string.

# In[100]:


a=input("enter a String")
b=len(a)-1
c=""
while(b>=0):
    c=c+list(a)[b]
    b=b-1
print(c)


# **Question 19:** Write a Python program to check if a string is a palindrome.

# In[110]:


a=input("enter a String")
b=len(a)-1
c=""
while(b>=0):
    c=c+list(a)[b]
    b=b-1
print(c,type(c))
if(a==c):
    print(f'the string {a} is palindrome')
else:
    print(f'The string {a} is NOT palindrome')
    


# **Question 20:** Write a Python program to sort a list of numbers in ascending order.

# In[127]:


a=[10.20,2,5]
a.sort(reverse=False)
print(a)


# In[ ]:




