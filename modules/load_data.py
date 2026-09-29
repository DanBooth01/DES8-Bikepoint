import os
import boto3
from dotenv import load_dotenv
import logging
from datetime import datetime


logger = logging.getLogger(__name__)

def s3_upload(data_dir:str,AWS_ACCESS_KEY:str, AWS_SECRET_ACCESS_KEY:str, AWS_BUCKET_NAME:str):
    """Uploads all files in the data dictionary

    Args:
        data_dir (str): Where the data is
        AWS_ACCESS_KEY (str): Linked to AWS IAM User
        AWS_SECRET_ACCESS_KEY (str): Linked to AWS IAM User
        AWS_BUCKET_NAME (str): s3 bucket to upload
    """
    
    s3_client = boto3.client(
        's3',
        aws_access_key_id = AWS_ACCESS_KEY,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    )


    files_to_upload = os.listdir('data')

    for file in files_to_upload:
        file_to_upload = f'data/{file}'
        filename_s3 = file
        try:
            s3_client.upload_file(file_to_upload, AWS_BUCKET_NAME, filename_s3)
            print(f'{file} uploaded successfully')
            logger.info(f'{file} uploaded successfully')
            os.remove(file_to_upload)
        except Exception as e:
            print(f'An error has occured: {e}')
            logger.error(f'An error has occured: {e}')

