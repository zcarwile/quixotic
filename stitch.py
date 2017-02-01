
# coding: utf-8

# In[1]:

#!/home/ubuntu/.conda/envs/quixotic/bin/python


# In[16]:

import pandas as pd
import os
import datetime
import pytz

import parameters


# In[17]:

# TO DO: move DB parameters to file

import mysql.connector

DB_USER = parameters.DB_USER
DB_PASSWORD = parameters.DB_PASSWORD
DB_HOST = parameters.DB_HOST
DB_NAME = parameters.DB_NAME


# In[18]:

DATA_DIR_RESCUE_TIME = parameters.DATA_DIR_RESCUE_TIME
DATA_DIR_EMAIL = parameters.DATA_DIR_EMAIL
DATA_DIR_CALENDAR = parameters.DATA_DIR_CALENDAR
ETL_DIR = parameters.ETL_DIR

USER_TIMEZONE = "US/Eastern"


# In[23]:

df_rt = pd.DataFrame()
names = ['hour', 'duration', 'title', 'detail']

#file = 'zcarwile_2015-10-02.txt'
for file in os.listdir(DATA_DIR_RESCUE_TIME):
    df_tmp = pd.DataFrame()
    if ".txt" in file:
        full_path = '%s/%s' % (DATA_DIR_RESCUE_TIME, file)
        try:
            df_tmp = pd.read_table(full_path, sep='\t', header=None, names=names)
            df_rt = pd.concat([df_rt, df_tmp], ignore_index=True)
        except:
            print('Error processing: ' + full_path)
    
df_rt.tail()


# In[24]:

# to make RT data "aware"
def to_aware(hour, timezone):
    est = pytz.timezone(timezone)
    aware = est.localize(datetime.datetime.strptime(hour,'%Y-%m-%dT%H:%M:%S'))
    return(aware)
                         
df_rt['start'] = df_rt.apply(lambda row: to_aware(row['hour'], USER_TIMEZONE), axis=1)
df_rt['start'] = pd.to_datetime(df_rt['start'], utc=True)


# In[25]:

# create fake end time
# ultimately, rescue time is a poor data source because we're not using the raw tracks.  but ok for illustration
def create_end_time(hour, timezone, duration):
    est = pytz.timezone(timezone)
    tmp = est.localize(datetime.datetime.strptime(hour,'%Y-%m-%dT%H:%M:%S')) 
    duration = int(duration)
    end_time = tmp + datetime.timedelta(seconds=duration)
    return(end_time)

df_rt['end'] = df_rt.apply(lambda row: create_end_time(row['hour'], USER_TIMEZONE, row['duration']), axis=1)
df_rt['end'] = pd.to_datetime(df_rt['end'], utc=True)

df_rt.drop('hour', 1, inplace=True)
df_rt.drop('duration', 1, inplace=True)


# In[26]:

df_rt.sort_values(by='start', inplace=True)
df_rt['tags'] = 'Rescue Time'

df_rt.tail()


# In[28]:

# Email
#file = 'zcarwile_1.txt'

df_email = pd.DataFrame()
names = ['detail','sent','features','title','redaction'] # TO DO: need an extra column -- for now I'm just stuffing

for file in os.listdir(DATA_DIR_EMAIL):
    if ".txt" in file:
        df_tmp = pd.DataFrame()
        full_path = '%s/%s' % (DATA_DIR_EMAIL, file)
        try:
            df_tmp = pd.read_table(full_path, header=None, names=names)
            df_email = pd.concat([df_email, df_tmp], ignore_index=True)
        except:
            print('Error processing: ' + full_path)
            
df_email['start'] = pd.to_datetime(df_email['sent'], utc=True)
df_email.drop('sent', 1, inplace=True)

df_email.sort_values(by='start', inplace=True)

df_email['tags'] = 'Gmail'
df_email.tail()


# In[29]:

# Calendar
#file = 'zcarwile_1.txt'
df_calendar = pd.DataFrame()
names = ['detail','start_time','end_time','features','title']

for file in os.listdir(DATA_DIR_CALENDAR):
    if ".txt" in file:
        full_path = '%s/%s' % (DATA_DIR_CALENDAR, file)
        try:
            df_tmp = pd.read_table(full_path, header=None, names=names)
            df_calendar = pd.concat([df_calendar, df_tmp], ignore_index=True)
        except:
            print('Error processing: ' + full_path)


df_calendar['start'] = pd.to_datetime(df_calendar['start_time'], utc=True)
df_calendar['end'] = pd.to_datetime(df_calendar['end_time'], utc=True)

df_calendar.drop('start_time', 1, inplace=True)
df_calendar.drop('end_time', 1, inplace=True)

df_calendar.sort_values(by='start', inplace=True)
df_calendar['tags'] = 'Google Calendar'

df_calendar.tail()


# In[ ]:




# In[30]:

# Check for unified data types in timestamp
#print(type(df_rt.loc[0]['start']))
#print(type(df_rt.loc[0]['start']))
#print(type(df_email.loc[0]['start']))
#print(type(df_calendar.loc[0]['start']))
#print(type(df_calendar.loc[0]['end']))


# In[35]:


frames = [df_rt, df_email, df_calendar]

result = pd.concat(frames, ignore_index=True)
result.sort_values(by='start', inplace=True)
result['user_id'] = 1
result.tail(100)


# In[36]:

# unified file with UTC timestamps

outfile = '%s/%s' % (ETL_DIR, 'zcarwile.txt')
result.to_csv(outfile, sep="\t")


# In[37]:

# test for file pulled from EC2

#z = pd.read_csv('zcarwile.txt','\t')
#z.tail()


# In[38]:

cnx = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, db=DB_NAME)
result.to_sql('quixotic_api_event', cnx, flavor='mysql', if_exists='append', index=True, index_label='id')
cnx.close()


# In[ ]:

# HOW DO I initialize table in Django with a default user
#insert into quixotic_api_user (name) values ('zcarwile');

