from pymongo import MongoClient
import csv
import pandas as pd
import boto3
from botocore.exceptions import NoCredentialsError
client = MongoClient ("mongodb+srv://ikram:ikram123@cluster0.kx5fr.mongodb.net/Timestamp")
db=client["Timestamp"]
collection_currency = db["positions"]
collection_dev = db["devices"]
cursor1 = collection_currency.find({})
cursor2 = collection_dev.find({})
position_docs=list(cursor1)
device_docs=list(cursor2)
positions = []
for i in position_docs:
    for j in range(0,len(i['positions'])):
        positions.append(i['positions'][j])
for i in positions:
    for j in i['attributes'].keys():
        i[j]=i['attributes'][j]
for j in positions:
    j.pop('attributes',None)
keys = positions[0].keys()
with open('positions.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(positions)
devices = []
for i in device_docs:
    for j in range(0,len(i['devices'])):
        devices.append(i['devices'][j])
for i in devices:
    i.pop('attributes',None)
    i.pop('geofenceIds',None)
    i.pop('phone',None)
    i.pop('model',None)
    i.pop('contact',None)
    i.pop('category',None)
keys = devices[0].keys()
with open('devices.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(devices)
ACCESS_KEY = 'AKIA3EC5YFFBPZYRRAPC'
SECRET_KEY = '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'
def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
uploaded = upload_to_aws('positions.csv', 'projectofkarim', 'positions.csv')
uploaded = upload_to_aws('devices.csv', 'projectofkarim', 'devices.csv')
