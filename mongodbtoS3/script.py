from pymongo import MongoClient
import pandas as pd
import boto3
from botocore.exceptions import NoCredentialsError
client = MongoClient ("mongodb+srv://XXXXXX:XXXXXXX@cluster0.kx5fr.mongodb.net/Timestamp")
db=client["Timestamp"]
collection_currency = db["positions"]
collection_dev = db["devices"]
cursor1 = collection_currency.find({})
cursor2 = collection_dev.find({})
position_docs=list(cursor1)
device_docs=list(cursor2)
docs_pos=pd.DataFrame(columns=[])
docs_dev=pd.DataFrame(columns=[])
for num,doc in enumerate(position_docs):
    doc["_id"]=str(doc["_id"])
    doc_id=doc["_id"]
    series_obj = pd.Series( doc, name=doc_id )
    docs_pos = docs_pos.append( series_obj )
for num,doc in enumerate(device_docs):
    doc["_id"]=str(doc["_id"])
    doc_id=doc["_id"]
    series_obj = pd.Series( doc, name=doc_id )
    docs_dev = docs_dev.append( series_obj )
ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXX'
SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXX'
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
docs_pos.to_csv('positions.csv',sep=",")
docs_dev.to_csv('devices.csv',sep=',')
uploaded = upload_to_aws('positions.csv', 'projectofkarim', 'positions.csv')
uploaded = upload_to_aws('devices.csv', 'projectofkarim', 'devices.csv')
###docs_pos.to_json("pos.json")
###docs_dev.to_json("dev.json")