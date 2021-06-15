#!/usr/bin/env python
# coding: utf-8

# In[1]:



# -----> As this projet contains data from the WHO and the WB, we can suggest action to these 
# organizations based on our findings with the overall goal of increasing life expectancy. Or, at the very least, since
# these organizations have a much better grasp on the current situations in the countries of interest than a data analyst,
# we will be providing them with tangible, usable data visualizations from which they can base 
# their own research and planing.

# Codecademy's suggestions:

# - Has life expectancy increased over time in the six nations? --> Yes
# - Has GDP increased over time in the six nations? --> Yes
# - Is there a correlation between GDP and life expectancy of a country? --> Yes
# - What is the average life expectancy in these nations? --> Plotted
# - What is the distribution of that life expectancy? --> Plotted


# In[3]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[35]:


df = pd.read_csv("all_data.csv")
df.rename(columns={"Life expectancy at birth (years)": "Life Expectancy"}, inplace=True)
df['GDP'] = df['GDP'].apply(lambda x: x/1000000000)

# All GDP values represented in billions for ease of readability

print(df.head())


# # Plot Life Expectancy Over Time For 6 Nations:

# In[33]:


chile = df[df.Country == "Chile"]
china = df[df.Country == "China"]
germany = df[df.Country == "Germany"]
mexico = df[df.Country == "Mexico"]
usa = df[df.Country == "United States of America"]
zimbabwe = df[df.Country == "Zimbabwe"]

ax1 = plt.subplot(2, 3, 1)
ax1.plot(chile['Year'], chile['Life Expectancy'])
plt.title("Chile")

ax1 = plt.subplot(2, 3, 2)
ax1.plot(china['Year'], china['Life Expectancy'], color='green')
plt.title("China")

ax1 = plt.subplot(2, 3, 3)
ax1.plot(germany['Year'], germany['Life Expectancy'], color='m')
plt.title("Germany")

ax1 = plt.subplot(2, 3, 4)
ax1.plot(mexico['Year'], mexico['Life Expectancy'], color='r')
plt.title("Mexico")

ax1 = plt.subplot(2, 3, 5)
ax1.plot(usa['Year'], usa['Life Expectancy'], color='c')
plt.title("United States")

ax1 = plt.subplot(2, 3, 6)
ax1.plot(zimbabwe['Year'], zimbabwe['Life Expectancy'], color='k')
plt.title("Zimbabwe")

plt.tight_layout()


# In[ ]:


# The above graphs show that life expectancy has steadily increased for all 6 nations in the dataset over 15 years.


# # Plot GDP Over Time For 6 Nations:

# In[36]:


ax1 = plt.subplot(2, 3, 1)
ax1.plot(chile['Year'], chile['GDP'])
plt.title("Chile")

ax1 = plt.subplot(2, 3, 2)
ax1.plot(china['Year'], china['GDP'], color='green')
plt.title("China")

ax1 = plt.subplot(2, 3, 3)
ax1.plot(germany['Year'], germany['GDP'], color='m')
plt.title("Germany")

ax1 = plt.subplot(2, 3, 4)
ax1.plot(mexico['Year'], mexico['GDP'], color='r')
plt.title("Mexico")

ax1 = plt.subplot(2, 3, 5)
ax1.plot(usa['Year'], usa['GDP'], color='c')
plt.title("United States")

ax1 = plt.subplot(2, 3, 6)
ax1.plot(zimbabwe['Year'], zimbabwe['GDP'], color='k')
plt.title("Zimbabwe")

plt.tight_layout()


# In[ ]:


# The above graphs show that GDP has also increased for all 6 nations in the dataset over 15 years, with some fluctuations.


# # Plot GDP v.s. Life Expectancy For 6 Nations:

# In[37]:


ax1 = plt.subplot(2, 3, 1)
ax1.plot(chile['GDP'], chile['Life Expectancy'])
plt.title("Chile")

ax1 = plt.subplot(2, 3, 2)
ax1.plot(china['GDP'], china['Life Expectancy'], color='green')
plt.title("China")

ax1 = plt.subplot(2, 3, 3)
ax1.plot(germany['GDP'], germany['Life Expectancy'], color='m')
plt.title("Germany")

ax1 = plt.subplot(2, 3, 4)
ax1.plot(mexico['GDP'], mexico['Life Expectancy'], color='r')
plt.title("Mexico")

ax1 = plt.subplot(2, 3, 5)
ax1.plot(usa['GDP'], usa['Life Expectancy'], color='c')
plt.title("United States")

ax1 = plt.subplot(2, 3, 6)
ax1.plot(zimbabwe['GDP'], zimbabwe['Life Expectancy'], color='k')
plt.title("Zimbabwe")

plt.tight_layout()


# In[ ]:


# # The above graphs show that life expectancy and GDP are positively correlated.


# # Average Life Expectancies for Each Nation 

# In[46]:


plt.figure(figsize=(10, 6))
sns.barplot(x="Country", y="Life Expectancy", data=df)
plt.title("Average Life Expectancy per Country")
plt.ylim(40, 83)
plt.show()


# In[47]:


plt.figure(figsize=(10, 6))
sns.boxplot(x="Country", y="Life Expectancy", data=df)
plt.title("Average Life Expectancy per Country Distribution")
plt.ylim(40, 83)
plt.show()


# In[ ]:


# The above graphs show that average life expectancies for the 6 nations in the dataset are relatively similar with the
# exception of Zimbabwe, whose life expectancy is much lower and has a much wider distribution.

