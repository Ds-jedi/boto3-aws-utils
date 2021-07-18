import boto3

root_session = boto3.session.Session(profile_name="root")

sts= root_session.client('sts')

response=sts.get_caller_identity()
print(response.get('Account'))



ec2_dev_session = boto3.session.Session('ec2_developer')

sts =  ec2_dev_session.client('sts')

response=sts.get_caller_identity()
print(response['Account'])