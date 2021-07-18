import boto3
import sys

ec2 = boto3.resource('ec2')

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
            x = ec2.Instance(instance_id)

            # go to middle section of service resource of ec2 
            # coz u need to do operation on exiting stuffs , not new stuffs
            # x is  variable object that stores data return by ec2.Instance(instance_id)
            # print(dir(x)) to see all the options 
            
            print("Starting ec2 instance.....")
            x.start()

	elif opt==2:
            instance_id=input('Enter your EC2 Instance Id: ')
            x = ec2.Instance(instance_id)
            print("Stopping ec2 instance.....")
            x.stop()

	elif opt==3:
            instance_id=input('Enter your EC2 Instance Id: ')
            x = ec2.Instance(instance_id)
            print("Terminating ec2 instance.....")
            x.terminate()
            
	elif opt==4:
            print("Thank you for using this script")
            sys.exit()
	else:
	    print("Your option is invalid. Please try once again")



