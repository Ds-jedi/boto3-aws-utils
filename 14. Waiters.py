# suppose u want to create an ec2 , and after creating script displays that it is running
# but ec2 doesnt start immediately , it goes to pending state for around 10-15 sec
# and then it starts . If u implement waiters , ur script will wait for ec2 to start
# and then display that it works


# using client

import boto3 
import time


ec2 = boto3.client("ec2")

print("Starting ec2 instace...")

ec2.start_instances(InstanceIds=['i-002d4110f1199166f'])

waiter = ec2.get_waiter('instance_running')   

# refer docs boto3 --> ec2--> waiter --> EC2.Waiter.InstanceRunning

waiter.wait(InstanceIds=['i-002d4110f1199166f']) 

print("Now your ec2 instace is up and running")



###########################################################################

# using resource 

import boto3 
import time


ec2 = boto3.resource("ec2")

print("Starting ec2 instace...")

x = ec2.Instance("i-002d4110f1199166f")

# ec2.instance returns bunch of objects which includes start() and wait_until_running()
# use print (dir(x)) to get info

print("Starting given instance....")

x.start()

x.wait_until_running()  

print("Now your instance is up and running")

##############################################################################

# taking ec2 id input from user 

import boto3 
import time


ec2 = boto3.client("ec2")

my_ec2_id = input('Enter your EC2 Instance Id: ')
print("Starting ec2 instance...")

ec2.start_instances(InstanceIds=[ my_ec2_id ])
waiter = ec2.get_waiter('instance_running')   
waiter.wait(InstanceIds=[ my_ec2_id ]) 
print("Now your ec2 instace is up and running")