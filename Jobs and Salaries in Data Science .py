#!/usr/bin/env python
# coding: utf-8

# ### Jobs and Salaries in Data Science

# ### Introduction

# In[1]:


# this project about jobs an salaries in data science 
# i will use data vsualization to analysis this data to become easy for all people to understand it 
# i hope to make it easy for you 
# don,t forget encourage me to keep going 


#  ### Technologies

# In[2]:


# numpy 
# pandas 
# matplotlib 
# seaborn 
# handling data 


# ### Setup
# 

# In[21]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import category_encoders as ce
import plotly.express as px


# ### let,s read our data 

# In[4]:


data = pd.read_csv("C:/Users/LAP ME/Downloads/jobs_in_data.csv")


# ### let,s describe our data 

# In[5]:


data.describe()


# ### let,s get imformation about our data 

# In[6]:


data.info()


# ### let,s take copy from our data to analysis it and  keep the original data 

# In[7]:


data1 = data.copy


# ### missing value 

# In[15]:


data.isna().sum()


# In[16]:


data.head()


# In[17]:


data.columns


# In[18]:


data["work_year"].unique()


# In[19]:


data.shape


# In[22]:


fig1 = px.scatter(data, y='experience_level', x='salary_in_usd', title='Simple Scatter Plot')
fig1.show()


# In[23]:


fig2 = px.scatter(data, x= 'salary', y='job_category')
fig2.show()


# In[33]:


fig = px.scatter(data, x= 'salary', y='job_category')
fig.show()


# In[35]:


salary_trends = data.groupby("work_year")["salary_in_usd"].mean()
plt.plot(salary_trends.index, salary_trends.values, color="deepskyblue", linewidth=6)
plt.title("The Dance of Salaries Over Time", fontsize=22, fontweight="bold")
plt.show()


# In[40]:


# Calculate the top 10 job categories based on average salary
top_job_categories = data.groupby('job_category')['salary_in_usd'].mean().sort_values(ascending=False).head(10).index

# Filter the DataFrame to include only the top 10 job categories
df_top10 = data[data['job_category'].isin(top_job_categories)]

# Plot the bar chart for the top 10 job categories
sns.set_style("whitegrid")
sns.barplot(x="job_category", y="salary_in_usd", data=df_top10, palette="viridis")
plt.title("Top 10 Job Categories: Salary Distribution", fontsize=16, fontweight="bold")
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.show()


# In[41]:


fig_1 = px.bar(data, x="job_category", y="salary_in_usd", color="job_category",
               title="Job Categories: A Symphony of Different Income Levels",
               color_continuous_scale='darkmint')
fig_1.update_layout(xaxis=dict(tickangle=45, tickmode='array', tickvals=list(data['job_category']), ticktext=list(data['job_category'])))
fig_1.show()


# In[55]:


sns.relplot(x = "salary", y = "employment_type", data = data)
plt.show()


# In[54]:


data.head(1)


# In[56]:


sns.violinplot(x = "salary", y = "employment_type", data = data)
plt.show()


# In[57]:


sns.countplot(x = 'salary' , data = data)
plt.show()


# In[59]:


sns.kdeplot(x = "salary", y = "salary_in_usd", data = data)
plt.show()


# In[60]:


sns.regplot(x = "salary", y = "salary_in_usd", data = data)
plt.show()


# In[61]:


sns.pairplot(data = data, hue = "salary")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




