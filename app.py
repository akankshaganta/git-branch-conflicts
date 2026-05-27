import boto3
from botocore.exceptions import ClientError

# Create S3 client
s3 = boto3.client("s3")

bucket_name = "my-unique-bucket-name-12345"
region = "ap-south-1"   # Mumbai region

try:
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            "LocationConstraint": region
        }
    )

    print(f"Bucket '{bucket_name}' created successfully!")

except ClientError as e:
    print("Error:", e)
