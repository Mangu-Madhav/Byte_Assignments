#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Core Python Proficiency Test – Level 1 


# In[2]:


#1 Print your name 5 times using only while loop. 
i=5
while(i>0):
    print("Mangu Madhav")
    i-=1


# In[3]:


# 2 Print numbers 1 to 10 using only while loop. 
i=1
while(i<11):
    print(i)
    i+=1


# In[4]:


# 3 Print numbers 10 down to 1 using only while loop.
i=10
while(i>0):
    print(i)
    i-=1


# In[1]:


# 4 Take a number from user and print its multiplication table (up to 10) using while loop
n=int(input("enter any number to give its multiplication table"))
i=1
print("multiplication table of ",n)
while(i<11):
    print(f'{n} * {i} = {n*i}')
    i+=1


# In[2]:


# 5 Keep asking for password until user enters "analytics2025" → print "Login Success!". 
n=input("enter password")
while(n!='analytics2025'):
    print("Please enter correct password")
    n=input()
else:
    print("login Success!")


# In[3]:


# 6 Add numbers continuously until user enters 0, then print the sum of all entered numbers.
n=int(input("enter any number"))
sum=0
while(n!=0):
    sum=sum+n
    n=int(input("enter any number"))
print("sum of the numbers is",sum)


# In[5]:


# 7 Calculate factorial of a number using only while loop 
n=int(input("enter any number"))
fact=1
while(n>1):
    fact*=n
    n-=1
print(f'factorial of the number  is {fact}')


# In[6]:


#  8 Reverse a number using while loop (12345 → 54321)
n=int(input("enter any number to print it in reverse"))
reverse=0
while(n>0):
    reverse=reverse*10+(n%10)
    n=n//10
print("the reverse number is ",reverse)


# In[15]:


# 9 Number guessing game: secret = 35. Give hints "Too high"/"Too low" until correct. 
secret=35
n=int(input("guess the number"))
while(n!=secret):
    if(n>35):
        print("Too High")
    elif(n<35):
        print("Too low")
    n=int(input("enter Again"))
print("yesss...You got it")


# In[53]:


#  10  Check if a number is palindrome using only while loop (no string methods).
n=int(input("guess the number"))
reverse=0
i=n
while(n>0):
    reverse=reverse*10+(n%10)
    n=n//10
if(i==reverse):
    print("palindrome")
else:
    print("Not Palindrome")
    


# In[7]:


# 11  Print the following pattern using only while loop: 
# text 
# 1 
# 22 
# 333 
# 4444 
# 55555
i=1

while(i<6):
    j=1
    while(j<=i):
        print(i,end=" ")
        j+=1  
    print("\n")
    i+=1


# In[10]:


#12. Implement a login system with maximum 3 attempts. If password is wrong 3 times → 
# print "Account Blocked!". Correct password: "python123" 
password=input("enter your password")
n=2
while(n>0 and password!='python123'):
        password=input("enter correct password")
        n-=1
if(n==0 and password!='python123'):
    print("Account blocked")
else:
    print("login successful")
    


# In[55]:


# 13 Keep taking expense amounts until user enters -1, then print total expense and count of 
# transactions. 
expenses=int(input("enter your expenditure"))
count=1
sum=0
while(expenses!=-1):
    sum=sum+expenses
    count+=1
    expenses=int(input("enter your expenditure"))
print(f'total expenditure  of your {count} transcations is {sum}')


# In[1]:


# 14 Print only odd numbers from 1 to 20 using while loop and continue statement. 
i=1
while(i<21):
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1


# In[6]:


# 15  Write a program using while loop to count and print the number of digits in a given 
# positive integer (Example: 7834 → 4 digits).
n=int(input("enter any positive number"))
count=0
if(n<0):
    print("enter only +ve numbers")
else:
     while(n>0):
        n=n//10
        count+=1
     print("number of digits in the given number is ",count)
        


# In[13]:


# # 16 (Updated) Write a program using while loop to calculate and print the sum of the series: 1 
# + 4 + 9 + 16 + … + 100 (i.e., sum of squares of first 10 natural numbers). 
i=1
sum=0
while(i<11):
    sum=sum+(i**2)
    i+=1
print("sum of the series is",sum)


# In[16]:


# 17 Print first 10 Fibonacci numbers using only while loop (0, 1, 1, 2, 3, 5, …). 
a=0
b=1
i=2
print(a,b,end=" ")
while(i<11):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    i+=1


# In[17]:


#  18  Use break when user types "stop" (case insensitive) in an infinite input loop.
i=0
while(i<1):
    n=input("enter any input")
    if(n.lower()=='stop'):
        break
    


# In[18]:


# # What is the output? 
# Python 
# i = 0 
# while i < 3: 
# print("Hi") 
# i += 1 
# else: 
# print("End") 

output will be:
hi
hi
hi
End


# In[5]:


# 20  Write a program to find GCD of two numbers using while loop (Euclidean algorithm)
n1=int(input("enter first number"))
n2=int(input("enter second number"))
if(n1>n2):
    i=n1
else:
    i=n2
Gcd=1
j=1
while(j<=i):
    if(n1%j==0 and n2%j==0):
        Gcd=j
    j+=1
print("GCD is",Gcd)


# In[ ]:




