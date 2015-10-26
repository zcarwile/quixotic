from __future__ import print_function
import httplib2
import os
import sys

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

from harvest_calendar import get_last_collection_time_and_file_id

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'

DATA_DIR = '../quixotic/data/operational/email'

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
                                   'gmail-python-quickstart.json')

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
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    lastHarvest,file_id = get_last_collection_time_and_file_id(DATA_DIR)

    print('Collecting SENT emails since last harvest')
    print(lastHarvest)

    sys.exit()

    #results = service.users().labels().list(userId='me').execute()
    results = service.users().messages().list(userId='me',labelIds='SENT').execute()
    messages = results.get('messages')
    

    #TODO: I'll need to handle the case of when more than 100 messages need to get added    
    #nextPageToken = results.get('nextPageToken')

    if not messages:
        print('No messages found.')
    else:
        for message in messages:
            to = ""
            subj = ""
            date = ""
            m = service.users().messages().get(userId='me',id=message['id'],format='metadata').execute()
            for header in m.get('payload').get('headers'):
                if header['name'] == 'To':
                    to = header['value']
                if header['name'] == 'Subject':
                    subj = header['value']
                if header['name'] == 'Date':
                    date = header['value']
            
            # What is this damn date format?!?
            print(date)
                    
            
        
            
          
        
        
        


if __name__ == '__main__':
    main()
