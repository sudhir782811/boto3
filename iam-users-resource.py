import boto3
session_con = boto3.session.Session(profile_name="sud")
ec2_re = session_con.resource(service_name="iam", region_name="eu-central-1")

for i in ec2_re.users.all():
    print(i.user_name)