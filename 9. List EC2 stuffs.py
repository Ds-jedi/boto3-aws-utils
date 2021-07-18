# List instance ID  , image id , launch time in Ec2

import boto3


ec2 = boto3.client('ec2')


response=ec2.describe_instances()['Reservations']               

for each_item in response:	
    for each in each_item['Instances']:
		
		print(each['ImageId'])
    print(each['InstanceId'])
    print(each['LaunchTime'].strftime("%Y-%m-%d") )


# to get image ids and other stuffs , you need to go inside 
# describe instances returns a dictionary , go inside reservations key ,
# it will show a list , go to instances  , instances will return a dictionary ,
# then print ur stuffs required

# for more help  , goto boto3 docs
# ec2 --> client --> describe instances --> returns 
