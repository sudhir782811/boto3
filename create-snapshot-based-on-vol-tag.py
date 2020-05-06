import boto3

session = boto3.session.Session(profile_name="sud")
ec2_client = session.client(service_name="ec2", region_name="eu-central-1")

prod_vol = {"Name": 'tag:ENV', 'Values': ['Prod']}
response = ec2_client.describe_volumes(Filters=[prod_vol])
my_vol_id = []
for i in response['Volumes']:
    my_vol_id.append(i['VolumeId'])
    print('going to take snapshot of volumes: {}'.format(my_vol_id))

    response = ec2_client.create_snapshot(
        Description="boto3" + i['VolumeId'],
       VolumeId=i['VolumeId']
    )

    print('snapshot has been done of vol: {}'.format(my_vol_id))
