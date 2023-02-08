import os
import pandas as pd
from matplotlib import pyplot as plt

dir_path = 'C:\\Users\\mmuhr-adm\\Desktop\\detgef data\\Rene_060223_02-06-2023_14-34-12\\Rene_060223_02-06-2023_14-34-12\\Rene_060223_02-06-2023_14-34-12.csv'

df = pd.read_csv(dir_path, delimiter=';', decimal=',')
df.set_index('time', inplace=True)
df['voltage_actual_ps'].plot()
plt.show()
# 

import plotly.express as px


fig = px.scatter(df, x=df.index, y="voltage_actual_ps", title='Life expectancy in Canada')
fig.show()