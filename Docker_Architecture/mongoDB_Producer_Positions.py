from kafka import KafkaProducer
import json
import time as t

from bson.json_util import dumps, loads
from MongoDB_data import get_positions

""" def json_serialize(data):
    return dumps(data) """

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x:dumps(x).encode('utf-8'))


def process_positions(position):
    
    position.pop("_id")
    
    for j in position['positions'][0]['attributes'].keys():
        position['positions'][0][j]=position['positions'][0]['attributes'][j]
    
    position['positions'][0].pop('attributes')
    
    pops = ['type','protocol','serverTime','deviceTime','outdated','network']
    
    for pop in pops:
        position['positions'][0].pop(pop)
    
    devices= {
    1:"ELBAIDOURY",
    3:"SAIDI",
    4:"ESSABRI",
    16:"JAD",
    17:"others"
    }
    
    if position['positions'][0]['deviceId'] == 1:
        position['positions'][0]['name'] = devices[1]
    elif position['positions'][0]['deviceId'] == 3:
        position['positions'][0]['name'] = devices[3]
    elif position['positions'][0]['deviceId'] == 4:
        position['positions'][0]['name'] = devices[3]
    elif position['positions'][0]['deviceId'] == 16:
        position['positions'][0]['name'] = devices[16]
    elif position['positions'][0]['deviceId'] == 17:
        position['positions'][0]['name'] = devices[17]

    returned = position['positions'][0]
    return returned

if __name__ == '__main__':

    new_rank=0

    while 1==1:
    
        positions, count = get_positions()
        print(count, new_rank)

        if count > new_rank:
            print(count, new_rank)
            #rank=count-new_rank
            print(len(positions))
            for i in range(new_rank,count):
                processed_position = process_positions(positions[i])
                producer.send("positions",processed_position)
                print(processed_position)
                print("sent")
                print('=================\n')
        new_rank=count
        print(new_rank)
        t.sleep(10)