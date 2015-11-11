### QUIXOTIC Analytical ETL
import mysql.connector
import http.client
import xml.etree.ElementTree as ET

db_server = "127.0.0.1"
db_port = 3306
db_name = "quixotic_etl"
db_user = "root"
db_pass = "root"

from qlib import get_last_collection_time_and_file_id

DATA_DIR_EMAIL = '../quixotic/data/operational/email'
DATA_DIR_CALENDAR = '../quixotic/data/operational/calendar'
DATA_DIR_RESCUE_TIME = '../quixotic/data/operational/rescue_time'


def main():

    # connect to general server for input
    cnx = mysql.connector.connect(user=db_user, password=db_pass, host=db_server)
    
    ### write emails from latest file
    junk,file_id_email = get_last_collection_time_and_file_id(DATA_DIR_EMAIL)     
    with open file:
        for row in rows:
            write_event()
    
    ### write calendar events from latest file
    junk,file_id_calendar = get_last_collection_time_and_file_id(DATA_DIR_CALENDAR)         
    with open file:
        for row in rows:
            write_event()
   
   
    ### Get last RT date from DB
    
    cursor = cnx.cursor()  
    query = "(SELECT max(start) from event)"  
    cursor.execute(query)
    # unmarshall date
    
    ### write Rescue Time events since last ETL date/(time?) (may be multiple files)
    
    # get files
    for file in file:
        for row in row:
            if date > last_rescue_time_date:
                write_event()
                # perhaps use pd.DataFrame() to do a single write
    
    cursor = cnx.cursor()
    
    ## old code
#    for row in rows:
#    	event = row.split('\t')
#    	start = event[0]
#    	stop = event[1]
#    	title = event[2]
#    	if title == None:
#    		title = ""
#    	else:
#    		title = title.replace("\"","")
#    
#    	
#    	# insert event
#    	if stop == None:
#    		query = "INSERT INTO event (start, end, title, tags) VALUES (\"%s\", NULL, \"%s\", \"%s\")" % (start, title, tag)
#    	else:
#    		query = "INSERT INTO event (start, end, title, tags) VALUES (\"%s\", \"%s\", \"%s\", \"%s\")" % (start, stop, title, tag)
#    	
#    	cursor.execute(query)
    
    	
    # close input cursor and commit output (future sections will only need ETL database)	
    cnx.commit()
    cursor.close()
    
    ### Generated features (i.e. word count, relevance score, spamness)
    
    # L8R
    
    ### Generate and classify blocks of time blocks of time
    
    # L8R
    
    ### Close DB Connections
    
    cnx.close()

if __name__ == "__main__":
    main()