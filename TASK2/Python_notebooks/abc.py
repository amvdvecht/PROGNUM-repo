#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import *
# Input values for a b and c and convert to float
a = float(input("Give a value for a:")) 
b = float(input("Give a value for b:"))
c = float(input("Give a value for c:"))

D = (b**2) - 4 * a * c # Calculate D with given function

# If D is bigger than 0 provide the two answers by calculating x using the formula from the question
if D > 0:
    x_1 = ( -b + sqrt( (b**2) - 4 * a * c) ) / (2 * a)
    x_2 = ( -b - sqrt( (b**2) - 4 * a * c) ) / (2 * a)
    print(f"f(x) = {a} x^2 + {b} x + {c}, with values a={a}, b={b}, c={c}, gives 2 solutions.")
    print(f"The solutions are x={x_1}, and x={x_2}")

# If D is smaller than 0 print that there are no solutions for the input a, b, and c
elif D < 0:
    print(f"There are no solutions for f(x), with the values a={a}, b={b}, c={c}")
    
# If D is 0 provide the answer by calculating x (- or + square root will give the same answer since you add or substract 0 so we only use 1 of them to calculate x)
elif D == 0:
    x = ( -b + sqrt( (b**2) - 4 * a * c) ) / (2 * a)
    print(f"There is only 1 solution for f(x), with values a={a}, b={b}, c={c}") 
    print(f"The solution is x={x}")
    
# Failsafe if anything goes wrong: ask user to resubmit values of a,b,c
else:
    print(f"It seems something went wrong, please retry with different values for a, b, and c")


# In[ ]:




