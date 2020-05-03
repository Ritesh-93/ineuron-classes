#!/usr/bin/env python
# coding: utf-8

# In[1]:


"my name is ritesh"


# # Task 1
# 
# # Problem 2

# In[2]:


x =[]
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
        if i % 5 !=0:
            x.append(i)
print(x)
print(len(x))


# # Problem 3

# In[4]:


first_name = 'ritesh'
last_name = 'yadav'
name=first_name+ " " +last_name
name = name[::-1]
name


# # Problem 4

# In[5]:


#Formula: V=4/3 * π * r 3

pi = 3.1415926535897931
r= 6.0
v= 4.0/3.0*pi* r**3
v


# # Task 2
# 
# 
# # Problem 1

# In[1]:


x = '1, 2, 3, 4, 5, 6, 7, 8, 9, 10'
list = x.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)


# # Problem 3

# In[20]:


name = 'riteshyadav'
name = name[::-1]
name


# # Problem 4

# In[19]:


print("WE, THE PEOPLE OF INDIA,\n having solemnly resolved to constitute India into a SOVEREIGN, !\n SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC\n and to secure to all")

