import boto3
import csv

ec2_=boto3.resource("ec2")
cnt=1
csv_ob = open("inventory_info.csv","w",newline='')
csv_w = csv.writer(csv_ob)
csv_w.writerow(["S_NO","Instance_Id",'Instance_Type','Architecture','LaunchTime','Privat_Ip'])
for each in ec2_.instances.all():
	print(cnt,each,each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.private_ip_address)
	csv_w.writerow([cnt,each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.private_ip_address])

	cnt+=1
csv_ob.close()