#!/usr/bin/env python
# coding: utf-8

# In[2]:

# Sirius data
apparentMagnitude = -1.46
absoluteMagnitude = 1.45

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

m = apparentMagnitude
M = absoluteMagnitude

d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164
dist = f"The distance to Sirius: {d} pc"
print(dist)


# define magnitudes as input given by user
apparentMagnitude = input("Give the value for the apparent magnitude: ")
absoluteMagnitude = input("Give the value for the absolute magnitude: ")

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

#convert inputted values to integers so they can be used in the formula for distance
m = float(apparentMagnitude)
M = float(absoluteMagnitude)

d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164
dist = f"The distance to the star is: {d} pc"
print(dist)

# In[ ]:




