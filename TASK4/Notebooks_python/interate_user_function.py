#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries as alias
import numpy as np
from scipy.integrate import quad
from numpy import sin, cos, exp, pi  # functions/constants user can use

#Define function montecarlo
def montecarlo(f, a, b, N=100000):
    """
    Compute integral between, user provided a and b and function f, using the monte carlo method.
    """
    try:
        x = np.random.uniform(a, b, N) # N amount of uniform distributed numbers between a and b 
        y = y = np.array([eval(f, {"x": xi, "sin": sin, "cos": cos, "exp": exp, "pi": pi}) for xi in x]) # Evaluate function f for each item in array x (add definitions so there is less risk of errors)
        integral = (b - a) * np.mean(y) # Calculate integral
        return integral
    except NameError as e:
        print(f"NameError: {e}. Did you use a function or variable not defined?")
        return None
    except Exception as e:
        print(f"Error during Monte Carlo integration: {e}")
        return None

# Ask user input
fstr = input("Enter a function f(x):")

# Calculate integral with quad
# Try/except clauses for input function
try:
    f = lambda x: eval(fstr, {"x": x, "sin": sin, "cos": cos, "exp": exp, "pi": pi}) # Redefine f as eval(f) with variable x (define ther functions and variables for less risk of error)
    result, error= quad(f, 0, np.pi) #Calculate integral using quad between 0 and pi (as asked in question)
    print(f"Integration with quad gives result: {result}")
except Exception as e:
    print(f"Error: {e}") # Print reason why it wont work

# Calculate integral with monte carlo (previously defined function)
result_mc = montecarlo(fstr,0,np.pi) #Calculate integral between 0 and pi (as asked in question)
if result_mc is not None: #add another failsafe
    print(f"Integral with Monte carlo gives result: {result_mc}")


# In[ ]:




