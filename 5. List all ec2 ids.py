import boto3

ec2 = boto3.resource('ec2')

response = ec2.instances.all()   # will return a list use for loop to get additional info
								 # print (get(response)) will list all operations on response










#################################################################

import boto3

ec2 = boto3.client('ec2')

response= ec2.describe_instances()

for each_item in response['Reservations']:
	for each_instance in each_item['Instances']:
		print(each_instance['InstanceId'])