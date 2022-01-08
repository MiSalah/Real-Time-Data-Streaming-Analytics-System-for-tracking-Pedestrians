from kafka import KafkaProducer
import json
import time as t
from data import get_users

def json_serialize(data):
    return json.dumps(data)


producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=json_serialize)

if __name__ == '__main__':
    while 1==1:
        users = get_users()
        print(users)
        producer.send("positions",users)
        t.sleep(3)


