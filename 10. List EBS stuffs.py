# list all VolumeIDs , AZs and volume type of a ebs volumes

import boto3


ec2 = boto3.client('ec2')


response=ec2.describe_volumes()['Volumes']

for each_item in response:
	
    print( each_item['VolumeId'] )
    print( each_item['AvailabilityZone'] )
    print( each_item['VolumeType'] )


# describe volumes returns a dict , go inside volumes key , which 
# returns a list , print ur stuffs from that list
