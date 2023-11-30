
#assume this to be an external client side application requesting data from pur django backend app

import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name': 'Shubham Pandey',
    'roll': 23,
    'city': 'Chennai'
}

json_data = json.dumps(data)

#data is sent (POST req) from client side (here) to server side (to our django backend app)
r = requests.post(url = URL, data = json_data)

data = r.json()
print(data)