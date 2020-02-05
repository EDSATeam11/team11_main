"""# Function 4: Municipality & Hashtag Remover

Write a function which takes in a pandas dataframe and returns the same dataframe which is modified. The function should do the following:

* Extract the municipality from a tweet using the dictonary given below into a new column in the same dataframe.
* Extract the hashtag from a tweet into a new column in the same data frame.
* The column headers should be "municipality" & "hashtags" respectively.
* For those tweets which don't have the either a municipality nor a hashtag, fill it with ```np.nan```."""
import pandas as pd
import numpy as np

def extract_municipality_hashtags(df):
    #extract the municipality : Mikael
    #use this dictionary to extract municipalities
    municipality_dict = { '@CityofCTAlerts' : 'Cape Town',
            '@CityPowerJhb' : 'Johannesburg',
            '@eThekwiniM' : 'eThekwini' ,
            '@EMMInfo' : 'Ekurhuleni',
            '@centlecutility' : 'Mangaung',
            '@NMBmunicipality' : 'Nelson Mandela Bay',
            '@CityTshwane' : 'Tshwane'}

    #add new column to dataframe : Courtney

    #extract the hastag : Mikael

    #add new column to dataframe : Monica

    #change the column headers of added columns : Courtney
    #The column headers should be "municipality" & "hashtags" respectively.

    #Change those tweets which don't have the either a municipality nor a hashtag, fill it with 'np.nan' : Olwethu

    #return new dataframe : Mikael
    return 0

if __name__ == '__main__':
    url = 'https://raw.githubusercontent.com/RidhaMoosa/eskom_data-/master/twitter_nov_2019.csv'
    twitter_df = pd.read_csv(url)
    print(twitter_df)
    print('our new data frame : ','\n',extract_municipality_hashtags(twitter_df))