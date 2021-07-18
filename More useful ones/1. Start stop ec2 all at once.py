# boto3 script to start , stop , restart ec2 (with certain tag name) all at once 

import boto3

ec2 = boto3.client("ec2")


x=[]                      # empty list created

f1={"Name": "tag:Name", "Values":['Non_Prod']}
for each_item in ec2.describe_instances(Filters=[f1])['Reservations']:
	for each_in in each_item['Instances']:
		x.append(each_in['InstanceId'])        # stored all our instance id in that empty list
print(x)

print("Starting intances with ids of : ",x)


ec2.start_instances(InstanceIds=x)
waiter=ec2.get_waiter('instance_running')
waiter.wait(InstanceIds=x)
print("Your np instances are up and running....")