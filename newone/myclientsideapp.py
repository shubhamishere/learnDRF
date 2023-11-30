import requests
import json


data = {
    'name' : 'Sonam',
    'roll' : 101,
    'city' : 'Ranchi'
}

json_data = json.dumps(data)
#sending the json_data as post request, and the response will be stored in r
r = requests.post(url = "http://127.0.0.1:8000/stucreate/", data = json_data)

#to extract the data from the response
data = r.json()
print(data)
