#question1
#connect and fetch data from json

#import modules/packages
import requests

#parse url get the json data using requests
r = requests.get('https://pomber.github.io/covid19/timeseries.json').json()

#check the type of the data
print(type(r))

#checking if data is fetched or not
import pandas as pd

#create data frame instance as df
df = pd.DataFrame(r)

#print head of the data frame
print(df.head())

#fetch all the rows from the data frame
for index, row in df.iterrows():
   print(row)

#fetch column names form data frame
print(df.columns)

