import boto3
import sys

ec2 = boto3.client("ec2")


while True:
	print("This script performs the following actions on ec2 instance")
	print("""
		1. start
		2. stop
		3. terminate
		4. Exit""")
	opt=int(input("Enter your option: "))
	if opt==1:
            instance_id=input('Enter your EC2 Instance Id: ')
            
            #print(dir(my_req_instance_object))
            
            print("Starting ec2 instance.....")
            
            ec2.start_instances(InstanceIds=[instance_id])

            # above logic available in boto3 docs 
            # ec2 --> clients --> start_instances --> syntax


	elif opt==2:
            instance_id=input('Enter your EC2 Instance Id: ')
            print("Stopping ec2 instance.....")
            ec2.stop_instances(InstanceIds=[instance_id])

	elif opt==3:
            instance_id=input('Enter your EC2 Instance Id: ')
            print("Terminating ec2 instance.....")
            ec2.terminate_instances(InstanceIds=[instance_id])

	elif opt==4:
            print("Thank you for using this script")
            sys.exit()
            
	else:
	    print("Your option is invalid. Please try once again")