import requests
import json
URL= "http://localhost:8000/studentapi/26/"

def get_data(id = None):
    data={}
    if id is not None:
        data={'id':id}
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.get(url=URL, data=json_data,headers=headers)
    data= r.json()
    print(data)
#get_data(24)
def post_data():
    data={
        'name':'ruman',
        'roll':21,
        'city':'dhaka'
    }
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data,headers=headers)
    data=r.json()
    print(data)
#post_data()
def update():
    data={
        'id':23,
        'city':'pabna',
        'name':'Suhana Rahman khan faria',
        'roll':198
        
    }
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.put(url = URL, data = json_data,headers=headers)
    data=r.json()
    print(data)
update()
def delete():
    data={
        'id':25
    }
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.delete(url = URL, data = json_data,headers=headers)
    data=r.json()
    print(data)