#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Import libraries with alias's
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define given function and set in the calling environment
def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0
A = float(input(f"Give value for the amplitude:")) # Amplitude
x0 = float(input(f"Give value for the peak position:")) # Peak position
sig = float(input(f"Give value for the peak width:")) # Peak width
z0 = float(input(f"Give value for the offset in y:")) # offset in y

# Plot function
x = np.linspace(-10, 10, 200) # Generate 200 samples between -10 and 10 for x
y = gauss(x, A, x0, sig, z0) # Use defined function with calling environment values for y
plt.figure()
plt.plot(x, y, label = 'Gaussian curve') # Plot x against y and label the plot

#Provide upper and lower limit
lower = float(input(f"Give value for the lower limit:"))  
upper = float(input(f"Give value for the upper limit:"))

#calculate are between upper and lower
area, error = quad(lambda t: gauss(t, A, x0, sig, z0), lower, upper) # quad calculates value and uncertainty, so we assign area to value and error to the uncertainty
print(f"The area between {lower} and {upper} is equal to: {area:.5g}") # prints area with maximum of 5 significant digits

# Fill area between upper and lower under gaussian curve
x_fill = np.linspace(lower, upper, 100)
y_fill = gauss(x_fill, A, x0, sig, z0)
plt.fill_between(x_fill, y_fill, color='orchid', alpha=0.3, label=f"Area = {area:.4g}")

# Graph customisation:
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Area under a Gaussian")
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




