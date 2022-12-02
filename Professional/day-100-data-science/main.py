import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv('NLSY97_subset.csv')
df1 = pd.read_csv('NLSY97_Variable_Names_and_Descriptions.csv')
# plt.xticks(fontsize=14)
# plt.yticks(fontsize=14)

# for column in df.columns:
#     plt.plot(df['EARNINGS'],df['BYEAR'],linewidth=1, label=df[column].name)
# plt.show()

# School years and Earnings
s_regression = LinearRegression()
school = df[['S', 'EARNINGS']]
sX = pd.DataFrame(school, columns=['EARNINGS'])
sy = school.drop(columns='EARNINGS')
s_regression.fit(sX,sy)
print(s_regression.score(sX,sy))

# coef
s_coef = pd.DataFrame(s_regression.coef_,sy.columns)
print(s_coef[0][0])
plt.figure(figsize=(8,4), dpi=100)
with sns.axes_style("whitegrid"):
  sns.regplot(data=df,
            x='S',
            y='EARNINGS',
            scatter_kws = {'alpha': 0.4},
            line_kws = {'color': 'black'})
plt.show()
