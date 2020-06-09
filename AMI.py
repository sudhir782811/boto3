import boto3
from datetime import datetime
aws_mag_con=boto3.session.Session(profile_name="sud")
ec2_con_cli=aws_mag_con.client(service_name="ec2", region_name='eu-central-1')

f1={"Name": "tag:ENV", "Values":['Prod']}
ins_id=[]
response = ec2_con_cli.describe_instances(Filters=[f1])
for i in response['Reservations']:
    for t in i['Instances']:
        ins_id.append(t['InstanceId'])

        ec2_con_cli.create_image(
            InstanceId=t['InstanceId'],
            Name="Boto3" + t['InstanceId']
            )

        print("taking image backup of {}".format(ins_id))