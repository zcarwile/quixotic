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

DATA_DIR_EMAIL = '../quixotic/data/operational/email'
DATA_DIR_CALENDAR = '../quixotic/data/operational/calendar'
DATA_DIR_RESCUE_TIME = '../quixotic/data/operational/rescue_time'


# In[3]:

# connect to general server for input
cnx = mysql.connector.connect(user=db_user, password=db_pass, host=db_server, db=db_name)
fout = open("../quixotic/data/output/etl.txt","w")


# In[4]:

cursor = cnx.cursor()  
query = "DELETE from event where tags=\"Rescue Time\""  
cursor.execute(query)


# ## Rescue Time

# In[5]:

### write Rescue Time events since last ETL date/(time?) (may be multiple files)
cursor = cnx.cursor()
# get relevant day files
for file in os.listdir(DATA_DIR_RESCUE_TIME): #[stamp > last_harvest_rescue_time:
    file_fullpath = DATA_DIR_RESCUE_TIME + os.sep + file
    with open(file_fullpath,"r") as f:
        for line in f:
        #if event_time > last_harvest_rescue_time:
            event = line.split("\t")
            start = event[0] # 2015-11-06T09:00:00 MYSQL STR_TO_DATE('2015-10-26T07:45:00', '%d-%m-%YT%h:%i:%s')
            features = event[1]
            title = event[2].replace("\"","")
            detail = event[3].replace("\"","")
            tags = "Rescue Time"
            fout.write("%s\t%s\t%s\t%s\t%s\n" % (start, title, features, detail, tags))
            query = "INSERT IGNORE INTO event (start, title, detail, tags, features) VALUES (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\")" % (start, title, detail, tags, features)
            try:            
                cursor.execute(query)
            except:
                print("ERROR: %s" % (query))
            
cnx.commit()
cursor.close()


# ## Emails

# In[5]:

cursor = cnx.cursor()  
query = "DELETE from event where tags=\"Email\""  
cursor.execute(query)

for file in os.listdir(DATA_DIR_EMAIL):

    ### write emails from latest file
    cursor = cnx.cursor()
        
    file_email = DATA_DIR_EMAIL + os.sep + file
    with open(file_email,"r") as f:
        for line in f:
            event = line.split("\t")
            features = event[0]
            start = event[1] # 2015-11-24 16:03:57 -- MYSQL STR_TO_DATE('2015-11-24 16:03:57', '%d-%m-%YT h:%i:%s')
            detail = event[2].replace("\"","")
            title = event[3].replace("\"","")
            tags = "Email"
            fout.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (features, start, "", title, detail, tags))
            query = "INSERT IGNORE INTO event (start, title, detail, tags, features) VALUES (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\")" % (start, title, detail, tags, features)
            try:            
                cursor.execute(query)
            except:
                print("ERROR: %s" % (query))
    
    cnx.commit()
cursor.close()


# ## Calendar

# In[6]:

cursor = cnx.cursor()  
query = "DELETE from event where tags=\"Calendar\""  
cursor.execute(query)


for file in os.listdir(DATA_DIR_CALENDAR):
    ### write calendar events from latest file
    cursor = cnx.cursor()
             
    file_calendar = DATA_DIR_CALENDAR + os.sep + file
    with open(file_calendar,"r") as f:
        for line in f:
            event = line.split("\t")
            features = event[0]
            start = event[1][0:19] #2015-10-26T07:45:00-04:00 -- MYSQL STR_TO_DATE('2015-10-26T07:45:00', '%d-%m-%YT%h:%i:%s')
            end = event[2] #2015-10-26T07:45:00-04:00 -- MYSQL STR_TO_DATE('2015-10-26T07:45:00', '%d-%m-%YT%h:%i:%s')
            detail = event[3].replace("\"","")
            title = event[4].replace("\"","")
            tags = "Calendar"
            fout.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (features, start, end, title, detail, tags))
            query = "INSERT IGNORE INTO event (start, end, title, detail, tags, features) VALUES (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\")" % (start, end, title, detail, tags, features)
            try:            
                cursor.execute(query)
            except:
                print("ERROR: %s" % (query))
    
    cnx.commit()
cursor.close()        



# In[7]:

### Generated features (i.e. word count, relevance score, spamness)

# L8R

### Generate and classify blocks of time blocks of time

# L8R

### Close DB Connections
fout.close()
cnx.close()


# In[ ]:



