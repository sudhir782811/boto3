import boto3
aws_mag_con=boto3.session.Session(profile_name="sud")
ec2_con_re=aws_mag_con.resource(service_name="ec2", region_name='eu-central-1')
f1={"Name": "instance-state-name", "Values":['running', 'stopped']}
f2={"Name": "instance-type", "Values":['t2.micro']}
for i in ec2_con_re.instances.filter(Filters=[f1,f2]):
    print(i)