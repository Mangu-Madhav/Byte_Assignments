#!/usr/bin/env python
# coding: utf-8

# In[8]:


#1 Write a program that asks the user to input a number and prints whether the
 # number is positive.
num=eval(input("enter a number"))
if num>0:
    print("the number is positive")
    


# In[9]:


# 2 Write a program that asks the user to input a number and prints whether the
#  number is positive or negative.
num=eval(input("enter a number"))
if num>=0:
    print("The number is positive")
else:
    print("The number is negative")


# In[10]:


#3 Write a program that asks the user to input a number and prints whether the
# number is positive, negative, or zero.
num=eval(input("enter a number"))
if num>0:
   print("The number is positive")
elif num<0:
   print("The number is negative")
else:
   print("The number is Zero")


# In[11]:


#4 Write a program that asks the user to input a number and prints whether the
# number is positive and even, positive and odd, or negative.
num=eval(input("enter a number"))
if num>0:
   if num%2==0:
       print("The number is positive and Even")
   else:
       print("The number is Positive and Odd")
else:
   print("The number is negative")


# In[19]:


#5 Write a program that prints all the numbers from 1 to 10 using a for loop.
for i in range(1,11):
     print(i)


# In[12]:


#6  Write a program that prints all the numbers from 1 to 10 using a while loop.
n=1
while(n<11):
    print(n)
    n=n+1


# In[11]:


# 7 Write a program that prints a 5x5 grid of asterisks (*) using nested loops
for i in range(1,6):
   for j in range(1,6):
       print("*",end="\t")
   print("\n")


# In[13]:


# 8 Write a program that asks the user to input numbers until they input 0. The
# program should print the sum of all the input numbers.
sum=0
num=int(input("enter a number"))
while(num!=0):
    num=int(input("enter a number"))
    sum+=num 
print(sum)


# In[14]:


#9 Write a program that prints all the numbers from 1 to 10 except 5 using a for loop
#  and continue statement.
for i in range(1,11):
    if(i==5):
        continue
    print(i)


# In[38]:


# 10 Write a program that defines an empty function using the pass statement.
 


# In[16]:


# #11  Write a program that asks the user to input a number and prints all the even
#  numbers from 1 to that number using a for loop.
num=int(input("enter a number"))
for i in range(1,num+1):
    print(i)


# In[45]:


#12 Write a program that calculates the factorial of a number input by the user using a
# while loop.
num=int(input("enter a number"))
fact=1
while(num>0):
   fact*=num
   num-=1
print(fact)


# In[49]:


#13 Write a program that calculates the sum of the digits of a number input by the user
#  using a while loop.
num=int(input("enter a number"))
sum=0
while(num>0):
    sum+=(num%10)
    num//=10
print(sum)


# In[18]:


# 14 Write a program that checks if a number input by the user is a prime number using
#  a for loop
count=0
num=int(input("enter a number"))
for i in range(2,num):
    if(num%i==0):
        count+=1
if(count==0):
    print("prime")
else:
    print("not Prime")


# In[6]:


# 15 Write a program that prints the first n Fibonacci numbers, where n is input by the
# user.
n=int(input("enter a number"))
a,b=0,1
print(a,b,end=" ")
while(n>2):
   c=a+b
   print(c,end=" ")
   a=b
   b=c
   n-=1

