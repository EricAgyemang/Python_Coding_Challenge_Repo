#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Problem 1
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

x = np.arange(-8,8.1,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,'g--',label='sin(x)')
plt.plot(x,y2,'o',color='r',label='cos(x)')
plt.legend(loc='best')
plt.xlim([-10,10])
plt.ylim([-2,2])


# In[8]:


#Problem2

from matplotlib import pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')

#IMPORT THE DATA SET
df = pd.read_csv('tips.csv')
fig = plt.figure()

# PLOT 1
ax1 = fig.add_subplot(2,2,1)
ax1.hist(df['tip'], bins=10,alpha=0.3,color='g')

# PLOT 2
ax2 = fig.add_subplot(2,2,2)
grouped = df['day'].groupby(df['day'])
grouped.keys.value_counts().plot(kind='bar',rot=360)

# PLOT 3
ax3 = fig.add_subplot(2,2,3)
df['tip'].plot.box()

# PLOT 4
ax4 = fig.add_subplot(2,2,4)
df['size'].hist()


# In[ ]:





# In[ ]:


#Problem 3


# In[9]:


#1
df_AAPL = pd.read_csv('AAPL.csv', index_col = "Date")
print("For Apple:")
print(df_AAPL.head(1))
df_IBM = pd.read_csv('IBM.csv', index_col = "Date")
print("For IBM:")
print(df_IBM.head(1))
df_MSFT = pd.read_csv('MSFT.csv', index_col = "Date")
print("For Microsoft:")
print(df_MSFT.head(1))
df_GOOG = pd.read_csv('GOOG.csv', index_col = "Date")
print("For Google:")
print(df_GOOG.head(1))


# In[10]:


#2 
import matplotlib.ticker as ticker
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
ax1.plot(df_AAPL['High'])
ax1.xaxis.set_major_locator(ticker.NullLocator()) #no xticks
#ax1.yaxis.set_major_locator(ticker.NullLocator()) #no yticks
ax2.scatter(df_IBM.index, df_IBM['Low'])
ax2.xaxis.set_major_locator(ticker.NullLocator()) #no xticks
ax3.hist(df_MSFT['Close'])
ax3.xaxis.set_major_locator(ticker.NullLocator()) #no xticks
ax4.hist(df_GOOG['Adj Close'])
ax4.xaxis.set_major_locator(ticker.NullLocator()) #no xticks


# In[11]:


#3
#Uses index as x-axis by default.
df_AAPL.plot(y = ["High", "Low"])


# In[12]:


#4
df_AAPL[['High', 'Low']].plot.box()


# In[ ]:




