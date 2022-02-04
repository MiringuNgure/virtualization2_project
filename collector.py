import pandas as pd
import sqlalchemy

from bs4 import BeautifulSoup as bs
pd.set_option('display.max_colwidth', 500)
import time
import requests
import random

engine = sqlalchemy.create_engine('postgresql://postgres:postgres@postgres:5432/postgres')

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

while True:

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
    df = pd.DataFrame()
    df["name"] = airports
    df ["airport_code"] = codes
    df["temperature"] = var[0]
    df["dewpoint"] = var[1]
    df["pressure"] = var[2]
    df["winds"] = var[3]
    df["visibility"] = var[4]
    df["ceiling"] = var[5]
    df["clouds"] = var[6]

    df.to_sql(
        name= 'airports',
        con= engine,
        index = False,
        if_exists= "replace"
    )
    time.sleep(3600) #sleep 1hr