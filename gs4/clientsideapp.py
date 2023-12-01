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
#get_data(1)
#get_data(2)
#get-data()

##----------------------------------------------
#method for POSTing data
def post_data():
    #this dict data we will post to server
    # outgoing_data = {
    #     'name': 'ravi',
    #     'roll': 104,
    #     'city': 'Dhanbad',
    # }

    # outgoing_data = {
    #     'name': 'sujeet',
    #     'roll': 10,
    #     'city': 'Delhi',
    # }

    # outgoing_data = {
    #     'name': 'kishan',
    #     'roll': 26,
    #     'city': 'Mumbai',
    # }

    # outgoing_data = {
    #     'name': 'umesh',
    #     'roll': 98,
    #     'city': 'Kolkata',
    # }

    outgoing_json_data = json.dumps(outgoing_data)

    #requests.post will send data to the server and receive
    #-a response in 'r'
    r = requests.post(url = URL, data = outgoing_json_data)
    incoming_data = r.json()
    print(incoming_data)



##-------------------------
#fn for requesting to PUTting/updating data on server side
def update_data():
    #this dict data we will post to server
    outgoing_data = {
        'id': 6,
        'name': 'Jack',
        'city': 'Indore',
        'roll': 76,
    }

    outgoing_json_data = json.dumps(outgoing_data)

    #requests.post will send data to the server and receive
    #-a response in 'r'
    r = requests.put(url = URL, data = outgoing_json_data)
    incoming_data = r.json()
    print(incoming_data)



#a fn to delete student data by passing the id
def delete_data():
    data = {'id': 8}

    out_json_data = json.dumps(data)
    r = requests.delete(url = URL, data = out_json_data)
    data = r.json()
    print(data)


#callling this fn with id 1 to get and print the data of student id 1 from the server
#get_data(1)
#get_data(3)
#get_data()

delete_data()

#update_data()

#post_data()

#update_data()