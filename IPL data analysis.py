#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[24]:


data = pd.read_csv("IPLData.csv")


# In[25]:


data


# In[26]:


data.describe()


# In[27]:


data.isna().sum()


# In[28]:


data.info()


# In[29]:


#cleaning the data
# capped - batters,bowlers,allrounders,wicket keeper (playing the ipl in first time)
# uncapped - batters,bowlers,allrounders,wicket keeper


# In[30]:


#segregating data - capped batters
batters = data.loc[(data["Player_Type"]=="Batter")]
batters_new = batters.loc[(batters["Capped"]==1)]
Capped_batters = batters_new[['Player Name','Team','Nationality','Matches_Played','Runs','Average','Strike_Rate']]


# In[31]:


Capped_batters.head()


# In[41]:


#segregating data - capped bowlers
bowlers = data.loc[(data["Player_Type"]=="Bowler ")]
bowlers_new = bowlers.loc[(bowlers["Capped"]==1)]
Capped_bowlers = bowlers_new[['Player Name','Team','Nationality','Matches_Played',
                              'Wickets','Bowling_average','Economy','Bowling_Strike_Rate']]


# In[42]:


Capped_bowlers.head()


# In[45]:


#segregating data - capped Keeper
Keepers = data.loc[(data["Player_Type"]=="Keeper")]
Keepers_new = Keepers.loc[(Keepers["Capped"]==1)]
Capped_Keepers = Keepers_new[['Player Name','Team','Nationality','Matches_Played','Runs',
                              'Average','Strike_Rate','Catches','Run_outs','Stumps']]


# In[46]:


Capped_Keepers.head()


# In[47]:


#segregating data - capped Allrounders
Allrounders = data.loc[(data["Player_Type"]=="Allrounder")]
Allrounders_new = Allrounders.loc[(Allrounders["Capped"]==1)]
Capped_Allrounders = Allrounders_new[['Player Name','Team','Nationality','Matches_Played','Runs','Average','Strike_Rate',
                                     'Wickets','Bowling_average','Economy','Bowling_Strike_Rate']]


# In[48]:


Capped_Allrounders.head()


# In[49]:


#cleaning the data by none or NAN values 0
Capped_batters = Capped_batters.fillna(0)
Capped_bowlers = Capped_bowlers.fillna(0)
Capped_Keepers = Capped_Keepers.fillna(0)
Capped_Allrounders = Capped_Allrounders.fillna(0)


# In[51]:


#cheaking the na values in the dataset
print(Capped_batters.isna().sum())
print(Capped_bowlers.isna().sum())
print(Capped_Keepers.isna().sum())
print(Capped_Allrounders.isna().sum())


# # Initial Analysis

# In[53]:


top_batters = Capped_batters.loc[(Capped_batters["Average"]>=32.0)]

#sorting data
top_batters_average = top_batters.sort_values("Average",ascending=False)
top_batters_runs = top_batters.sort_values("Runs",ascending=False)
top_batters_strike_rate = top_batters.sort_values("Strike_Rate",ascending=False)
top_batters_matches = top_batters.sort_values("Matches_Played",ascending=False)


# In[54]:


top_batters_average


# In[55]:


top_batters_runs


# In[56]:


top_batters_strike_rate


# In[57]:


top_batters_matches


# top 3 batters
# 1.David warner
# 2.KL Rahul
# 3.Virat Kohli

# In[61]:


top_bowlers = Capped_bowlers.loc[(Capped_bowlers["Bowling_average"]<=24.0)]

top_bowlers_average = top_bowlers.sort_values("Bowling_average")
top_bowlers_strike_rate = top_bowlers.sort_values("Bowling_Strike_Rate")
top_bowlers_wickets = top_bowlers.sort_values("Wickets",ascending=False)
top_bowlers_economy = top_bowlers.sort_values("Economy")
top_bowlers_matches = top_bowlers.sort_values("Matches_Played",ascending=False)


# In[62]:


top_bowlers_average


# In[63]:


top_bowlers_strike_rate


# In[64]:


top_bowlers_wickets


# In[65]:


top_bowlers_economy


# In[66]:


top_bowlers_matches


