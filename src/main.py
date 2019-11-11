#!/usr/local/bin/python3
import api
import sys
import argparse
import subprocess
import clean

def recieveConfig():
    parser = argparse.ArgumentParser(description='Youtube data extractor')
    parser.add_argument('-s', '--search', help='Make a Youtube search by doing --search <keyword>.')
    parser.add_argument('-n', '--number', help='Specify maximum number of results to obtain in request', default=25)        
    args = parser.parse_args()
    return args

def main():
    
    print("Youtube Data Extractor!!!")
    config = recieveConfig()
    
  
    query = api.search_videos_by_keyword(api.service, q=config.search, part='id,snippet', eventType='completed', type='video', order='viewCount', maxResults=config.number)

    generated_df = clean.dict_to_df(query)
    print(generated_df)


if __name__=="__main__":
    main()