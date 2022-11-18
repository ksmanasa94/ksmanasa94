# %%
#Import Python Libraries
import numpy as np
import pandas as pd

# %%
input_file_path = r"C:\Users\19059\OneDrive\Documents\assignment4\youtube_dataset.csv"
df = pd.read_csv(input_file_path, encoding= 'unicode_escape')
df

# %%
# Creating a function to calculate the distribution of channeltype from the top 1000 records.
import seaborn as sns
def channel():
    x= df.iloc[:1000,:]['channeltype']
    print(x)
channel()

# %%
df_filtered = df.iloc[:1000,:]
df_filtered

# %%
df_filtered.to_csv("Filtered_Data.csv")
df_filtered

# %%
import matplotlib.pyplot as plt

def Distribution():
    sns.displot(df_filtered['channeltype'], kde=True)
Distribution()


