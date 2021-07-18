===========================================================================

import boto3

root_session=boto3.session.Session(profile_name="root")

iam=root_session.resource('iam')


#Listiing iam users with resource object:

for user in iam.users.all():
    print(user.name)

==============================================================================

#### using client object 

import boto3

root_session=boto3.session.Session(profile_name="root")
iam=root_session.client('iam')


#Listiing iam users with client  object:

for each in iam.list_users()['Users']:
   print(each['UserName'])

============================================================================

### using multiple sessions


import boto3

root_session=boto3.session.Session(profile_name="root")
nigga_session=boto3.session.Session(profile_name="nigga")

iam_root=root_session.resource('iam')
iam_nigga=nigga_session.client('iam')



for user in iam.users.all():
    print(user.name)