# top bowlers
# 1.Kagiso Rabada
# 2.Jasprit Bumrah
# 3.Yuzvendra Chahal
# 4.Nathan Coulter-Nile

# In[67]:


top_allrounders = Capped_Allrounders.loc[(Capped_Allrounders["Strike_Rate"]>=140.0)]

top_allrounders_average = top_allrounders.sort_values("Average",ascending=False)
top_allrounders_strike_rate = top_allrounders.sort_values("Strike_Rate",ascending=False)
top_allrounders_runs = top_allrounders.sort_values("Runs",ascending=False)
top_allrounders_bowling_average = top_allrounders.sort_values("Bowling_average")
top_allrounders_bowling_strike_rate = top_allrounders.sort_values("Bowling_Strike_Rate")
top_allrounders_wickets = top_allrounders.sort_values("Wickets",ascending=False)
top_allrounders_economy = top_allrounders.sort_values("Economy")
top_allrounders_matches = top_allrounders.sort_values("Matches_Played",ascending=False)


# In[68]:


top_allrounders_average


# In[69]:


top_allrounders_strike_rate


# In[70]:


top_allrounders_runs


# In[71]:


top_allrounders_bowling_average


# In[72]:


top_allrounders_bowling_strike_rate


# In[73]:


top_allrounders_wickets


# In[74]:


top_allrounders_economy


# In[75]:


top_allrounders_matches


# 1.Andre Russell
# 2.Sunil Narine
# 3.Hardik Pandya
# 4.Jofra Archer

# In[77]:


top_keepers = Capped_Keepers.loc[(Capped_Keepers["Average"]>=25.0)]

top_keepers_average = top_keepers.sort_values("Average",ascending=False)
top_keepers_strike_rate = top_keepers.sort_values("Strike_Rate",ascending=False)
top_keepers_runs = top_keepers.sort_values("Runs",ascending=False)
top_keepers_catches = top_keepers.sort_values("Catches",ascending=False)
top_keepers_run_outs = top_keepers.sort_values("Run_outs",ascending=False)
top_keepers_stumps = top_keepers.sort_values("Stumps",ascending=False)
top_keepers_matches = top_keepers.sort_values("Matches_Played",ascending=False)


# In[78]:


top_keepers_average


# In[79]:


top_keepers_strike_rate


# In[80]:


top_keepers_runs


# In[81]:


top_keepers_catches


# In[82]:


top_keepers_run_outs


# In[83]:


top_keepers_stumps


# In[84]:


top_keepers_matches


# 1.MS Doni
# 2.Dinesh Karthik
# 3.Rishabh Pant	

# # Visualization

# In[87]:


#batters data
plt.figure(figsize=(15,5))
sns.barplot(x='Player Name',y='Strike_Rate',data=top_batters)


# In[90]:


plt.figure(figsize=(15,5))
sns.barplot(x='Player Name',y='Runs',data=top_batters)


# In[91]:


plt.figure(figsize=(15,5))
sns.barplot(x='Player Name',y='Average',data=top_batters)


# In[93]:


plt.figure(figsize=(15,5))
sns.barplot(x='Player Name',y='Matches_Played',data=top_batters)


# In[96]:


#bowlers data
plt.figure(figsize=(20,5))
sns.barplot(x='Player Name',y='Bowling_average',data=top_bowlers)


# In[97]:


plt.figure(figsize=(20,5))
sns.barplot(x='Player Name',y='Bowling_Strike_Rate',data=top_bowlers)


# In[98]:


plt.figure(figsize=(20,5))
sns.barplot(x='Player Name',y='Wickets',data=top_bowlers)


# In[99]:


plt.figure(figsize=(20,5))
sns.barplot(x='Player Name',y='Economy',data=top_bowlers)


# In[102]:


plt.figure(figsize=(20,5))
sns.barplot(x='Player Name',y='Matches_Played',data=top_bowlers)


# In[ ]:


top_allrounders = Capped_Allrounders.loc[(Capped_Allrounders["Strike_Rate"]>=140.0)]

