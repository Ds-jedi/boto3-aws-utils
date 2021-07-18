# using meta u do client operations using resource
# suppose u need to show regionsname of ec2 , u cant do that with resource
# u can do that only through client 

import boto3


ec2 = boto3.resource("ec2")

for each_item in boto3.meta.client.describe_regions()['Regions']:
	
    print(each_item['RegionName'])
