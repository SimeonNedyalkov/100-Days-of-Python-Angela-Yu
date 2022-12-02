import numpy as np

import pandas as pd

import plotly.express as px

import matplotlib.pyplot as plt

import seaborn as sns

df_deaths_by_police_us = pd.read_csv('Deaths_by_Police_US.csv',encoding='cp1252')
df_median_household_income_2015 = pd.read_csv('Median_Household_Income_2015.csv',encoding='cp1252')
df_share_of_race_by_city = pd.read_csv('Share_of_Race_By_City.csv',encoding='cp1252')
df_complete_high_school = pd.read_csv('Pct_Over_25_Completed_High_School.csv',encoding='cp1252')
df_people_below_poverty_level = pd.read_csv('Pct_People_Below_Poverty_Level.csv',encoding='cp1252')

df_median_household_income_2015.isna()
df_median_household_income_2015 = df_median_household_income_2015.dropna()
#print(df_median_household_income_2015['Median Income'].min())
#print(df_median_household_income_2015['Geographic Area'])
state_with_most_kills = df_deaths_by_police_us["state"].value_counts()
print(state_with_most_kills)
print(df_median_household_income_2015.loc[df_median_household_income_2015['Geographic Area'] == 'CA'])
print(df_complete_high_school.loc[df_complete_high_school['Geographic Area'] == 'CA'])
print(df_people_below_poverty_level.loc[df_people_below_poverty_level['Geographic Area'] == 'CA'])
print(df_share_of_race_by_city.loc[df_share_of_race_by_city['Geographic area'] == 'CA'])
grouped_races = df_share_of_race_by_city.groupby('Geographic area').value_counts()
# More Black and hispanic people in CA than white
print(f'White people:{grouped_races.groupby("share_white").value_counts().mean()}')
print(f'Black people:{grouped_races.groupby("share_black").value_counts().mean()}')
print(f'Hispanic people:{grouped_races.groupby("share_hispanic").sum().mean()}')
print(f'Asian people:{grouped_races.groupby("share_asian").sum().mean()}')
