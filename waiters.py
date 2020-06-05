import boto3
aws_mag_con=boto3.session.Session(profile_name="sud")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="eu-central-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="eu-central-1")

ec2_con_cli.start_instances(InstanceIds=['i-07ddab99f1ed060e8'])
waiter = ec2_con_cli.get_waiter('instance_running') #it will wait until the instance is reached to running status.
waiter.wait(InstanceIds=['i-07ddab99f1ed060e8'])
print("instance is up and running")