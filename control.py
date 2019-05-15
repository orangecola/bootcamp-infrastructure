import boto3, os
from botocore.exceptions import ClientError

instances = [os.environ['instance']]
def start(event, context):
    try: 
        ec2 = boto3.client('ec2')
        ec2.start_instances(InstanceIds=instances)
    except ClientError as e:
        return(e)