# delete all those ebs volumes that are unused (ie available) and are untagged


import boto3


ec2=boto3.resource("ec2")

f_ebs_unused={"Name":"status","Values":["available"]}
for each_volume in ec2.volumes.filter(Filters=[f_ebs_unused]):
	if not each_volume.tags:
		print(each_volume.id, each_volume.state,each_volume.tags)
		print("Deleting unused and untagged volumes.....")
		each_volume.delete()

print("Delted all unused unatageed volumes.")
