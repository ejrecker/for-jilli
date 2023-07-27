#need to import auth then add headers
import csv
import json
import requests

#config variables
base_url = 'https://legalserver.com'
api_endpoint = '/users/'


#get info to submit via api from csv
api_data_dict = {}
with open('data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader) #skips header line

    for row in csv_reader:
        id = row[0]
        key = row[1]
        value = row[2]
        if id in api_data_dict.keys():
            api_data_dict[id][key] = [value]
        else:
            api_data_dict[id] = {key: value}

#loop through dict to submit data via patch request to api
for id in api_data_dict.keys():
    payload = json.dumps(api_data_dict[id])
    url = f'{base_url}{api_endpoint}{id}'
    requests.patch(url=url, data=payload)    




