import pandas as pd

file_a = 'ndc_talks_manualy_fixed.csv'
file_b = 'ndc_talks_youtube.csv'

df_a = pd.read_csv(file_a)
df_b = pd.read_csv(file_b)

extended = pd.concat([df_a,df_b['DurationInMinutes']], axis = 1)

moved = extended[['Published', 'Type', 'Conference', 'Title', 'Speaker', 'Duration', 'DurationInMinutes', 'Link']]

moved.to_csv('ndc_talks_extended.csv', index=False)