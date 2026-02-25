#!/usr/bin/env python
# coding: utf-8

# In[15]:


from math import *
a = float(input("Give a value for a:"))
b = float(input("Give a value for b:"))
c = float(input("Give a value for c:"))

D = (b**2) - 4 * a * c

if D > 0:
    x_1 = ( -b + sqrt( (b**2) - 4 * a * c) ) / (2 * a)
    x_2 = ( -b + sqrt( (b**2) - 4 * a * c) ) / (2 * a)
    print(f"f(x) = {a} x^2 + {b} x + {c}, with values a={a}, b={b}, c={c}, gives 2 solutions.")
    print(f"The solutions are x_1={x_1}, and x_2={x_2}")
     
elif D < 0:
    print(f"There are no solutions for f(x), with the values a={a}, b={b}, c={c}")
elif D == 0:
    x = ( -b + sqrt( (b**2) - 4 * a * c) ) / (2 * a)
    print(f"There is only 1 solution for f(x), with values a={a}, b={b}, c={c}") 
    print(f"The solution is x={x}")
else:
    print(f"It seems something went wrong, please retry with different values for a, b, and c")


# In[ ]:




