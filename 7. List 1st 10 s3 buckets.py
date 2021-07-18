import boto3

s3 = boto3.resource('s3')


for each_item in s3.buckets.limit(10):
	print(each_item.name)