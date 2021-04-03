#!/usr/bin/env python
# coding: utf-8

# In[1]:


numbers=input()
print(numbers)


# In[2]:


numbers=input().split()
print(numbers)


# In[3]:


numbers=[int(x) for x in numbers]
print(numbers)


# In[7]:


for i in numbers:
    if i==1:
        print("Bulbasor")
    elif i==2:
        print("Pikachu")
    elif i==3:
        print("Charmandar")
    else:
        print("Invalid")


# In[9]:


#Dictionaries
pokemon_map={
    1:"Bulbasor",
    2:"Pikachu",
    3:"Charmandar",
    4:"Charizard"
}
print(pokemon_map)


# In[10]:


pokemon_map[2]


# In[12]:


for i in numbers:
    if pokemon_map.get(i) is None:
        print("Invalid")
    else:
        print(pokemon_map[i])


# In[14]:


def printpokemons(numbers):
    pokemon_map={
    1:"Bulbasor",
    2:"Pikachu",
    3:"Charmandar",
    4:"Charizard"
    }
    for i in numbers:
        if pokemon_map.get(i) is None:
            print("Invalid")
        else:
            print(pokemon_map[i])
    return


# In[15]:


numbers=[int(x) for x in input().split()]
printpokemons(numbers)


# In[16]:


get_ipython().system('pip install numpy')


# In[ ]:




