#!/Users/zcarwile/miniconda/envs/quixotic/bin/python

# coding: utf-8

# In[1]:

### QUIXOTIC Analytical ETL
import mysql.connector
import http.client
import xml.etree.ElementTree as ET
import os
import pandas as pd

db_server = "127.0.0.1"
db_port = 3306
db_name = "quixotic_etl"
db_user = "root"
db_pass = "root"

DATA_DIR_CALENDAR = '../quixotic/data/operational/calendar'

# connect to general server for input
cnx = mysql.connector.connect(user=db_user, password=db_pass, host=db_server, db=db_name)
fout = open("../quixotic/data/output/etl_calendar.txt","w")

### Wipe old data

cursor = cnx.cursor()  
query = "DELETE FROM event WHERE tags=\"Calendar\";"  
print(query)
cursor.execute(query)
cursor.close()

### Calendar

### write calendar events from latest file

     
for file_calendar in os.listdir(DATA_DIR_CALENDAR):
    with open(DATA_DIR_CALENDAR + os.sep + file_calendar, "r") as f:
        cursor = cnx.cursor()        
        for line in f:
            event = line.split("\t")
            features = event[0]
            start = event[1][0:19] #2015-10-26T07:45:00-04:00 -- MYSQL STR_TO_DATE('2015-10-26T07:45:00', '%d-%m-%YT%h:%i:%s')
            end = event[2] #2015-10-26T07:45:00-04:00 -- MYSQL STR_TO_DATE('2015-10-26T07:45:00', '%d-%m-%YT%h:%i:%s')
            detail = event[3]
            title = event[4]
            tags = "Calendar"
            fout.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (features, start, end, title, detail, tags))
            query = "INSERT INTO event (start, end, title, detail, tags, features) VALUES (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\")" % (start, end, title, detail, tags, features)
            try:            
                cursor.execute(query)
            except:
                print("ERROR: %s" % (query))
    
        cnx.commit()
        cursor.close()        

### Close DB Connections
fout.close()
cnx.close()




