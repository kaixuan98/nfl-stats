import boto3 
import json 
import os
from dotenv import load_dotenv

load_dotenv()

aws_access_key = os.environ.get("AWS_ACCESS_KEY")
aws_secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")


s3 = boto3.client('s3', aws_access_key, aws_secret_key)

# create meta data for each scrape


# naming stategy 
# example: raw/2024/weekXX/<stats>.json


# upload with file and data
# def upload_to_s3(data, stats_name, week, year="2024"):