from kafka import KafkaConsumer
consumer = KafkaConsumer('positions', bootstrap_servers=['localhost:9092'])
print("hello")
for message in consumer:
    print(message)