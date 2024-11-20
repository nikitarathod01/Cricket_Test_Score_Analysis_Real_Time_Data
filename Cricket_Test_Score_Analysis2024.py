#!/usr/bin/env python
# coding: utf-8

# In[84]:


#Firts we have to import the necessary libraries.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[85]:


# Now we have to import the data to process further.


# In[86]:


df = pd.read_csv('CricketTestMatchData.csv')


# In[87]:


df


# In[88]:


# For more correct understanding of the columns in the data, we have to rename some of the columns here.


# In[89]:


df = df.rename(columns = {'Mat':'Matches','NO':'Not_outs','HS':'Highest_Inns_Score','BF':'Balls_Faced','SR':'Batting_Strike_Rate'})


# In[90]:


df.head(5)


# In[91]:


# The next step is to find out the any null values in the data.


# In[92]:


df.isnull().any()


# In[93]:


# As we can see in the above list there are some null values in the data, so we have to find them first.


# In[94]:


df[df['Balls_Faced'].isna()==1]


# In[95]:


# Now we have to fill the null values with the zeros.


# In[96]:


df['Balls_Faced']=df['Balls_Faced'].fillna(0)


# In[97]:


df[df['Player']=='ED Weekes (WI)']


# In[98]:


df[df['Player']=='CL Walcott (WI)']


# In[99]:


df[df['Player']=='Hon.FS Jackson (ENG)']


# In[100]:


# The next step is find out the duplicates in the data.


# In[101]:


df.duplicated()


# In[102]:


# So we find out some duplicates here.


# In[103]:


df[df['Player'].duplicated()==1]


# In[104]:


df[df['Player'].isin(['GA Headley (WI)','WR Hammond (ENG)','JB Hobbs (ENG)','V Sehwag (ICC/IND)'])]


# In[105]:


# Drop the duplicates.


# In[106]:


df=df.drop_duplicates()


# In[107]:


df[df['Player'].isin(['GA Headley (WI)','WR Hammond (ENG)','JB Hobbs (ENG)','V Sehwag (ICC/IND)'])]


# In[108]:


#Split up the span into start and end dates + Career length


# In[109]:


df['Span'].str.split(pat = '-')


# In[110]:


df['Span'].str.split(pat = '-').str[1]


# In[111]:


df['Rookie_Year'] = df['Span'].str.split(pat = '-').str[0]


# In[112]:


df['Final_Year'] = df['Span'].str.split(pat = '-').str[1]


# In[113]:


df


# In[114]:


#Drop Span columns


# In[115]:


df= df.drop(['Span'], axis = 1)


# In[116]:


df.head()


# In[117]:


# Split up the country from the player (as we can see in the data that country of the player is attached to the name of the player.)


# In[118]:


df['Player'].str.split(pat = '(')


# In[119]:


df['Country'] = df['Player'].str.split(pat = '(').str[1]


# In[120]:


df['Country'] = df['Country'].str.split(pat = ')').str[0]


# In[121]:


df['Country']


# In[122]:


df['Player'] = df['Player'].str.split(pat = '(').str[0]


# In[123]:


df.head()


# In[124]:


# Change the datatypes 


# In[125]:


df.dtypes


# In[126]:


df['Highest_Inns_Score'].str.split(pat = '*').str[0]


# In[127]:


df['Highest_Inns_Score'] = df['Highest_Inns_Score'].str.split(pat = '*').str[0]


# In[128]:


df['Highest_Inns_Score'] = df['Highest_Inns_Score'].astype('int')


# In[129]:


df['Highest_Inns_Score'].astype('int')


# In[130]:


df.dtypes


# In[131]:


df = df.astype({'Rookie_Year':'int','Final_Year':'int' })


# In[132]:


df.dtypes


# In[133]:


df.head()


# In[134]:


df['Batting_Strike_Rate'] = df['Batting_Strike_Rate'].astype('int')


# In[135]:


df.dtypes


# In[136]:


df['Balls_Faced'] = df['Balls_Faced'].str.split(pat = '+').str[0]


# In[137]:


df[df['Balls_Faced'].isna()==1]


# In[138]:


df['Balls_Faced']=df['Balls_Faced'].fillna(0)


# In[139]:


df['Balls_Faced'] = df['Balls_Faced'].astype('int')


# In[140]:


df.dtypes


# In[141]:


pd.set_option('display.max_rows', None)


# In[142]:


df


# In[143]:


df.isnull().any()


# In[144]:


df.dtypes


# In[145]:


df['4s'] = df['4s'].str.split(pat = '+').str[0]


# In[146]:


df['4s'] = df['4s'].astype('int')


# In[147]:


df.dtypes


# In[148]:


df['6s'] = df['6s'].str.split(pat = '+').str[0]


# In[149]:


df['6s'] = df['6s'].astype('int')


# In[150]:


df.dtypes


# In[151]:


# Build out the career length column 


# In[152]:


df['Career_Length'] =  df['Final_Year'] - df['Rookie_Year']


# In[153]:


df


# In[154]:


#Calculations with the dataframe 
# Cricketers in this DF What is the average Career Lenght 


# In[156]:


df['Career_Length'].mean()


# In[157]:


# Average Batting_Strike_Rate for the Cricketers who played more than the 10 years.


# In[161]:


df[df['Career_Length']>10]['Batting_Strike_Rate'].mean()


# In[162]:


# Find the number of the cricketers who played before the 1960's.


# In[165]:


df[df['Rookie_Year']>1960]['Player'].count()


# In[166]:


#Max highest Innings scored by the country.


# In[167]:


df.groupby('Country')['Highest_Inns_Score'].max()


# In[170]:


df.groupby('Country')['Highest_Inns_Score'].max().to_frame('Highest_Inns_Score').reset_index().sort_values('Highest_Inns_Score',ascending = False)


# In[171]:


# Hundreds, fifties and ducks(0) AVG by Country.


# In[172]:


df.groupby('Country')[['100', '50', '0']].mean()


# In[ ]:




