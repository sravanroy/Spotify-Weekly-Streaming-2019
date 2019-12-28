import os
os.chdir("C:/Users/User/Desktop/Spotify")


# load required libraries
import requests
import io
import pandas as pd
from subprocess import Popen
from datetime import datetime, timedelta


# list of column names for the final DataFrame
column_names = ['Position', 'Track_Name','Artist','Streams','Track_URL','Country','Date','Week_Number']


# Initialzing an empty DataFrame for appending DataFrames while parsing
df_final = pd.DataFrame(columns = column_names)


# list of country names to iterate and parse 
regions = ['global','ad','ca','dk','gr','is','mx','ph','sv','ar','ch','do',	'gt	','it','my','pl','th'
            'at','cl','ec','hk','jp','ni','pt','tr','au','co','ee','hn','lt','nl','py','tw',
            'be','cr','es','hu','lu','no','ro','us','bg','cy','fi','id','lv','nz','se','uy'
            'bo','cz','fr','ie','mc','pa','sg','vn','br','de','gb','il','mt','pe','sk']


# initializing the date with the latest week date
date_str1 = '2019-12-20'
date_1 = datetime.strptime(date_str1,'%Y-%m-%d')

# The start date to collect the data (last week of 2018)
date_start = datetime.strptime('2018-12-28','%Y-%m-%d')


# while loop to iterate over the date ranges from latest to start weeks 
while(date_1>=date_start):
    
    date_1 = datetime.strptime(date_str1,'%Y-%m-%d')
    # subtracting the current date by 7 to get the previous week's starting date
    date_2 = date_1 - timedelta(days=7)
    date_str2  = date_2.strftime(format='%Y-%m-%d')
    date = date_1.strftime(format='%m/%d/%Y')
    week_number = date_1.strftime(format='%V')
    
    # converting the date range in the format consistent with Spotify URL
    date_range = date_str2+'--'+date_str1
    
    
    # looping over all the regions in a given date range
    for region in regions:
        
        url = 'https://spotifycharts.com/regional/{}/weekly/{}/download'.format(region,date_range)
        
        s = requests.Session() 
        response = s.get(url)    
        
        data = response.content
        
       
        try:
            df = pd.read_csv(io.StringIO(data.decode('utf-8')), skiprows=1)
            df.columns = ['Position','Track_Name','Artist','Streams','Track_URL']
            df['Country'] = region
            df['Date'] = date
            df['Week_Number'] = week_number
        except:
            # add an empty DataFrame incase of errors
            df = pd.DataFrame(columns = column_names)
        
        
        # appending the DataFrames together 
        df_final = pd.concat([df_final,df], ignore_index=True, sort=False)
     
    # updating the current date to previous week's start date
    date_1 = date_1 - timedelta(days=7)
    date_str1  = date_1.strftime(format='%Y-%m-%d')
    


# writing the final DataFrame to a CSV file
df_final.to_csv("Spotify_Weekly_Streaming_2019.csv",index=False)


