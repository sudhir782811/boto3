import boto3
from pprint import pprint
session_con = boto3.session.Session(profile_name="sud")
ec2_re = session_con.client(service_name="ec2", region_name="eu-central-1")

response = ec2_re.describe_instances()
for i in response['Reservations']:
    for t in (i['Instances']):
        print("instance id is: {} and image id is: {} and instance type is: {}".format(t['InstanceId'],t['ImageId'],t['InstanceType']))