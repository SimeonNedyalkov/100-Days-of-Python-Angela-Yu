import numpy as np

import pandas as pd

import plotly.express as px

import matplotlib.pyplot as plt

import seaborn as sns



# These might be helpful:


from datetime import datetime, timedelta


df_data = pd.read_csv('mission_launches.csv')

columns = df_data.columns

questions = ['Who launched the most missions in any given year?',

'How has the cost of a space mission varied over time?',

'Which months are the most popular for launches?',

'Have space missions gotten safer or has the chance of failure remained unchanged?',]

success_missions = df_data.Mission_Status.value_counts().Success

failure_missions = df_data.Mission_Status.value_counts().Failure

#numberOfFailure = df_data[df_data["Mission_Status"] == "Failure"].CountryCodes.value_counts()
df_data.isna()
df_data = df_data.dropna()
org_values = df_data.Organisation.value_counts()
date = df_data.Date.value_counts()



years = []

for i in df_data.Date:

    years.append(i.split(",")[1].split(" ")[1])



df_data["Year"] = years


df_data.groupby(["Year"]).agg({"Mission_Status":pd.Series.value_counts})

df_data["Price"] = df_data["Price"].replace(",","", regex=True)

df_data["Price"] = df_data["Price"].astype(float)



x = df_data.groupby(["Year"]).agg({"Price":pd.Series.sum}).index

y = df_data.groupby(["Year"]).agg({"Price":pd.Series.sum}).values



plt.figure(figsize=(20,8))

plt.xticks(rotation=45)

plt.plot(x,y)
plt.show()

months = []

for i in df_data.Date:

    months.append(i.split(",")[0].split(" ")[1])



df_data["Months"] = months


print(df_data.groupby(["Months"]).agg({"Mission_Status":pd.Series.value_counts}))

print(df_data.groupby(['Year']).agg({'Mission_Status':pd.Series.value_counts}))
