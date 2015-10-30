import requests
import pickle

from harvest_calendar import get_last_collection_time_and_file_id

internet = False

DATA_DIR = '../quixotic/data/operational/rescue_time'


if internet == True:
    with open("rescue_time_key") as f:
        key=f.read().strip()
        
        # TODO: Parameters
        kind = "document" #document or activity
        interval = "hour"
        format = "json"
        
        # TODO: Parameterize from outside
        
        lastHarvest,file_id = get_last_collection_time_and_file_id(DATA_DIR)
        file_id = file_id + 1
        date = "2015-10-21"
        
        url = "https://www.rescuetime.com/anapi/data?key=%s&perspective=interval&restrict_kind=%s&interval=%s&restrict_begin=%s&restrict_end=%s&format=%s" % (key,kind,interval,date,date,format)
        
        response = requests.get(url)
        
        print("Pickling RT WS response")
        pickle.dump(response.json(), open('sample_rescue_time.p','wb'))

data = pickle.load(open('sample_rescue_time.p','rb'))    
rows = data['rows']
    
for row in rows:
    if int(row[1]) > 60: 
        print('%s\t%s\t%s\t%s' %  (row[0],row[1],row[3],row[4]))
    #pass
