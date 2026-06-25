
# Import all the modules and libraries
import boto3
from pprint import pprint

#Open Management Console
aws_management_console=boto3.session.Session(profile_name="default")

#Open IAM Console
iam_console=aws_management_console.client(service_name='iam')

#Use Boto3 Documentation to get more information
result=iam_console.list_users()
pprint(result['Users'])
