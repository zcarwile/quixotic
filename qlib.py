from __future__ import print_function
import os
import sys
import datetime

""" Helper functions: these can probably be shared across all harvesters"""

def get_last_collection_time_and_file_id(DATA_DIR_CALENDAR):
    
    # TODO: get last timestamp and associated file id from DATA_DIR_CALENDAR  
        
    last_id = 0
    state = None
    for filename in os.listdir(DATA_DIR_CALENDAR):
        fullpath = os.path.join(DATA_DIR_CALENDAR, filename)
        created = datetime.datetime.fromtimestamp(os.path.getctime(fullpath))
        
        try:
            if state == None:
                state = created
                last_id = int(fullpath.split("zcarwile_")[1].split(".txt")[0])
            else:
                if created > state:
                    state = created
                    last_id = int(fullpath.split("zcarwile_")[1].split(".txt")[0])
        except ValueError:
            last_id = -1

    if state == None:
        state = datetime.datetime(2015,9,21).isoformat() + 'Z'
    else:
        state = created.isoformat() + 'Z'       
        #TODO: Need to convert file timestamp to whatever God awful format Google wants
        pass
       
    return state,last_id