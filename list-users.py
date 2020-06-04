import boto3
session_con = boto3.session.Session(profile_name="sud")
iam_client = session_con.client(service_name="iam", region_name="eu-central-1")

response = iam_client.list_users()
for i in response['Users']:
    print(i['UserName'])
