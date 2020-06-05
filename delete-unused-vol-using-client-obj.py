import boto3
aws_mag_con=boto3.session.Session(profile_name="sud")
ec2_con_re=aws_mag_con.client(service_name="ec2", region_name='eu-central-1')

response = ec2_con_re.describe_volumes()
for i in response['Volumes']:
    #if 'State' in i and i['State'] == "available":
    if not 'Tags' in i and i['State'] == "available":
        print(i['VolumeId'])

        ec2_con_re.delete_volume(VolumeId=i['VolumeId'])

        print("unused volume has been deleted")