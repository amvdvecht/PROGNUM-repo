#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Fibonacci:
    """Class for calculating Fibonacci sequence"""

    def __init__(self):
        self.sequence = [0, 1]
    def nth_term(self, N):
        """
        Returns the N-th Fibonacci number
        """
        for i in range(2,N+1):  # go untill the nth fib number is reached
            self.sequence.append(self.sequence[-1] + self.sequence[-2]) # add next fib number
        return self.sequence[N] # if N is reached print the Nth fib number (-1 as index also works to get the last value)

    def divisible_by(self, N, M):
        """
        Returns all Fibonacci numbers less than the N-th Fibonacci number
        that are divisible by M
        """
        fib_n = self.nth_term(N)  # compute N-th term
        divisible_list = [] # empty list
        a, b = 0, 1 # Starting values
        while a < fib_n: # if starting value is smaller than nth term (from previous method)
            if a % M == 0: # check if divideable
                divisible_list.append(a)
            a, b = b, a + b # calc new fib number
        return divisible_list

# Check with known values

fib = Fibonacci()

nth_100 = fib.nth_term(100)
print("100-th Fibonacci number:", nth_100)

div_by_7 = fib.divisible_by(100, 7)
print("Fibonacci numbers < 100-th term divisible by 7:")
print(div_by_7)


# In[ ]:





# In[ ]:




