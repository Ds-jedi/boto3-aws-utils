# reate an AWS CLI script using Python and the Boto3 library. I want the script to 
# ask for inputs (username? programmatic access? attach to which Group? 
# Change password on first login? etc.) and set up the user with those details.

import boto3 

iam = boto3.client("iam")

ur_email = input("Please enter your e-mail address: ")

response1 = iam.create_user( UserName = ur_email )

x = input("Do you require programmatic access?(y/n): ") 

if x == "y":
        iam.create_access_key( UserName = ur_email )
        print("access key created")
        print("Make sure awscli is installed on your machine")
elif x == "n":
        print("Console access only")




response2 = iam.list_groups()
groups = response2['Groups']
index = 1

for each in groups:
    print(f'{index}: {each["GroupName"]}')
    index += 1

option = int(input("Please pick a group number: "))
arn = groups[option-1]["Arn"]             # arn is the group's policy arn . we need this
                                          # arn to attach user to that group 

'''
Output will be like this

1: admins
2: devops
3: programmers
Please pick a group number: 2
You selected option 2: arn:aws:iam::123456781234:group/devops

'''


response3 = iam.attach_group_policy(
    GroupName = groups[option-1][ "GroupName" ] ,
    PolicyArn = arn
)


