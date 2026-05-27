import boto3
from botocore.exceptions import ClientError

# Create S3 client
s3 = boto3.client("s3")

bucket_name = "akankshaganta"
region = "ap-south-3"   # Mumbai region

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
