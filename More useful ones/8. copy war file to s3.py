# copy .war file in current directory to s3


import boto3
import os

iam = boto3.client("s3")

for file in os.listdir():                              # searches file in current directory
    if '.war' in file:                                  # if .war files are present 
        upload_file_bucket = 'my-dummy-bucket'               # ur s3 bucket name
        upload_file_key = 'myfolder/' + str(file)           # ur folder path inside bucket
                                                            # files will be saved in myfolder/something.war 
        iam.upload_file(file, upload_file_bucket, upload_file_key)

    if '.py' in file:
        upload_file_bucket = 'my-dummy-bucket'
        upload_file_key = 'python/' + str(file)
        iam.upload_file(file, upload_file_bucket, upload_file_key)