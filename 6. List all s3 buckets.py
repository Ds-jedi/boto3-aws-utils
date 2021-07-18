import boto3

s3 = boto3.resource('s3')


for each_item in s3.buckets.all:
	print(each_item.name)



########################################################

import boto3

s3 = boto3.resource('s3')


response=s3.list_buckets()

for each_item in response['Buckets']:
	print(each_item['Name'])
	
    #print(each_item.get('Name'))
