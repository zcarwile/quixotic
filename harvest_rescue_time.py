#!/Users/zcarwile/miniconda/envs/quixotic/bin/python

import requests
import datetime
from pytz import reference

from qlib import get_last_collection_time_and_file_id

DATA_DIR_RESCUE_TIME = '../quixotic/data/operational/rescue_time'

def main():

    with open("rescue_time_key") as f:
        key=f.read().strip()
        
        # TODO: Parameters
        kind = "document" #document or activity
        interval = "hour"
        format = "json"
            
        lastHarvest,file_id = get_last_collection_time_and_file_id(DATA_DIR_RESCUE_TIME)
        date = lastHarvest.strftime("%Y-%m-%d")
    
        # get NOW    
        localtime = reference.LocalTimezone()
        now = datetime.datetime.now().replace(tzinfo=localtime)
        
        print("Last Rescue Time Harvest: ")
        print(date)
        
        print("\nCalling RT API")
    
        
        current_date = lastHarvest.replace(hour=0, minute=0, second=0, microsecond=0)
        while (current_date < now):    
            str_date = current_date.strftime("%Y-%m-%d")  
            print(str_date)        
       
            url = "https://www.rescuetime.com/anapi/data?key=%s&perspective=interval&restrict_kind=%s&interval=%s&restrict_begin=%s&restrict_end=%s&format=%s" % (key,kind,interval,str_date,str_date,format)         
            response = requests.get(url)
             
            #print("Pickling RT WS response")
            #pickle.dump(response.json(), open('sample_rescue_time.p','wb'))
            #data = pickle.load(open('sample_rescue_time.p','rb'))  
            
            data = response.json()
            rows = data['rows']
            print(data)
         
            with open('%s/zcarwile_%s.txt' % (DATA_DIR_RESCUE_TIME,str_date),'w') as f:    
                for row in rows:
                    if int(row[1]) > 60: 
                        f.write('%s\t%s\t%s\t%s\n' %  (row[0],row[1],row[3],row[4]))
                
            current_date = current_date + datetime.timedelta(days=1)
    
if __name__ == '__main__':
    main()            
