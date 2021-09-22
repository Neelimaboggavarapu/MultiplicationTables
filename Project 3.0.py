#!/usr/bin/env python
# coding: utf-8

# In[9]:



number = int(input("Enter number:"))
n2 = int(input("Enter the number upto which you want the table of {num}:".format(num=number)))

mul = 1
print("Here is the table of ",number)
print("*"*50,"\n")
while(mul<=n2):
    print(number," x ",mul," = ",number*mul)
    mul = mul + 1


# In[ ]:




