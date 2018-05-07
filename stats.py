import mysql.connector
import parameters

DB_USER = parameters.DB_USER
DB_PASSWORD = parameters.DB_PASSWORD
DB_HOST = parameters.DB_HOST
DB_NAME = parameters.DB_NAME


cnx = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, db=DB_NAME)
cursor = cnx.cursor()

query_event_count = "select count(*) from quixotic_api_event;"
query_last_start = "select max(start) from quixotic_api_event;"

cursor.execute(query_event_count)
for x in cursor:
	event_count = x[0]

cursor.execute(query_last_start)
for x in cursor:
	last_start = x[0]

print("Database contains %d events; most recent event %s" % (event_count, str(last_start)))

cursor.close()
cnx.close()