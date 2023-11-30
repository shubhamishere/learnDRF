import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

#a fn to get all the details when nothing is passed and specific detail when an id is passed
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)

    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)

#callling this fn with id 1 to get and print the data of student id 1 from the server
get_data()