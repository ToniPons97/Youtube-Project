import pandas as pd
import main


def dict_to_df(data):
    return pd.DataFrame(data)

     

def df_to_csv(data):
    data.to_csv('../output/youtube.csv', index=False)
    return "CSV successfully exported!"

def show_all_columns(data):
    return data.columns


def show_specified_columns(data, word):
    return data[[word]]



