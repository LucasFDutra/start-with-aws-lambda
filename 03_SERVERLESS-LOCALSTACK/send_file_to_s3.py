import boto3

config_s3 = {
    'service_name': 's3',
    'aws_access_key_id': '123',
    'aws_secret_access_key': '123',
    'endpoint_url': 'http://localhost:4566'
}

my_bucket = 'teste'
test_file = 'teste.csv'

s3 = boto3.client(**config_s3)

s3.put_object(Body=test_file, Bucket=my_bucket, Key=test_file) 
objects_list = s3.list_objects_v2(Bucket=my_bucket)
print(objects_list)