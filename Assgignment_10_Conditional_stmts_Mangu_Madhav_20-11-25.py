#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Login Verification: Check if the entered password equals 'admin123'.
password='admin123'
user_password=input("enter the password")
if(password==user_password):
    print("login Successful")


# In[3]:


# 2. Age Eligibility: Check if age ≥ 18 for A-rated movie.
age=int(input("enter your age"))
if(age>=18):
    print("you are eligible ")
    


# In[5]:


# 3. Mobile Recharge Offer: ₹199 or above → free 2GB data coupon.
recharge_plan=int(input("enter your recharge plan"))
if(recharge_plan>=199):
    print("You'v got 2GB data Coupon")


# In[8]:


# 4.Student Grade Checker: Assign grades based on marks.
marks=int(input("enter your marks"))
if(marks>=90):
    print("Grade : A, EXCELLENT!!!")
elif(marks>=70):
    print("Grade: B, very Good!")
elif(marks>=70):
    print("Grade: C, Good")
elif(marks>=60):
    print("Grade: D, You've to improve")
else:
    print("FAIL, Better luck Next Time")
    


# In[13]:


#5. Temperature Alert System: Categorize weather by temperature.
Temp=eval(input("enter the temperature"))
if(Temp>40):
    print("It's Better to stay at home,it's too hot at outside")
elif(Temp>30):
    print("You may go out")
elif(Temp>20):
    print("perfect weather, you should go out")
else:
    print("It's too cold to go out")


# In[16]:


#  6. Credit Card Eligibility: Salary and CIBIL nested check.
salary=float(input("enter your salary"))
cibil=float(input("enter your cibil score"))
if(salary>30000):
    if(cibil>65):
        print("You are Eligible for Credit Card")
    else:
        print("NOT Eligible for CREDIT CARD....Cibil Score is low")
else:
    print("NoT Eligible for CREDIT CARD...Salary is too les")


# In[26]:


# 7. ATM Withdrawal Validator: Check balance + multiple of 100.
withdraw=float(input("enter amount to be withdraw"))
balance=200000
if(withdraw<balance):
    if(withdraw%100==0):
        print("Tansaction successful!!!..\nPlease collect your Cash..")
    else:
        print("please enter the multiples of 100 only")
else:
    print("Insufficient Balance")
    


# In[35]:


#8. Mobile Number Validator: Length 10 and starts with 6/7/8/9.
phno=int(input("enter your number"))
pn=str(phno)
print(pn,type(pn))
print(len(pn))
if(len(pn)==10):
    if(pn[0]==6):
        print("eligible")
    elif(p
else:
    print("enter valid number")


# In[45]:


# 9. Electricity Bill Category: Use match-case for type
E_bill=float(input("enter electic bill"))
# match(E_bill):
#     case 3000:
#         print("Your's is Domestic Electric bill")
#     case 20000:
#         print("your's is Commericial Electric bill")
#     case 20000:
#         print("your's is industrial Electric bill")
#     case _:
#         print("enter valid bill amount")


# In[39]:


# Simple Calculator: Use match-case for +, -, *, /.
n1=int(input("enter 1st number"))
n2=int(input("enter 2nd number"))
op=input("enter operator(+,-,*,/)")
match(op):
    case '+':
        print(f'Addition of {n1} and {n2} is {n1+n2}')
    case '-':
        print(f'Subtraction of {n1} and {n2} is {n1-n2}')
    case '*':
        print(f'Multiplication of {n1} and {n2} is {n1*n2}')
    case '/':
        print(f'floor Division of {n1} and {n2} is {n1/n2}')
    case _:print("enter valid operator")

