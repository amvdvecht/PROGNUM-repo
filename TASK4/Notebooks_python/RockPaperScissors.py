#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # Import numpy library with alias np

choice = np.array(['R', 'P', 'S']) # Make array of available options for the computers choice
indx = np.random.randint(0, len(choice), 1) # Pick a random number from 1 to 3, will be the index corresponding to the pick of the computer
player = input("Choose R (rock), P (paper) or S (scissors):") # Make the player submit their choice of rock paper or scissors
print(f"Computers choice is: {choice[indx]}, Your choice is: {player}") # Print both the choice of the computer and the player

if player == 'R' or player == 'P' or player == 'S': # Check wether player input is a valid option of rock paper or scissors

    """ Using if loops, compare the answer of the computer and the player, same means a tie. Rock beats paper, paper beats scissors and scissors beats rock.
    Check the computers choice and then the players choice, based on what the choices are print that you won or lost """
    
    if choice[indx] == player:
        print(f"It's a tie")

    if choice[indx] == 'R':
        if player == 'S':
            print(f"You lost :(")
        if player == 'P':
            print(f"You won!!!")
        
    if choice[indx] == 'P':
        if player == 'R':
            print(f"You lost :(")
        if player == 'S':
            print(f"You won!!!")
        
    if choice[indx] == 'S':
        if player == 'P':
            print(f"You lost :(")
        if player == 'R':
            print(f"You won!!!")
else:
    print(f"Please provide a valid input (P, S or R) as {player} is not valid") # If player input is not valid mention that it should be changed for the code to work


# In[ ]:




