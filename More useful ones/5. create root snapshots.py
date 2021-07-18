# to create root volume snapshots we need the instance ids of ec2s 

import boto3


ec2  = boto3.client("ec2")
 
x = []         # empty list to store all ec2 instanceids 

response = ec2.describe_instances() 
for each_item in response['Reservations']:
	for each_instance in each_item['Instances']:
		print(each_instance['InstanceId'])
        x.append(each_instance['InstanceId'])


for each in x:

    y = ec2.client.create_snapshots(           # y is just a variable to store required
                                               # output
                                           
    
    InstanceSpecification=
    {
        'InstanceId': x[each],
        'ExcludeBootVolume': False
    },
    TagSpecifications=
    [
        {
            'Tags': [
                {
                    'Key': 'name',
                    'Value': 'my volume'
                },
            ]
        },
    ],
    )

    # repsonse will store new created snapshot ids and other metadata
    #  in a dictionary format 
    print ( y['snapshot_id'] )