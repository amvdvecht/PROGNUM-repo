#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("In the following input put your day month and year of birth:") # Give explanaition about what to input

D, M, Y = input("Day of birth:"), input("Month of birth:"), input("Year of birth:") # Define varidables D, M, and Y as the input day, month and year of birth
print(f"The first birth date is: {D}-{M}-{Y}") # Print the put in date

D, M, Y = float(D), float(M), float(Y)                # Convert to floats to allow for partial days

JD = 367*Y -7*(Y+(M+9)/12)/4 - 3*((Y+(M-9)/7)/100 + 1)/4 + (275*M)/9 + D + 1721029-0.5 # Calculate the JD value with the formula from the question
print(f"Your JD value is: {JD}")     # Print the previously calculated JD value


# In[ ]:




