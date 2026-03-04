#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # Imports numpy library as alias np

def monte_carlo_int(func, a, b, N): # Define function with variables func, a (lower lim), b (upper lim), N (number of points)
    """ Monte calro integration between a and b"""
    
    x = np.random.uniform(a, b, N) # Generate N amount of x values uniform between a and b
    y = eval(func) # Evaluates the function put in when called upon the udf

    integ = (b-a) * np.mean(y) # Calculate the integral using that the (sum of f(x))/n is equal to the mean of all f(x)
    return integ

func = input("Enter function you want the integral of:") # Define func as input
a = float(input("Enter the lower bound:")) # Define a (lower bound in integral) as input
b = float(input("Enter the upper bound:")) # Define b (upper bound in integral) as input
N = int(input("Enter the number of samples to use in integral (like 1000):")) # Define N (number of samples) as input
result = float(monte_carlo_int(func, a, b, N)) # Should be around 1/2 since integral of x between 0 and 1 is 1/2, float to get rid of np.float64 infront
print(result)


# In[ ]:




