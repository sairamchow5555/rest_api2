import json
import requests

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT ='api/'
# def get_resource(id = None):
#     data = {}
#     if id is not None:
#         data ={
#         'id':id
#         }
#     resp = requests.get(BASE_URL + END_POINT,data = json.dumps(data))
#     print(resp.json())
#     print(resp.status_code)
#
# get_resource(1)

def create_resource():
    new_emp ={
    'eno':107,
    'ename':'JR.NTR',
    'esal':25001,
    'eaddr':'India'
    }
    resp = requests.post(BASE_URL + END_POINT,data = json.dumps(new_emp))
    print(resp.json())
    print(resp.status_code)

create_resource()

# def update_resource(id):
#     emp = {
#     'id':id,
#     'esal':19999,
#     'eaddr':'London'
#     }
#     resp = requests.put(BASE_URL + END_POINT,data = json.dumps(emp))
#     print(resp.json())
#     print(resp.status_code)
#
# update_resource(3)

# def delete_resource(id):
#     emp = {
#     'id':id
#     }
#     resp = requests.delete(BASE_URL + END_POINT,data = json.dumps(emp))
#     print(resp.json())
#     print(resp.status_code)
#
# delete_resource(5)
