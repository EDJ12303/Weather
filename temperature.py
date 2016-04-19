# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 16:49:04 2016

@author: Erin
"""
import datetime
import requests
import pandas as pd
import sqlite3 as lite

cities = {  "Austin": '30.303936,-97.754355',
            "Boston": '42.331960,-71.020173',
            "Chicago": '41.837551,-87.681844',
            "Cleveland": '41.478462,-81.679435',
            "Denver": '39.761850,-104.881105'
          }
        
con = lite.connect('weather.db')
cur = con.cursor()

# Drop tables if they already exist
with con:
    cur.execute("DROP TABLE IF EXISTS daily_maxtemp")
#darkskykey = "8e2f0f9e97727516429316ac1aaec3ad"
start_date = datetime.datetime.now() - datetime.timedelta(days=30)
end_date = datetime.datetime.now()
#testing start date formating
print start_date.strftime('%Y-%m-%dT%H:%M:%S')
print end_date.strftime('%Y-%m-%dT%H:%M:%S')

cities.keys()
with con:
    cur.execute('CREATE TABLE daily_maxtemp (day_of_reading INT, Austin REAL, 
    Boston REAL, Chicago REAL, Cleveland REAL, Denver REAL);')
with con:
    while start_date < end_date:
        cur.execute("INSERT INTO daily_maxtemp(day_of_reading) VALUES (?)", 
                    (int(start_date.strftime('%Y%m%d')),))
        start_date += datetime.timedelta(days=1)

#loop through the cities and query the API
for k,v in cities.iteritems():
    start_date = end_date - datetime.timedelta(days=30) #reset value each time
    through the loop 
    while start_date < end_date:

        #query for the value
        r = requests.get
        ("https://api.forecast.io/forecast/8e2f0f9e97727516429316ac1aaec3ad/"
        + v + "," + str(start_date.strftime('%Y-%m-%dT%H:%M:%S')))
        
        with con:
            #insert the temperature max to the database
            cur.execute('UPDATE daily_maxtemp SET ' + k + ' = '
            + str(r.json()['daily']['data'][0]['temperatureMax']) 
            + ' WHERE day_of_reading = ' + start_date.strftime('%Y%m%d'))
            
        #increment start_date to the next day 
        start_date += datetime.timedelta(days=1) 
        

df = pd.read_sql_query
("SELECT * FROM daily_maxtemp",con,index_col='day_of_reading')
#mean temp for each city
print (df)


con.commit()
con.close()

print ("The mean temperature for each city is:")
print ("Austin")
print df['Austin'].mean()
print ("Boston")
print df['Boston'].mean()
print ("Chicago")
print df['Chicago'].mean()
print ("Cleveland")
print df['Cleveland'].mean()
print ("Denver")
print df['Denver'].mean()

print ("The range temperatures for each city is:")
print ("Austin")
print max(df['Austin'])- min(df['Austin'])
print ("Boston")
print max(df['Boston'])- min(df['Boston'])
print ("Chicago")
print max(df['Chicago'])- min(df['Chicago'])
print ("Cleveland")
print max(df['Cleveland'])- min(df['Cleveland'])
print ("Denver")
print max(df['Denver'])- min(df['Denver'])

print ("The variance of temperatures for each city is:")
print ("Austin")
print (df['Austin'].var())
print ("Boston")
print (df['Boston'].var())
print ("Chicago")
print (df['Chicago'].var())
print ("Cleveland")
print (df['Cleveland'].var())
print ("Denver")
print (df['Denver'].var())







