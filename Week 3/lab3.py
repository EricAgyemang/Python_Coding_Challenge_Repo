#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Problem1
ULID = input("Enter a ULID: ")
ULID1 = ULID[::-1]
ULID_Partial = ULID[-1]
if ULID.isalpha() == True:
    print(ULID + " consists of only alphabetical letters.")
elif ULID_Partial.isdigit()==True:
    print(ULID + " ends with a number.\nThe reversed ULID is: "+ULID1)
else: 
    print(ULID + " is not a valid ULID.")


# In[2]:


#Problem2
num = input("Enter a number: ")
num1 = float(num)
if "." in num:
    print("It is a floating-point number and the value is " + num+".")
elif num1 % 2 == 0:
    print("It is an even number and the value is "+num+".")
else:
    print("It is an odd number and the value is "+num+".")


# In[7]:


#Problem3
number = input("Enter a number: ")
number1 = float(number)
if number1 > 0:
    if "." in number:
        print(number + " is a positive floating-point number.")
    elif number1 % 2 == 0:
        print(number + " is a positive even number.")
    else:
        print(number + " is a positive odd number.")
else:
    if "." in number:
        print(number + " is a negative floating-point number.")
    elif number1 % 2 == 0:
        print(number + " is a negative even number.")
    else:
        print(number + " is a negative odd number.")


# In[ ]:





# In[ ]:




