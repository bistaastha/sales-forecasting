import os
import boto3
from botocore.exceptions import ClientError
access_key_id = 'AKIA3BJD2GLQLZVVGBFL'
secret_access_key = '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'
bucket_name = 'foldercsv'

s3_client = boto3.client(
    's3',
    aws_access_key_id = access_key_id,
    aws_secret_access_key = secret_access_key
)
# getting file storage path

datapath = os.path.join(os.getcwd() + '/data')
try:
    s3_client.upload_file(
        os.path.join(datapath, 'out.csv'),
        bucket_name, 
        'out.csv'
    )
except ClientError as e:
    raise e
