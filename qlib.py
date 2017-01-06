from __future__ import print_function
import os
import datetime
from pytz import reference

""" Helper functions: these can probably be shared across all harvesters"""

def get_last_collection_time_and_file_id(DATA_DIR):
         
    last_id = 0
    state = None
    
    for filename in os.listdir(DATA_DIR):
        fullpath = os.path.join(DATA_DIR, filename)
        created = datetime.datetime.fromtimestamp(os.path.getctime(fullpath))       
        try:
            fullpath.split(".txt")[1]
        except IndexError:
            # not a text file
            continue
        
        try:
            if state == None:
                state = created
                try:
                    last_id = int(fullpath.split("zcarwile_")[1].split(".txt")[0])
                except:
                    pass # RT does not apply
            else:
                if created > state:
                    state = created
                    try:
                        last_id = int(fullpath.split("zcarwile_")[1].split(".txt")[0])
                    except:
                        pass # RT does not apply
        except ValueError:
            last_id = -1
    
    if state == None:
        state = datetime.datetime(2016,1,1)
    
    localtime = reference.LocalTimezone()
    lct = state.replace(tzinfo=localtime)
    
    return lct,last_id


if __name__ == '__main__':
    DATA_DIR_CALENDAR = '../quixotic/data/operational/rescue_time'    
    lct,id = get_last_collection_time_and_file_id(DATA_DIR_CALENDAR)
    print(lct)
    print(id)