top_allrounders_average = top_allrounders.sort_values("Average",ascending=False)
top_allrounders_strike_rate = top_allrounders.sort_values("Strike_Rate",ascending=False)
top_allrounders_runs = top_allrounders.sort_values("Runs",ascending=False)
top_allrounders_bowling_average = top_allrounders.sort_values("Bowling_average")
top_allrounders_bowling_strike_rate = top_allrounders.sort_values("Bowling_Strike_Rate")
top_allrounders_wickets = top_allrounders.sort_values("Wickets",ascending=False)
top_allrounders_economy = top_allrounders.sort_values("Economy")
top_allrounders_matches = top_allrounders.sort_values("Matches_Played",ascending=False)


# In[103]:


#Allrounder data
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name',y='Average',data=top_allrounders)


# In[104]:


plt.figure(figsize=(20,10))
sns.barplot(x='Player Name',y='Strike_Rate',data=top_allrounders)


# In[105]:


plt.figure(figsize=(20,10))
sns.barplot(x='Player Name',y='Runs',data=top_allrounders)


# In[106]:


plt.figure(figsize=(20,10))
sns.barplot(x='Player Name',y='Bowling_average',data=top_allrounders)


# In[107]:


plt.figure(figsize=(20,10))
sns.barplot(x='Player Name',y='Bowling_Strike_Rate',data=top_allrounders)


# In[108]:


plt.figure(figsize=(20,10))
sns.barplot(x='Player Name',y='Wickets',data=top_allrounders)


# In[109]:


plt.figure(figsize=(20,10))
sns.barplot(x='Player Name',y='Economy',data=top_allrounders)


# In[110]:


plt.figure(figsize=(20,10))
sns.barplot(x='Player Name',y='Matches_Played',data=top_allrounders)


# In[111]:


#keepers data
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name',y='Average',data=top_keepers)


# In[112]:


plt.figure(figsize=(20,10))
sns.barplot(x='Player Name',y='Strike_Rate',data=top_keepers)


# In[113]:


plt.figure(figsize=(20,10))
sns.barplot(x='Player Name',y='Runs',data=top_keepers)


# In[114]:


plt.figure(figsize=(20,10))
sns.barplot(x='Player Name',y='Catches',data=top_keepers)


# In[115]:


plt.figure(figsize=(20,10))
sns.barplot(x='Player Name',y='Run_outs',data=top_keepers)


# In[116]:


plt.figure(figsize=(20,10))
sns.barplot(x='Player Name',y='Stumps',data=top_keepers)


# In[117]:


plt.figure(figsize=(20,10))
sns.barplot(x='Player Name',y='Matches_Played',data=top_keepers)


# In[150]:


top_bowlers.reset_index(drop=True)


# In[157]:


batter1 = top_batters.loc[(top_batters["Player Name"]=="KL Rahul ")]
batter2 = top_batters.loc[(top_batters["Player Name"]=="David Warner ")]
batter3 = top_batters.loc[(top_batters["Player Name"]=="Virat Kohli")]

bowler1 = top_bowlers.loc[(top_bowlers["Player Name"]=="Yuzvendra Chahal ")]
bowler2 = top_bowlers.loc[(top_bowlers["Player Name"]=="Jasprit Bumrah")]
bowler3 = top_bowlers.loc[(top_bowlers["Player Name"]=="Nathan Coulter-Nile")]
bowler4 = top_bowlers.loc[(top_bowlers["Player Name"]=="Kagiso Rabada ")]

allrounder1 = top_allrounders.loc[(top_allrounders["Player Name"]=="Andre Russell")]
allrounder2 = top_allrounders.loc[(top_allrounders["Player Name"]=="Sunil Narine ")]
allrounder3 = top_allrounders.loc[(top_allrounders["Player Name"]=="Hardik Pandya")]

keeper = top_keepers.loc[(top_keepers["Player Name"]=="MS Dhoni")]

print(batter1)


# In[158]:


Final = [batter1, batter2, batter3, allrounder1, allrounder2, allrounder3, bowler1, bowler2, bowler3, bowler4, keeper]
final_team = pd.concat(Final)
final_team = final_team.drop(labels = ['Matches_Played','Runs','Average','Strike_Rate','Wickets','Bowling_average','Economy',
                                      'Bowling_Strike_Rate','Catches','Run_outs','Stumps'],axis=1)
final_team.reset_index(drop=True)


# In[ ]:




