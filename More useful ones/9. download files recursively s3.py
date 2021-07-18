# copy all files recursively using boto3 python, easiest way is to use aws cli
# aws s3 cp --recursive s3://my_bucket_name local_folder

import os
import boto3

pwd = os.getcwd()     # get cuurent directory
s3 = boto3.resource('s3')
my_bucket = s3.Bucket('my_bucket_name')     # select ur bucket

# Amazon S3 does not have folders/directories. It is a flat file structure.

# To maintain the appearance of directories, path names are 
# stored as part of the object Key (filename). For example:

#  images/foo.jpg 

# In this case, the whole Key is images/foo.jpg, 
# rather than just foo.jpg.


# os.path.split(s3_object.key)
# this splits images/foo.jpg to a tuple = ["images" , "foo.jpg"]
# we store images as f_path and foo.jpg as f_name
# if ur object is a file , then ur f_path will be empty
# to download we use s3.download_file( "ur -bucket-name", filename , dest path )

for s3_object in my_bucket.objects.all():
    
    f_path , f_name = os.path.split(s3_object.key)
    if f_path == '' :
      s3.download_file( "my-bucket", f_name , pwd )
    else :
      new_path = os.path.join(pwd, f_path)
      os.makedirs(new_path)
      s3.download_file( "my-bucket" , f_name , new_path)
