import pandas as pd
import main


def dict_to_df(data):
    return pd.DataFrame(data)

     

#def df_to_csv(file_name):
#    return pd.to_csv(file_name, sep='\t', encoding='utf-8', index=False)


def show_all_columns(data):
    return data.columns


def show_specified_columns(data, *args):
    return data[[args]]



