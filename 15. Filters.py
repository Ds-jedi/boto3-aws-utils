# u have multiple intances . U need to collect data of specific instances based on
# running state and instance type . U use collections with filters .

import boto3

ec2=boto3.resource("ec2")

# goto boto3 ec2 docs --> service resources --> go to 3rd part (collections)
# --> instances --> go to filters --> additional filters 

f1={"Name": "instance-state-name", "Values":['running','stopped']}
f2={"Name":"instance-type","Values":['t2.micro']}

for each in ec2.instances.filter(Filters=[f1,f2]):
	print(each)