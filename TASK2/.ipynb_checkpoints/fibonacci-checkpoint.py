#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Define the starting values for the fibonacci sequence
first = 1
second = 2

for i in range(3, 100): # goes from the 3rd to 100th result because the 1st and 2nd are already defined and we want to go untill 100.
    following = first + second # Make next number in list the combination of the previous 2 numbers
    first = second # Make the second number the new first
    second = following # Replace the original second number with the calculated following

print(f"The 100th digit in the Fibonacci sequence is: {second}") #print the last second that was calculated, which is the 100th number


# In[ ]:




