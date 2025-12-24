#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Login Verification: Check if the entered password equals 'admin123'.
password='admin123'
user_password=input("enter the password")
if(password==user_password):
    print("login Successful")


# In[3]:


#2. Age Eligibility: Check if age ≥ 18 for A-rated movie.
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


# In[54]:


# 9. Electricity Bill Category: Use match-case for type
E_bill=float(input("enter units used"))
if(E_bill<100):
    x='a'
elif(E_bill<300):
    x='b'
elif(E_bill<900):
    x='c'
elif(E_bill>900):
    x='d'

match(x):
    case 'a':
        print(f'Rate per Unit is: Rs.4.5\nTotal bill is {4.5*E_bill}\nYour"s Domestic Electric bill')
    case 'b':
        print(f'Rate per Unit is: Rs.5.1\nTotal bill is {5.1*E_bill}\nYour"s Commericial bill')
    case 'c':
        print(f'Rate per Unit is: Rs.6.3\nTotal bill is {6.3*E_bill}\nYour"s institutional bill')
    case 'd':
        print(f'Rate per Unit is: Rs.8\nTotal bill is {8*E_bill}\nYour"s industrial bill')
    case _:
        print("enter only the no.of units used")


# In[39]:


# 10 Simple Calculator: Use match-case for +, -, *, /.
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


# In[14]:


# Project
# 1. Core Billing Logic (Using if-else and if)
option='yes'
sum=0
total_bill=0
total=0
sum_discount=0
while(option=='yes'):
    subtotal=0
    print("Items:Rice,dal,Sugar")
    Item_Name=input("enter Item Name\t\t   :")
    if(Item_Name.lower()=="rice"):
        Quantity=float(input("enter Quantity of the item :"))
        price=50
        print("Price\t\t\t   :",price)
        subtotal=price*Quantity
        print("subtotal\t\t   :",subtotal,end="\t")
        if(Quantity>10):
            Discount=0.05*subtotal
        else:
            Discount=0
        sum_discount+=Discount
        print("Sub_Discount\t\t   :",Discount)        
        total=total+(subtotal-Discount)
        # print("total \t\t\t   :",total)
    elif(Item_Name.lower()=="dal"):
        Quantity=float(input("enter Quantity of the item :"))
        price=40
        print("Price\t\t\t   :",price)
        subtotal=price*Quantity
        print("subtotal\t\t   :",subtotal,end="\t")
        if(Quantity>10):
            Discount=0.05*subtotal
        else:
            Discount=0
        sum_discount+=Discount   
        print("Sub_Discount\t\t   :",Discount)        
        total=total+(subtotal-Discount)
        # print("total \t\t\t   :",total)
        
    elif(Item_Name.lower()=="sugar"):
        Quantity=float(input("enter Quantity of the item :"))
        price=30
        print("Price\t\t\t   :",price)
        subtotal=price*Quantity
        print("subtotal\t\t   :",subtotal,end="\t")
        if(Quantity>10):
            Discount=0.05*subtotal
        else:
            Discount=0
        print("sub_discount\t\t   :",Discount)        
        total=total+(subtotal-Discount)
        # print("total \t\t\t   :",total)
        
    else:
        print("enter correct product Name:")
    option=input("Do you want to continue(yes/no)")
    
Discount2=0
loyal=input("is loayal member(yes/no)   :")    
if(loyal.lower()=='yes'):
    Discount2=0.1*total
sum_discount+=Discount2
print("Discount for loyal\t   :",Discount2,end="\t")
total_bill=total-Discount2
print("total bill_After_Discount  :",total_bill)
print("you have saved\t\t   :",sum_discount)
    


# In[14]:


# 2. Tiered Discounts & Surcharges
Total_amount=float(input("enter total amount on purchased products"))
Discount=0
if(Total_amount<100):
    Discount=0
    print("You have got Discount",Discount)
elif(Total_amount<500):
    Disount=0.05*Total_amount
    print("You have got Discount",Discount)
elif(Total_amount<1000):
    Discount=0.1*Total_amount
    print("You have got Discount",Discount)
else:
    Discount=0.15*Total_amount
    print("You have got Discount",Discount)
Total_amount=Total_amount-Discount
print("Total_bill is:",Total_amount)
ch=int(input("\nChoose payment method\n1.Credit_card\n2.Debit_card\n3.Cash\n"))
match(ch):
    case 1:
        fee=0.02*Total_amount
        Total_amount=Total_amount+fee
        print("Charges applied using Credit card :",fee)
        print("Total bill :",Total_amount)
    case 2:
        fee=0.1*Total_amount
        Total_amount=Total_amount+fee
        print("Charges applied using Credit card :",fee)
        print("Total bill :",Total_amount)
    case 3:
        discount=0.05*Total_amount
        Total_amount=Total_amount-discount
        print("You have got additional discount of ",discount)
        print("Total bill is:",Total_amount)
    case _:
        print("Choos valid payment method")


# In[17]:


# 3. Special Conditions (Using Nested if)
Cust_Id=int(input("enter customer id"))
is_delivery=input("Is it delivery product(yes/no)")
Total_amount=0
delivery_fee=0
if(is_delivery.lower()=='yes'):
    delivery_amount=float(input("Total price of the delivery order"))
    if(delivery_amount>500):
        print("CONGRATULATIONS!!!..You are Eligible for FREE delivary")
    else:
        print("delivery fee applied:50")
        delivery_fee=50
        Total_amount=delivery_amount+delivery_fee
else:
    print("NO delivery fee is applied")
is_premium_member=input("IS premium customer(yes/no)")
if(is_premium_member.lower()=='yes'):
    if(Total_amount>200):
        Bonus_points=50
        print("you have got bonus points of",Bonus_points)
    else:
        Bonus_points=10
        print("you have got bonus points of",Bonus_points)
    Special_Discount=0.05*Total_amount
    print("You have got 5% of special discount on premium subscription")
    Total_amount=Total_amount-Special_Discount
else:
    Normal_points=5
    print("you have got",Normal_points,"points")
print("Your Total amount is",Total_amount)


# In[29]:


# 4. Tax/VAT Calculation (Using match-case )
Cust_Id=int(input("enter customer id"))
ch='yes'
Tax_Amount=0
Total_of_sub=0
Total_amount=0
while(ch!='no'):
    name=input("enter product name:")
    price=eval(input("enter price of the product"))
    Quantity=eval(input("enter quantity of the"))
    sub_total=price*Quantity
    print("Product Name",name,"\nTotal Product Price :",sub_total)
    
    Total_of_sub=Total_of_sub+sub_total
    op=int(input("select category of the product\n1.Essentials\n2.Luxury Goods\n3.Electronics"))
    match(op):
        case 1:
            Tax_Amount=Tax_Amount+(0.05*sub_total)
            print("Tax applied on the product is:",0.05*sub_total)
        case 2:
            Tax_Amount=Tax_Amount+(0.20*sub_total)
            print("Tax applied on the product is:",0.20*sub_total)
        case 3:
            Tax_Amount=Tax_Amount+(0.12*sub_total)
            print("Tax applied on the product is:",0.12*sub_total)
        case _:
            print("\nselect correct category")
    ch=input("\nDo you want to buy more products(yes/no)")
Total_amount=Total_of_sub+Tax_Amount
print("\nTotal price of all the products is",Total_of_sub)
print("Total Tax on All products is",Tax_Amount)
print("Total amount due is",Total_amount)
    
    
    


# In[ ]:




