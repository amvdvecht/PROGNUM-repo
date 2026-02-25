#!/usr/bin/env python
# coding: utf-8

# In[1]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]
smaller = []
for i in range(len(masses)):  # Makes a loop so the following code is done for indices ranging from 0 to the end of the list masses
    m = masses[i]    # Define new variable as specific item from masses with index i
    m_moon = masses[-2]   # Define the moon mass as the item with index -2
    if m <= m_moon:     # If the previously defined mass is smaller or equal to the moon mass do the following:
        smaller.append(m)   # Add the mass to the previously empty list "smaller"

print(f"The values from the list masses that are smaller than the moon's mass are: {smaller}") # Print the list with only the smaller values

masses2 = masses[-5:]  # Define masses 2 as the list containing the last 5 of the original only
print(f"The list with the last five masses is: {masses2}")

avg = sum(masses2) / len(masses2) # Define the average as the sum of all values from masses2 devided by the length of masses2
print(f"The average mass of the previous list is: {avg}")


# In[ ]:




