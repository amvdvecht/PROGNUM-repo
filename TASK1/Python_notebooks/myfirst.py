#!/usr/bin/env python
# coding: utf-8

# Answers for Week 1
# 
# * Name: Anna van der Vecht
# * Username: amvecht
# * Student s-number: s6390382
# * Group (AS1, etc.): AS5

# Question 1.2 : First Session Quiz in a notebook

# In[3]:


x = 22/7


# $$y=\frac{sin(x)}{x}$$

# In[1]:


pi = 22/7 # Processed on Jupyter Hub


# 1.6.1. Embedding an image with Markdown

# ![dolphin.jpg](attachment:eda1b86b-2c8b-49a5-a660-8285409acb95.jpg)

# Question 1.3 : Augmented assignment operators

# In[6]:


x = 6
print(x)
x *= 5
x *= 4
x *= 3
x *= 2
x *= 1
print(x)


# Question 1.4 : Energy of a single photon

# In[26]:


from scipy.constants import c
from scipy.constants import h
print(c, h)
f = 2.42 * (10 ** 28)
print(f)
l = c/f 
print(l)

E = h*(c/l)
print(E)


# Question 1.5 : Gravitational pull

# In[20]:


from scipy.constants import G
m1=7.342*(10**22)
m2 = 5.9722*(10**24)
r= 385000.6

print (G)
print (m1)
print(m2)
print(r)

F = G*((m1*m2)/(r**2))
print("F=", F, "N")


# Question 1.7 : Print function

# In[25]:


x1 = 10
x2 = 22/7
print(x1, end="")
print(x2, end="")


# The end="" in the code will define what will be at the end of the printed value or text given before the comma.

# Question 1.9 : Command line exercises

# 1. echo $SHELL gives: /bin/bash
# 2. ls gives: coursework_week1.ipynb  dolphin.jpg  magnitude.ipynb  magnitude.py  Screenshot_20260210_143758.png  sq_s6390382_week1-1.ipynb
#    so a list of all the files in the current folder
# 3. ls -rtl gives: total 260
# -rw-r--r-- 1 amvecht users   5316 Feb 10 13:21 dolphin.jpg
# -rw-r--r-- 1 amvecht users    845 Feb 10 14:33 magnitude.py
# -rw-r--r-- 1 amvecht users  58643 Feb 10 14:39 Screenshot_20260210_143758.png
# -rw-r--r-- 1 amvecht users 171020 Feb 10 14:41 coursework_week1.ipynb
# -rw-r--r-- 1 amvecht users   2415 Feb 10 14:41 magnitude.ipynb
# -rw-r--r-- 1 amvecht users  12351 Feb 12 12:27 sq_s6390382_week1-1.ipynb
#     so that gives a more detailed list including total amount and the precise info of each file.
# 4. touch a.txt one creates a new and empty file, by using ls again (or ls rtl if you nee a clearer overview) you can see if the new file has been added
# 5. cp a.txt b.txt copies the text from a to b
# 6. mv b.txt c.txt moves the content from b to c
# 7. mkdir PROGNUM creates a folder in your current location folder
# 8. cd PROGNUM moves you into the prognum folder
# 9. 

# Question 1.13 : Commit and push your changes

# [amvecht@jupyterhub1 Week_1]$ cd ../../ ls
# bash: cd: too many arguments
# [amvecht@jupyterhub1 Week_1]$ cd ../../PROGNUM
# bash: cd: ../../PROGNUM: No such file or directory
# [amvecht@jupyterhub1 Week_1]$ rm a.txt
# [amvecht@jupyterhub1 Week_1]$ rm c.txt 
# [amvecht@jupyterhub1 Week_1]$ cd PROGNUM/
# cp -r * ../PROGNUM-repo/
# [amvecht@jupyterhub1 PROGNUM]$ cp -r * ../PROGNUM-repo/
# [amvecht@jupyterhub1 PROGNUM]$ ls - l
# ls: cannot access '-': No such file or directory
# ls: cannot access 'l': No such file or directory
# [amvecht@jupyterhub1 PROGNUM]$ ls -l
# total 0
# drwxr-xr-x 2 amvecht users 10 Feb 12 12:38 TASK1
# [amvecht@jupyterhub1 PROGNUM]$ git status
# fatal: not a git repository (or any parent up to mount point /Users)
# Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
# [amvecht@jupyterhub1 PROGNUM]$ cd PROGNUM-repo
# bash: cd: PROGNUM-repo: No such file or directory
# [amvecht@jupyterhub1 PROGNUM]$ cd PROGNUM-repo/
# bash: cd: PROGNUM-repo/: No such file or directory
# [amvecht@jupyterhub1 PROGNUM]$ cd PROGNUM-repo /
# bash: cd: too many arguments
# [amvecht@jupyterhub1 PROGNUM]$ cd Week_1/PROGNUM-repo/
# bash: cd: Week_1/PROGNUM-repo/: No such file or directory
# [amvecht@jupyterhub1 PROGNUM]$ cd
# [amvecht@jupyterhub1 ~]$ cd PROGNUM-repo/
# [amvecht@jupyterhub1 PROGNUM-repo]$ git status
# On branch main
# Your branch is up to date with 'origin/main'.
# 
# nothing to commit, working tree clean
# [amvecht@jupyterhub1 PROGNUM-repo]$ git add *
# [amvecht@jupyterhub1 PROGNUM-repo]$ git status
# On branch main
# Your branch is up to date with 'origin/main'.
# 
# nothing to commit, working tree clean
# [amvecht@jupyterhub1 PROGNUM-repo]$ git commit -m "add new folders and files" 
# On branch main
# Your branch is up to date with 'origin/main'.
# 
# nothing to commit, working tree clean
# [amvecht@jupyterhub1 PROGNUM-repo]$ git push 
# Username for 'https://github.com': amvdvecht
# Password for 'https://amvdvecht@github.com': 
# remote: Invalid username or token. Password authentication is not supported for Git operations.
# fatal: Authentication failed for 'https://github.com/amvdvecht/PROGNUM-repo.git/'
# [amvecht@jupyterhub1 PROGNUM-repo]$ git push
# Username for 'https://github.com': amvdvecht
# Password for 'https://amvdvecht@github.com': 
# Everything up-to-date

# In[ ]:




