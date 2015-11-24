
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

from qlib import get_last_collection_time_and_file_id

DATA_DIR_EMAIL = '../quixotic/data/operational/email'
DATA_DIR_CALENDAR = '../quixotic/data/operational/calendar'
DATA_DIR_RESCUE_TIME = '../quixotic/data/operational/rescue_time'


# In[2]:

# Create empty dataframe w/event schema
# But why -- this is just gon' be a PITA to load into MySQL
QDF = pd.DataFrame(columns=['start','end','title','detail','tags','features','relevant','user_id'])
print(QDF)


# In[3]:

# connect to general server for input
cnx = mysql.connector.connect(user=db_user, password=db_pass, host=db_server, db=db_name)
fout = open("../quixotic/data/output/etl.txt","w")


# In[4]:

### Get last RT date from DB

cursor = cnx.cursor()  
query = "(SELECT max(start) as maxstart from event where tags='Rescue Time')"  
cursor.execute(query)

# unmarshall date
last_harvest_rescue_time = None
for (maxstart) in cursor:
    if maxstart[0] is None:
        print("No previous RescueTime data found")
    else:
        last_harvest_rescue_time = maxstart[0]
        print("Last RescueTime harvest:")
        print(last_harvest_rescue_time) #datetime.datetime

cursor.close()


# In[8]:

### write Rescue Time events since last ETL date/(time?) (may be multiple files)
cursor = cnx.cursor()
# get relevant day files
for file in os.listdir(DATA_DIR_RESCUE_TIME): #[stamp > last_harvest_rescue_time:
    file_fullpath = DATA_DIR_RESCUE_TIME + os.sep + file
    with open(file_fullpath,"r") as f:
        for line in f:
        #if event_time > last_harvest_rescue_time:
            #write_rescuetime()
            fout.write("Rescue Time Event\n")
            #query
            #cursor.execute(query)
                
#cnx.commit()
#cursor.close()


# In[9]:

### write emails from latest file
cursor = cnx.cursor()
junk,file_id_email = get_last_collection_time_and_file_id(DATA_DIR_EMAIL)     
file_email = DATA_DIR_EMAIL + os.sep + "zcarwile_" + str(file_id_email) + ".txt"
with open(file_email,"r") as f:
    for line in f:
        event = line.split("\t")
        identifier = event[0]
        start = event[1]
        detail = event[2]
        title = event[3]
        tags = "Email"
        fout.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (identifier, start, "", title, detail, tags))
        #query = "INSERT INTO event (start, title, detail, tags, id) VALUES (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\")" % (start, title, detail, tags, identifier)
        #cursor.execute(query)

#cnx.commit()
#cursor.close()


# In[10]:

### write calendar events from latest file
cursor = cnx.cursor()
junk,file_id_calendar = get_last_collection_time_and_file_id(DATA_DIR_CALENDAR)         
file_calendar = DATA_DIR_CALENDAR + os.sep + "zcarwile_" + str(file_id_calendar) + ".txt"
with open(file_calendar,"r") as f:
    for line in f:
        event = line.split("\t")
        identifier = event[0]
        start = event[1]
        end = event[2]
        detail = event[3]
        title = event[4]
        tags = "Calendar"
        fout.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (identifier, start, end, title, detail, tags))
        #query = "INSERT INTO event (start, end, title, detail, tags, id) VALUES (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\")" % (start, end, title, detail, tags, identifier)
        #cursor.execute(query)

#cnx.commit()
#cursor.close()        



# In[11]:

### Generated features (i.e. word count, relevance score, spamness)

# L8R

### Generate and classify blocks of time blocks of time

# L8R

### Close DB Connections
fout.close()
cnx.close()


# In[ ]:




# In[ ]:




# In[ ]:



