
# coding: utf-8

# In[33]:

import pandas as pd
import os
import datetime
import pytz

import parameters


# In[34]:

DATA_DIR_RESCUE_TIME = parameters.DATA_DIR_RESCUE_TIME
DATA_DIR_EMAIL = parameters.DATA_DIR_EMAIL
DATA_DIR_CALENDAR = parameters.DATA_DIR_CALENDAR
ETL_DIR = parameters.ETL_DIR

USER_TIMEZONE = "US/Eastern"


# In[35]:

#for file in os.listdir(parameters.DATA_DIR_RESCUE_TIME):
file = 'zcarwile_2015-10-02.txt'
df_rt = pd.DataFrame()
names = ['hour', 'duration', 'subject', 'detail']
if ".txt" in file:
    full_path = '%s/%s' % (DATA_DIR_RESCUE_TIME, file)
    try:
        df_rt = pd.read_table(full_path, sep='\t', header=None, names=names)
    except:
        print('Error processing: ' + full_path)

df_rt.head()


# In[36]:

# to make RT data "aware"
def to_aware(hour, timezone):
    est = pytz.timezone(timezone)
    aware = est.localize(datetime.datetime.strptime(hour,'%Y-%m-%dT%H:%M:%S'))
    return(aware)
                         
df_rt['event_start'] = df_rt.apply(lambda row: to_aware(row['hour'], USER_TIMEZONE), axis=1)
df_rt['event_start'] = pd.to_datetime(df_rt['event_start'], utc=True)


# In[37]:

# create fake end time
# ultimately, rescue time is a poor data source because we're not using the raw tracks.  but ok for illustration
def create_end_time(hour, timezone, duration):
    est = pytz.timezone(timezone)
    tmp = est.localize(datetime.datetime.strptime(hour,'%Y-%m-%dT%H:%M:%S')) 
    duration = int(duration)
    end_time = tmp + datetime.timedelta(seconds=duration)
    return(end_time)

df_rt['event_end'] = df_rt.apply(lambda row: create_end_time(row['hour'], USER_TIMEZONE, row['duration']), axis=1)
df_rt['event_end'] = pd.to_datetime(df_rt['event_end'], utc=True)


# In[38]:

df_rt.drop('hour', 1, inplace=True)
df_rt.drop('duration', 1, inplace=True)
df_rt.head()


# In[39]:

# Email
file = 'zcarwile_1.txt'
df_email = pd.DataFrame()
names = ['id','sent','person','subject','detail']
if ".txt" in file:
    full_path = '%s/%s' % (DATA_DIR_EMAIL, file)
    try:
        df_email = pd.read_table(full_path, header=None, names=names)
    except:
        print('Error processing: ' + full_path)

df_email['event_start'] = pd.to_datetime(df_email['sent'], utc=True)
df_email.drop('sent', 1, inplace=True)
df_email.head()


# In[40]:

# Calendar
file = 'zcarwile_1.txt'
df_calendar = pd.DataFrame()
names = ['id','start_time','end_time','person','subject']
if ".txt" in file:
    full_path = '%s/%s' % (DATA_DIR_CALENDAR, file)
    try:
        df_calendar = pd.read_table(full_path, header=None, names=names)
    except:
        print('Error processing: ' + full_path)


df_calendar['event_start'] = pd.to_datetime(df_calendar['start_time'], utc=True)
df_calendar['event_end'] = pd.to_datetime(df_calendar['end_time'], utc=True)

df_calendar.drop('start_time', 1, inplace=True)
df_calendar.drop('end_time', 1, inplace=True)
df_calendar.head()


# In[ ]:




# In[41]:

# Check for unified data types in timestamp
print(type(df_rt.loc[0]['event_start']))
print(type(df_rt.loc[0]['event_start']))
print(type(df_email.loc[0]['event_start']))
print(type(df_calendar.loc[0]['event_start']))
print(type(df_calendar.loc[0]['event_end']))


# In[42]:

#goal
#index,id,event_start,event_end,person,subject,detail,important


# In[43]:




# In[44]:

# TO DO: Loop


# In[45]:

# TO DO: merge dataframes
frames = [df_rt, df_email, df_calendar]

result = pd.concat(frames)
result.head(500)


# In[46]:

# unified file with UTC timestamps

outfile = '%s/%s' % (ETL_DIR, 'zcarwile.txt')
result.to_csv(outfile, sep="\t")


# In[ ]:



