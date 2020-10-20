#!/usr/bin/env python
# coding: utf-8

# # ***Data Visualization of COVID-19 Confirmed Cases in the World***

# Note that these plots have been done after dropping the columns where 70% number of confirmed cases is zero.

# ### **Countrywise Plot**

# In[17]:


#imported all the required packages
import pandas as pd
import numpy as np
import seaborn as snb
import matplotlib.pyplot as plt



# In[18]:


#Specified the path to my dataset and loaded it in a dataframe
df_covid = pd.read_csv('https://raw.githubusercontent.com/Yogita98/Data-Visualization-of-Corona-Positive-Cases/master/time_series_2019-ncov-Confirmed.csv',index_col=0)
df_conti=pd.read_csv('https://raw.githubusercontent.com/Yogita98/Data-Visualization-of-Corona-Positive-Cases/master/c2c.csv')


# In[19]:


#Dropped the columns whose total number of positive cases on a particular day were less than 70%
for i in df_covid.columns:
  var=0.7*df_covid[i].count()
  if len(df_covid[df_covid[i]==0])>var:
    df_covid.drop([i],axis=1,inplace=True)
df_covid.columns


# In[20]:


column_list=[]
column_list=df_covid.columns
column_list


# In[21]:


country_dict=dict()
for i in range(487):
    # print(df.iloc[i][-1]) 
    # values of last column
    country_dict[df_covid.iloc[i][0]]=country_dict.get(df_covid.iloc[i][0],0)+df_covid.iloc[i][-1]
country_dict


# In[22]:


#The labels are computed in such a way that only those countries having Corona positive cummulatively 
#of all the days more than 1500 are plotted in the pie chart and the rest are combined and shown as Others. 
x=0
summ=0
country_labels=[]
country_sizes=[]
other_labels=[]
other_sizes=[]
for key,value in country_dict.items():
  if int(value)>=1500:
    country_labels.append(key)
    country_sizes.append(value)
  else:
    summ=summ+int(value)
country_labels.append('Others')
country_sizes.append(summ)
print(country_labels)
print(country_sizes)


# In[23]:


#Country wise plot of Corona positive cases
plt.rcParams.update({'font.size': 22})
fig = plt.figure(figsize=[40, 40])
ax = fig.add_subplot(111)
sizes=country_sizes
pie_wedge_collection = ax.pie(sizes, labels=country_labels, labeldistance=1.05,shadow=True)
for pie_wedge in pie_wedge_collection[0]:
    pie_wedge.set_edgecolor('white')
    

ax.set_title( "Figure 1: Country wise plot of Corona positive cases",fontsize=20)
ax.axis('equal')
ax.legend(loc='lower right',bbox_to_anchor=(1.2, 0.5),fontsize=20)


# ### **Datewise Plot**

# In[12]:


df_covid.columns


# In[24]:


#Computed the sum of Corona positive cases date wise and put it in a new row of the dataframe
drop_columns=['Lat', 'Long','Country/Region']
for i in range(0,len(drop_columns)):
  if drop_columns!=0:
    df_covid.drop(labels=drop_columns[i],axis=1,inplace=True)
    i=i-1
dates_list=[]
for col in df_covid.columns:
   dates_list.append(col)
print(dates_list)
df_covid.loc['Total'] = pd.Series(df_covid.sum())
datewise_sum=[]
for value in df_covid.iloc[-1].values:
  datewise_sum.append(value)
print(datewise_sum)


# In[14]:


#Date wise plot of Corona positive cases
plt.rcParams.update({'font.size': 10})
sizes=datewise_sum
labels=dates_list
fig = plt.figure(figsize=[20, 20])
ax = fig.add_subplot(111)
pie_wedge_collection = ax.pie(sizes, labels=labels, labeldistance=1.05)
for pie_wedge in pie_wedge_collection[0]:
    pie_wedge.set_edgecolor('white')
    

ax.set_title( "Figure 2: Datewise wise plot of Corona positive cases",fontsize=24)
ax.axis('equal')
ax.legend(loc='lower right',bbox_to_anchor=(1.2, 0.5),fontsize=10)


# ### **Continentwise Plot**

# In[15]:


continent_dict=dict()
for i in country_dict:
    temp=df_conti.loc[df_conti['Country']==i]
#     print(temp)
    if len(temp)>0:    
        continent_dict[temp.iloc[0][0]]=continent_dict.get(temp.iloc[0][0],0)+country_dict[i]
#         print(country_dict[i])
#         print(continent_dict.get(temp.iloc[0][0],0))
#         print("and")
#         print(continent_dict[temp.iloc[0][0]])

continent_dict


# In[16]:


plt.figure(figsize=(50,20))
plt.pie(continent_dict.values())
plt.title('Figure 3: Continentwise wise plot of Corona positive cases',size=24)
plt.legend(continent_dict.keys(),prop={'size': 15})
plt.show()


# In[ ]:





# In[ ]:




