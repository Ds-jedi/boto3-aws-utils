

import boto3 

ec2 = boto3.resource('ec2')

# create VPC

vpc = ec2.create_vpc(CidrBlock='192.168.0.0/16')

# we can assign a name to vpc, or any resource, by using tag

vpc.create_tags(Tags=[{"Key": "Name", "Value": "default_vpc"}])

vpc.wait_until_available()

print(vpc.id)




