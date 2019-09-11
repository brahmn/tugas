#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import scipy.stats
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[18]:


df = pd.read_csv("H:\Tugas\Belajar\Python\mtcars.csv")
df


# In[19]:


df.describe()


# In[20]:


df.sort_values('mpg')


# In[23]:


df = pd.read_csv("H:\Tugas\Belajar\Python\mtcars.csv")
df


# In[48]:


df.pivot(index='mpg_level',columns='model')


# In[37]:


plt.scatter(df.mpg, df.cyl)


# In[ ]:


#Berdasarkan scatterplot di atas menunjukkan besarnya silinder mobil berhubungan dengan semakin rendanya konsumsi bensin kendaraan.


# In[35]:


plt.scatter(df.mpg, df.disp)


# In[ ]:


#Untuk variabel miles per gallon dan display menunjukkan bahwa terdapat hubungan, yang mana semakin tingginya konsumsi bensin maka display kendaraan juga semakin rendah begitu pula sebaliknya


# In[38]:


plt.scatter(df.mpg, df.hp)


# In[ ]:


#Sedangkan variable mpg dan hp, menunjukkan bahwa tingginya konsumsi bahan bakar maka semakin rendahnya tenaga mobil tersebut, begitu pula sebaliknya


# In[40]:


plt.scatter(df.mpg, df.drat)


# In[ ]:


#Pada hubungan variabel antara mpg dan drat tidak terlalu menunjukkan hubungan yang berarti di mana pada plot memperlihatkan jika plot antara dua variabel cenderung menyebar


# In[36]:


plt.scatter(df.mpg, df.wt)


# In[ ]:


#Pada variabel mpg dan wt menunjukkan perbandingan terbalik, yang mana semakin tingginya mpg maka berat kendaraan (wt) pada kendaraan juga semkain ringan


# In[41]:


plt.scatter(df.mpg, df.qsec)


# In[ ]:


#Hubungan antara variabel mpg dan qsec cenderung tidak menunjukkan hubungan yang terlalu berarti, di mana titik plotnya cenderung tersebar tidak mengikuti tren


# In[42]:


plt.scatter(df.mpg,df.vs)


# In[ ]:


#Hubungan antara mpg dan vs memperlihatkan jika semakin rendahnya mpg maka lebih cenderung pada rendahnya vs. Meskipun terdapat sebagian titik di mana kendaraan dengan konsumsi rendah memiliki vs tinggi begitupun sebaliknya


# In[43]:


plt.scatter(df.mpg, df.am)


# In[ ]:


#Pada variabel am dan mpg menunjukkan mobil berkonsumsi tinggi cenderung berjenis automatic, dan sebaliknya mobil tanpa manual justru memiliki konsumsi lebih rendah


# In[44]:


plt.scatter(df.mpg, df.gear)


# In[ ]:


#Pada grafik scatterplot menunjukkan bahwa kendaraan bermpg rendah cenderung yang memiliki gigi tiga, sedangkan kendaraan bergigi empat dan lima cenderung memiliki konsumsi tinggi


# In[45]:


plt.scatter(df.mpg, df.carb)


# In[ ]:


#Kendaraan yang memiliki carburator rendah cenderung mempunyai konsumsi bahan bakar yang tinggi.

