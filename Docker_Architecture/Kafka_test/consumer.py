from kafka import KafkaConsumer
import json


if __name__ == '__main__':

    consumer = KafkaConsumer(
    "devices",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset='earliest',
    group_id="spark-consumer"
    )

    for message in consumer:
        print("Positions + {}".format(json.loads(message.value)))

