#!/Users/zcarwile/miniconda/envs/quixotic/bin/python
import mysql.connector

#ALTER TABLE event ADD redaction varchar(255);

rd = "/Users/zcarwile/Documents/quixotic/redaction_dictionary.txt"

db_server = "127.0.0.1"
db_port = 3306
db_name = "quixotic_etl"
db_user = "root"
db_pass = "root"

cnx = mysql.connector.connect(user=db_user, password=db_pass, host=db_server, db=db_name)

cursor = cnx.cursor()  
query = "UPDATE event SET redaction=detail, detail='<recipients removed>' where tags='Email' and redaction is null;"  
cursor.execute(query)
query = "UPDATE event SET redaction=detail, detail='<attendees removed>' where tags='Calendar' and redaction is null;"  
cursor.execute(query)
query = "DELETE FROM event where title like '%continuum.io%' and tags='Email';"  # these are just noise anyway
cursor.execute(query)

with open(rd) as f:
    for line in f:
        x = line.strip()
        query = "UPDATE event SET title=REPLACE(title, '%s', '<customer>'), redaction='%s' WHERE redaction is null and title LIKE BINARY '%%%s%%';" % (x,x,x)
        #print(query)
        cursor.execute(query)
        
cnx.commit()
cnx.close()
