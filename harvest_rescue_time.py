import requests

with open("rescue_time_key") as f:
	key=f.read().strip()

	# TODO: Parameters
	kind = "document" #document or activity
	interval = "hour"
	format = "json"

	# TODO: Parameterize from outside
	date = "2015-10-21"

	url = "https://www.rescuetime.com/anapi/data?key=%s&perspective=interval&restrict_kind=%s&interval=%s&restrict_begin=%s&restrict_end=%s&format=%s" % (key,kind,interval,date,date,format)

	response = requests.get(url)

	print(response.json())
