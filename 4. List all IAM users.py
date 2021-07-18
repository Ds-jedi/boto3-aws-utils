import boto3

iam = boto3.resource('iam')

for each_item in iam.users.all():
	print(each_item.user_name)


#######################################################################################


iam = boto3.client('iam')

response = iam.list_users()             # list_users shows a dictionary , 
                                        # which has a users key inside which username 
                                        # is present

# response is a variable inside which we are storing the data ,u can name it anything

for each_item in response['Users']:     # go inside users key which is a list
    print(each_item['UserName'])        # print username