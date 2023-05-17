import pandas as pd
import os

folder = "C:/temp/JetpackStats"
stat_files = []

for root, dirs, files in os.walk(folder):
    for file in files:
        # print(file)
        if "monthly" in file:
            stat_files.append(f"{root}/{file}")

column_names=['Title','Views','Url','Month']
stats_df = pd.DataFrame(columns=column_names)

for file in stat_files:
    print(file)
    month = file[29:36]
    df = pd.read_csv(file, delimiter=',', header=None, names=['Title','Views','Url'])
    df['Month'] = month
    stats_df = pd.concat([stats_df, df.head(10)])

stats_df.to_csv('monthly_stats.csv', index=False)