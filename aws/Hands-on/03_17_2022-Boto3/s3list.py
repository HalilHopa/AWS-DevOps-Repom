import boto3

# Use Amazon S3
s3 = boto3.resource('s3')

# Upload a new file
data = open('new.txt', 'rb')
s3.Bucket('halil-boto3-bucket').put_object(Key='new.txt', Body=data)