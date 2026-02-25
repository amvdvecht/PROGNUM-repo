#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#give the input for the birthdate of the first person

print("In the following inputs put the day month and year of the birth of person 1:")

D1, M1, Y1 = input("Day of birth:"), input("Month of birth:"), input("Year of birth:")
print(f"The first birth date is: {D1}-{M1}-{Y1}")


D1, M1, Y1 = float(D1), float(M1), float(Y1)                #convert to floats to allow for partial days

JD1 = 367*Y1 -7*(Y1+(M1+9)/12)/4 - 3*((Y1+(M1-9)/7)/100 + 1)/4 + (275*M1)/9 + D1 + 1721029-0.5
print(f"The JD value of person 1 is {JD1}")

#give the input for the birth date of the second person

print("in the following inputs put the day month and year of the birth of person 2:")

D2, M2, Y2 = input("Day of birth:"), input("Month of birth:"), input("Year of birth:")
print(f"The second birth date is: {D2}-{M2}-{Y2}")


D2, M2, Y2 = float(D2), float(M2), float(Y2)                #convert to floats to allow for partial days

JD2 = 367*Y2 -7*(Y2+(M2+9)/12)/4 - 3*((Y2+(M2-9)/7)/100 + 1)/4 + (275*M2)/9 + D2 + 1721029-0.5
print(f"The JD value of person 1 is {JD2}")

JD1, JD2 = int(JD1), int(JD2)                               #convert to integers to get rid of any decimals without rounding off

Days = abs(JD2-JD1)                                         #calculate the days between two birth dates
print(Days)


# In[ ]:




