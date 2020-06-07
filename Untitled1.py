#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt

plt.style.use('classic')
#fkmnthyfnbdysq способ построения
#w = 2
#h = 4
#d = 100
#plt.figure(figsize=(w,h), dpi=d)

#характеристика
means = (2, 2, 1, 1, 3, 3, 2, 3.3)
position = [0, 2, 4, 6, 8, 10, 12, 14]
std = (0.2, 0.5, 0.1, 0.6, 0.3, 0.5, 0.4, 0.3)
#подписи
plt.title('Simple')
plt.xlabel('postmonopause ')
plt.ylabel('present positive cells ')

plt.bar(position, means, color="w", yerr=std)
plt.savefig("out.png")



# In[ ]:




