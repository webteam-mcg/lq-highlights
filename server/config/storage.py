import boto3 as boto3
from botocore.config import Config

s3_resource = boto3.resource('s3',
                             endpoint_url='http://localhost:9000',
                             aws_access_key_id='minio',
                             aws_secret_access_key='minio123',
                             config=Config(signature_version='s3v4'),
                             region_name='us-east-1')

s3_client = boto3.client('s3',
                         endpoint_url='http://localhost:9000',
                         aws_access_key_id='minio',
                         aws_secret_access_key='minio123',
                         config=Config(signature_version='s3v4'),
                         region_name='us-east-1')

raw_footage_bucket = s3_resource.Bucket('raw-footage')
