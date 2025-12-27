#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 Take two numbers as input and print their sum.
a=int(input("enter first number"))
b=int(input("enter second number"))
c=a+b
print("sum of the numbers is:",c)


# In[2]:


#2 Take a float number from the user and print
a=float(input("enter a float value"))
print(a)


# In[3]:


#3  Take your age as input and print how many years are left to reach 100.
age=int(input("enter your age"))
print(100-age, "more years to reach 100")


# In[5]:


#4 Ask the user for their first and last name and print full name.
first_name=input("enter first name")
second_name=input("enter second_name")
print(first_name,second_name)


# In[9]:


#5 Take radius as input (float) and print the area of the circle using Area = r² (use =3.14).
r=float(input("enter radius of the circle"))
area=3.14*(r**2)
print("area of the circle is:",area)


# In[10]:


#6 Take a number and multiply it with 2 and print their product.
num=int(input("enter a number"))
product=2*num
print(f'product of {num} and 2 is {product}')


# In[59]:


#7 Input a math expression as string and evaluate it (Example: 5*6*2).
a=input("enter an expression to evaluate")
#Not Possible from the concepts we learned


# In[13]:


#8  Take a string input representing a number, convert it to int, and add 10 to it
a=input("enter a number")
b=int(a)+10
print(b)


# In[15]:


#9 Take a float as input, convert it to integer and print both values.
a=float(input("enter a float number"))
b=int(a)
print(f'float value is {a} and int value is {b}')


# In[16]:


#10 program to Ask the user for their name and print: Welcome,
name=input("enter your name")
print(f'Welcome, {name}')


# In[18]:


#11 program to Add and print the result (a=12, b=5)
a=float(input("enter a number"))
b=float(input("enter another number"))
result=a+b
print(result)


# In[19]:


# 12 program to Multiply x * y and then subtract (x=10, y=3).
x,y=10,3
multiple=x*y
subtraction=x-y
print(f' muliplication of {x} and {y} is {multiple} and subtraction is {subtraction}')


# In[21]:


#13 program to Check and print the datatype of x if x is True.
a=input("enter x value")
x=bool(a)
if (x==True):
    print(x)


# In[23]:


#14 Program to Find remainder when one number is divided by another (17 and 4).
a=float(input("enter a number"))
b=float(input("enter another number"))
remainder=a%b
print(remainder)


# In[24]:


#15 Program to Multiply 3 numbers and subtract last (2, 3, and 4).
a,b,c=2,3,4
product=a*b*c
sub=a-b-c
print(f'multiplication of {a},{b},{c} is {product} and subtraction is {sub}')


# In[26]:


#16 Program to Form a number from digits 5, 6, 9.
a=5
b=6
c=9
print("number formed is",a+b*c)


# In[27]:


#17 Program to Find the difference between two integers (a=10, b=25).
a=int(input("enter first integer"))
b=int(input("enter second integer"))
diff=a-b
print("differnce is ",diff)


# In[31]:


#18 Program to Add 1 to a given number 99
a=int(input("enter a number"))
a+=1
print("after adding 1, the new number is",a)


# In[32]:


#19 Program to Square a number and Add 1 (number=4).
a=int(input("enter a number"))
b=(a**2)+1
print("after squaring and adding 1 to ",a," is ",b)


# In[33]:


#20 Program to Multiply a number by 10 and Subtract 5 (number=6).
a=float(input("enter a number"))
b=a*10-5
print(b)


# In[34]:


#21 Program to Add two float numbers 1.234 and 2.456
a=float(input("enter a float number"))
b=float(input("enter another float number"))
print(f'addition of {a} , {b} is {a+b}')


# In[36]:


#22 Program to Calculate the area of a circle with radius 2.5 (=3.14).
a=2.5
area=3.14*a**2
print(area)


# In[37]:


#23 Multiply a float 2.5 with large int 1000 
a=2.5
b=1000
print(a*b)


# In[38]:


#24  Program to Add float 2.5 with int 4. What is the output?
# Ans: 6.5
# proof
a-2.5
b=4
print(a+b)


# In[42]:


#25 Program to Calculate average value of three float values 2.5, 3.5 and 7.0.
a,b,c=float(input("enter any 3 float values to add them")),float(input()),float(input())
avg=(a+b+c)/3
print(avg)


# In[45]:


#26 Program to check  datatypes of the Given two variables 5 and 8.0,
a=5
b=8.0
print(a,type(a),"\n",b,type(b))


# In[49]:


#27 Program to Multiply an Integer 4 with float 2.0.

a=int(input("enter an integer number"))
print(a*2.0)


# In[51]:


#28 Program to Check Type before and after dividing it by 2 (number=5).
a=5
print(a, type(a))
      
div=a/5
print(div,type(div))


# 

# In[53]:


# 29 Program to Check the boolean value of x (x=20)
x=20
y=bool(x)
print(y)


# In[54]:


# 30 Program to Check the boolean value of x (x=0).
x=0
y=bool(x)
print(x)





