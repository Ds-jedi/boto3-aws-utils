## listing all snapshots of every aws account


import boto3


ec2 = boto3.resource("ec2")


for each_snap in ec2.snapshots.all:
	print(each_snap)