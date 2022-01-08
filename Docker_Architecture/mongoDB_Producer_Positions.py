from kafka import KafkaProducer
import json
import time as t
#from data import get_users
from bson.json_util import dumps, loads
from MongoDB_data import get_positions

""" def json_serialize(data):
    return dumps(data) """

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x:dumps(x).encode('utf-8'))

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
                producer.send("positions",positions[i])
                print(positions[i])
                print("sent")
                print('=================\n')
        new_rank=count
        print(new_rank)
        t.sleep(10)

