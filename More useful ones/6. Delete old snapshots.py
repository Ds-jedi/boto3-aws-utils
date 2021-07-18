# delete snapshots older than 10 days , if a snapshot is in use it shows this
# error == botocore.exceptions.ClientError: An error occurred (InvalidSnapshot.InUse) 
# when calling the DeleteSnapshot operation: The snapshot snap-12345678 is currently 
# in use by ami-12345

import boto3
import datetime

ec2 = boto3.client('ec2')

response = ec2.describe_snapshots()

for each in response['Snapshots']:
    a = each['StartTime']                            
    b = a.date()                                     # age of snapshot
    c = datetime.datetime.now().date()               # current time 
    d = c-b                                          # current time - age of snapshot
    
    try:
        if d.days>10:
            id = each['SnapshotId']
            ec2.delete_snapshot(SnapshotId=id)
    
    except Exception as e:                             # created exception e (u can name it anything)
        if 'InvalidSnapshot.InUse' in e.message:       # if ur code shows error with string 'InvalidSnapshot.InUse'
           print ("skipping this snapshot")            # it will show (" skiping this snapshot")
           continue