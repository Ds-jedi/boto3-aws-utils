
### assign ipv6 to my ec2 using client 

import boto3

ec2 = boto3.client('ec2')

response = client.assign_private_ip_addresses(
    NetworkInterfaceId='eni-e5aa89a3',
    PrivateIpAddresses=[
        '10.0.0.82',
    ],
)

print(response)

