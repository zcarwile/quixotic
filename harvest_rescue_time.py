import requests
import pickle
import sys
import datetime

from qlib import get_last_collection_time_and_file_id

DATA_DIR_RESCUE_TIME = '../quixotic/data/operational/rescue_time'

with open("rescue_time_key") as f:
    key=f.read().strip()
    
    # TODO: Parameters
    kind = "document" #document or activity
    interval = "hour"
    format = "json"
    
    # TODO: Parameterize from outside
    
    lastHarvest,file_id = get_last_collection_time_and_file_id(DATA_DIR_RESCUE_TIME)
    date = datetime.datetime.strptime(lastHarvest[0:10], "%Y-%m-%d")
    now = datetime.datetime.now()
    
    print("Last Rescue Time Harvest: ")
    print(date)
    
    if (date < now):
        print("\nCalling RT API")
    else:
        print("Nothing to harvest")
    
    while (date < now):    
        str_date = str(date)[0:10]  
        print(str_date)        
  
        url = "https://www.rescuetime.com/anapi/data?key=%s&perspective=interval&restrict_kind=%s&interval=%s&restrict_begin=%s&restrict_end=%s&format=%s" % (key,kind,interval,str_date,str_date,format)
        
        response = requests.get(url)
        
        #print("Pickling RT WS response")
        #pickle.dump(response.json(), open('sample_rescue_time.p','wb'))
        #data = pickle.load(open('sample_rescue_time.p','rb'))  
        
        data = response.json()
        rows = data['rows']
    
        with open('%s/zcarwile_%s.txt' % (DATA_DIR_RESCUE_TIME,str_date),'w') as f:    
            for row in rows:
                if int(row[1]) > 60: 
                    f.write('%s\t%s\t%s\t%s\n' %  (row[0],row[1],row[3],row[4]))
                    
        date = date + datetime.timedelta(days=1)
    
            
