import boto3
aws_mag_con=boto3.session.Session(profile_name="sud")
ec2_con_re=aws_mag_con.resource(service_name="ec2", region_name='eu-central-1')

unused_ebs={"Name": "status", "Values":['available']}
for i in ec2_con_re.volumes.filter(Filters=[unused_ebs]):
    if not i.tags:
        print(i.id, i.state, i.tags)

        print("unused and untagged volume has been deleted")