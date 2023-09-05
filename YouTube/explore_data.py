import pandas as pd

# df = pd.read_csv('ndc_talks_youtube.csv')
df = pd.read_csv('ndc_talks_manually_fixed.csv')
# print(df.info())
# print("==" * 40)
print(df['Conference'].value_counts())
# print("==" * 40)
# print(df['Duration in Minutes'].value_counts())
# print("==" * 40)
# print(df.describe())