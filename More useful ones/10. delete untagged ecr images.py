# delete untagged ecr images , coz ecr can store only 1000 images

import boto3

client = boto3.client('ecr')

response = client.list_images(repositoryName='my repo')
untaggedImageList = []              # created empty list

for each in response['imageIds'] :
    if each['imageTag' == 'untagged'] :
        untaggedImageList.append(response["imageids"])

response2 = client.batch_delete_image(repositoryName='my repo', imageIds=untaggedImageList)

print(response2)