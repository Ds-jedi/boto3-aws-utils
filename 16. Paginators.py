# paginator concept to list all iam users and ec2 instance Ids
# usually resource and client object will only show data available on 1st page only 
# (around 50 -100 ) . But will skip tpage 2,3,4,etc .

import boto3 

iam= boto3.session.client("iam")
paginator = iam.get_paginator('list_users')       # go to boto3-->ec2-->client-->paginators
                                                  # --> list_users

x = paginator.paginate()                          # x stores data of alll those pages

for each_page in  x:
    for each_user in each_page['Users']:          # iterate thorugh all thoses pages 
       print (each_user['UserName']) 


ec2 = boto3.session.client("ec2")
paginator = ec2.get_paginator('describe_instances')

x = paginator.paginate() 

for each_item in x['Reservations']:
	for each_instance in each_item['Instances']:
		print(each_instance['InstanceId'])

