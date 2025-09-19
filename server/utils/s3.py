# server/utils/s3.py
import logging
import boto3
from botocore.exceptions import ClientError

class AwsS3UploadClass(object):
  def __init__(self, key_id, secret_key, bucket_name):
    self.key_id = key_id
    self.secret_key = secret_key
    self.bucket_name = bucket_name

    self.client = boto3.client('s3', endpoint_url=None, aws_access_key_id=self.id_key, aws_secret_access_key=self.secret_key, region_name='ca-central-1')

  def get_bucket(self, bucket_name):
    try:
      bucket = self.client.get_bucket(bucket_name)
    except ClientError as e:
      bucket = None
    return bucket

  def create_presigned_post(self, object_name, fields=None, conditions=None, expiration=3600):
    s3_client = boto3.client('s3')
    try:
      response = s3_client.generate_presigned_post(self.bucket_name,object_name, Fields=fields, Conditions=conditions, ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None
    # The response contains the presigned URL and required fields
    return response
  
