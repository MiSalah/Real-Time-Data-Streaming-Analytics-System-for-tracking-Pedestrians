import boto3
import os
s3 = boto3.client('s3', aws_access_key_id='&YOUR_ACCESS_KEY' , aws_secret_access_key='&YOUR_SECRET_KEY')
s3.download_file('projectofkarim', 'positions.csv', os.path.join('.','positions.csv'))
s3.download_file('projectofkarim', 'devices.csv', os.path.join('.','devices.csv'))