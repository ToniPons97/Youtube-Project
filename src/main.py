#!/usr/local/bin/python3
import api
import sys
import argparse
import subprocess
import clean
import sending_email as se

def recieveConfig():
    parser = argparse.ArgumentParser(description='Youtube data extractor')
    parser.add_argument('-s', '--search', help='Make a Youtube search by doing --search <keyword>.')
    parser.add_argument('-n', '--number', help='Specify maximum number of results to obtain in request', default=25)
    parser.add_argument('-sac', '--showAllCols', help='Prints list of all existing columns in DataFrame (Admitted values: True, False.)', default=False)
    parser.add_argument('-sc','--showColumn', help='Prints one or specified column.', default=False)
    parser.add_argument('-scsv', '--saveCsv', help='Converts DataFrame to a csv file and stores it in specified path.', default=False)
    parser.add_argument('-se', '--sendEmail', help='Sends csv generated from data extraction', default=False)
    args = parser.parse_args()
    return args

def main():
    
    print("Youtube Data Extractor!!!")
    config = recieveConfig()
    query = api.search_videos_by_keyword(api.service, q=config.search, part='id,snippet', eventType='completed', type='video', order='viewCount', maxResults=config.number)
    generated_df = clean.dict_to_df(query)
    print(generated_df)
    
    if config.showAllCols:
        columns  = clean.show_all_columns(generated_df)
        print(columns)
    if config.showColumn:
        specified_cols = clean.show_specified_columns(generated_df, config.showColumn)
        print(specified_cols)
    if config.saveCsv:
        csv = clean.df_to_csv(generated_df)
        print(csv)
    if config.sendEmail:
        se.send_email_with_file()
        print("Email successfuly sent!")
    else:
        pass



if __name__=="__main__":
    main()
