import pandas as pd
import sqlalchemy

from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import requests
import random
from pymongo import MongoClient

# Creating the variables that should be stored in the database
Temperature = []
Dewpoint = []
Pressure = []
Winds = []
Visibility = []
Ceiling = []
Clouds = []
airport_id=[]

#creating a list of lists that will be scrapped from the website
var = [Temperature, Dewpoint, Pressure, Winds, Visibility,Ceiling,Clouds]

#codes for the airports and corresponding names of the airports
codes = ["EDDL","EDDF","RJAA","SAEZ","CYVR","ENSB","CYYR", "EDDM", "EDDH", "OMDB"] 
airports =["Dusseldorf", "Frankfurt", "Tokyo","Buenos Aires", "Vancouver","Longyearbyen","Goose Bay", "Munich", "Harmburg", "Dubai"]

#loop all the aiports of interest
for i in codes:

    page = requests.get(f"https://www.aviationweather.gov/metar/data?ids={i}&format=decoded&hours=0&taf=off&layout=on") #create a reaquest
    soup = bs(page.content, "html.parser")
    
    j=0
    # loop data needed for the individual airports and create a dataframe
    for tr in soup.find_all('tr')[2:]:

        if j<7:
        
            tds= tr.find_all('td')
            var[j].append(tds[1].text)
            #print(tds[0].text,"",tds[1].text)
            j+=1

#create a dataframe
df1 = pd.DataFrame()
df1["name"] = airports
df1 ["airport_code"] = codes
df1["temperature"] = var[0]
df1["dewpoint"] = var[1]
df1["pressure"] = var[2]
df1["winds"] = var[3]
df1["visibility"] = var[4]
df1["ceiling"] = var[5]
df1["clouds"] = var[6]

client = MongoClient("mongodb+srv://Peter:Wuppertal9358@awala.m2wha.mongodb.net/weather?retryWrites=true&w=majority")

db=client.weather

collection=db['airport']
df1.reset_index(inplace=True)
data_dict = df1.to_dict("records")
collection.insert_many(data_dict)