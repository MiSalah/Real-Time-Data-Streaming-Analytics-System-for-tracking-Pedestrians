#from kafka import KafkaProducer
from pymongo import MongoClient
from bson.json_util import dumps
import json
import time as t

""" json_data_position = dumps(positions, indent = 2)
json_data_devices= dumps(devices, indent = 2) """
client = MongoClient('mongodb+srv://ikram:ikram123@cluster0.kx5fr.mongodb.net/Timestamp')
database = client.Timestamp

def get_positions():
    
    positions_collection = database.positions
    positions = list(positions_collection.find({}))
    
    return positions, len(positions)


def get_devices():

    devices_collection = database.devices
    devices = list(devices_collection.find({}))
    return devices, devices_collection.count_documents({}) 

""" for i in range(len(positions)-1,len(positions)):
    print(positions[i])

print(positions[-1]) 
 """

""" new_rank=0

while 1==1:
    
    positions, count = get_positions()
    print(count, new_rank)
    if count > new_rank:
        print(count, new_rank)
        #rank=count-new_rank
        print(len(positions))
        for i in range(new_rank,count):
            print(new_rank,count)
            print(positions[i])
            print("sent")
            print('=================\n')
        new_rank=count
        print(new_rank)
    t.sleep(10) """




# def json_serialize(data):
#     return json.dumps(data)

#print(positions.count_documents({}))
#print(devices.count_documents({}))
""" 
for position in positions:
    print(position)
    print("===========================\n")

for device in devices:
    print(device)
    print("===========================\n") 
 """


""" 
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x: dumps(x).encode('utf-8'))

if __name__ == '__main__':

    with open('data_position.json') as f:
        data = json.load(f)
    producer.send('positions', value=positions)
    producer.send('devices',value=devices)
    t.sleep(3)
 """

