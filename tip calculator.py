#!/usr/bin/env python
# coding: utf-8

# In[3]:


#This simple Python program calculates how much each person should pay for the restaurant bill based on the following:
# - total bill
# - number of people to split
# - percentage of tip (10, 12, 15)

print("Welcome to the tip calculator.")
#get the total bill value
bill = float(input("What was the total bill? $"))
#get the number of people to split
num_people = int(input("How many people to split the bill? "))

#initialize the tip_percent variable
tip_percent = 0

#The user will be in an infinite loop until he inputs the values within (10, 12, 15)
while tip_percent not in (10,12,15):
  tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

#calculate the payment for each person
pay = round((bill*((tip_percent+100)/100))/num_people,2)
print(f"Each person should pay: ${pay}")


# In[ ]:




