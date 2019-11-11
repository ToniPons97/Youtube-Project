import pandas as pd
import main

df = pd.read_csv("../input/USvideos.csv")
print(df.head())

def dict_to_df(data):
    df = pd.DataFrame(data)
    print("Shape of DataFrame", df.shape)
    return df
     

def df_to_csv(file_name):
    return df.to_csv(file_name, sep='\t', encoding='utf-8', index=False)
