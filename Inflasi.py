#!/usr/bin/env python
# coding: utf-8

# In[80]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import scipy.stats
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[79]:


inflasi = pd.read_excel("H:\Tugas\Belajar\Python\inflasi2.xlsx")
inflasi


# In[91]:


inflasi.info()


# In[84]:


inflasi.max()


# In[83]:


inflasi.min()


# In[85]:


inflasi.mean()


# In[88]:


plt.figure(figsize=(15,10)
plt.plot(inflasi.mean)
plt.show()


# In[58]:


data = pd.read_excel("H:\Tugas\Belajar\Python\inflasi3.xlsx")
data


# In[90]:


plt.figure(figsize=(15,10))
plt.plot(data.tahun, data.inflasi)
plt.legend(['Inflasi'])
plt.xlabel('Tahun')
plt.ylabel('Tingkat Inflasi')
plt.show()


# In[60]:


# Berdasarkan plot inflasi Indonesia di atas menunjukkan bahwa dari tahun ke tahun mengalami penurunan, meskipun terdapat sejumlah fluktuasi antara tahun 2007 dan 2008, di mana terjadinya krisis ekonomi global.
# Adapun tingkat inflasi tertinggi pada tahun 2006 yang mencapai angka 17.92. Sementara inflasi terendah pada tahun 2019 yang mencapai 2.4.
# Maka dapat diprediksi inflasi akan semakin menurun di tahun 2020 mendatang, Sementara berdasarkan rata-rata pertumbuhan IHK yang mempengaruhi inflasi, di mana permintaan barang dan jasa cenderung berkurang dan menyebabkan berkurangnya harga barang.


# In[ ]:




