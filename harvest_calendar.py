from __future__ import print_function
import httplib2
import os
import time

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

DATA_DIR = '../quixotic/data/operational/calendar'

""" Helper functions: these can probably be shared across all harvesters"""

def get_last_collection_time_and_file_id(DATA_DIR):
    
    # TODO: get last timestamp and associated file id from DATA_DIR  
        
    last_id = 0
    state = None
    for filename in os.listdir(DATA_DIR):
        fullpath = os.path.join(DATA_DIR, filename)
        created = datetime.datetime.fromtimestamp(os.path.getctime(fullpath))
        
        if state == None:
            state = created
            last_id = int(fullpath.split("zcarwile_")[1].split(".txt")[0])
        else:
            if created > state:
                state = created
                last_id = int(fullpath.split("zcarwile_")[1].split(".txt")[0])

    if state == None:
        state = datetime.datetime(2015,9,21).isoformat() + 'Z'
    else:
        state = created.isoformat() + 'Z'       
        #TODO: Need to convert file timestamp to whatever God awful format Google wants
        pass
       
    return state,last_id
    

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    startTime = datetime.datetime(2015,9,21).isoformat() + 'Z'
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    lastHarvest,file_id = get_last_collection_time_and_file_id(DATA_DIR)
    file_id = file_id + 1 

    with open('%s/zcarwile_%d.txt' % (DATA_DIR,file_id),'w') as f:    
    
        print('Getting Google Calendar events since last harvest')
        print(lastHarvest)
        eventsResult = service.events().list(
            calendarId='primary', timeMin=lastHarvest, timeMax=now, singleEvents=True,
            orderBy='startTime').execute()
        events = eventsResult.get('items', [])
    
        if not events:
            print('No new events found.')
        else:
            print('%s new events found' % (str(len(events))))
        
        
            for event in events:
                
                event_id = event['id']
                start = event['start'].get('dateTime', event['start'].get('date'))
                end = event['end'].get('dateTime', event['end'].get('date'))
                org = event['organizer'].get('displayName')
                
                #TODO -- do I want to add support for attendees and title?        
                
                f.write("%s\t%s\t%s\t%s\t%s\n" % (event_id,start, end, org, event['summary']))
                #print("%s\t%s\t%s\t%s\n" % (start, end, org, event['summary']))
            
        print('Written to %s/zcarwile_%d.txt' % (DATA_DIR,file_id))


if __name__ == '__main__':
    main()
