import boto3
session_con = boto3.session.Session(profile_name="sud")
s3_re = session_con.resource(service_name="s3", region_name="eu-central-1")

for i in s3_re.buckets.all():
    print(i.name)
##we can also use limit to see top 10 bucket

## for i in s3_re.buckets.limit(10):
    #print(i.name)
