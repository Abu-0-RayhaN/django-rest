import requests
import json
URL="http://localhost:8000/studentapi/"
#this get_data function is requesting for data to our api. 
# This is taking an id and converting it into json data.
# then it will send this to our api. Api will take the id 
# and send the data of the student whose id is one.
def get_data(id =None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL, data=json_data)
    data=r.json()
    print(data)
    
def post_data():
    data={
        'name':'rayan',
        'roll':170,
        'city':'Cumilla'
    }
    json_data=json.dumps(data)
    r= requests.post(url=URL, data=json_data)
    data=r.json()
    print(data)

def update_data():
    data={
        'id':5,
        'name':'Rayhan',
        'city':'dhaka(update)'
    }
    json_data=json.dumps(data)
    r= requests.put(url=URL, data=json_data)
    data=r.json()
    print(data)
def delete_data():
    data={'id':3} 
    json_data=json.dumps(data)
    r= requests.delete(url=URL, data=json_data)
    data=r.json()
    print(data)

post_data()