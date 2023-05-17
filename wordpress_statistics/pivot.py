import pandas as pd

df = pd.read_csv('monthly_stats.csv')

pivot = df.pivot(index='Title', columns='Month', values='Views')

print(pivot)
pivot.to_csv('monthly_stats_pivot.csv', index=True)