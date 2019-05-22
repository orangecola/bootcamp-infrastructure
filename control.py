import boto3, os, json
from botocore.exceptions import ClientError

instances = [os.environ['instance']]
def start(event, context):
    try: 
        ec2 = boto3.client('ec2')
        ec2.start_instances(InstanceIds=instances)
        return formatOutput("Instance Started, run /check to determine IP Address of bootcamp server")
    except ClientError as e:
        return(e)

def stop(event, context):
    try: 
        ec2 = boto3.client('ec2')
        ec2.stop_instances(InstanceIds=instances)
        return formatOutput("Instance Stopped")
    except ClientError as e:
        return(e)

def check(event, context):
    try: 
        ec2 = boto3.client('ec2')
        response = ec2.describe_instances(InstanceIds=instances)
        instance = response['Reservations'][0]['Instances'][0]
        if 'PublicIpAddress' in instance:
            result = "Server is at " + instance['PublicIpAddress']
        else:
            result = "Server does not have a public IP Address. Did you turn on the server with /start? If so wait a few moments for the server to start and try again." 
        return formatOutput(result)
    except ClientError as e:
        return(e)

def formatOutput(output):
	return {
        "statusCode": 200,
        "body": output
    }