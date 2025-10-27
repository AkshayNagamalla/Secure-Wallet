import boto3
from config import settings

def generate_presigned_s3_upload_url(file_name: str, expires_in=3600):
    s3_client = boto3.client(
        "s3",
        endpoint_url=settings.S3_ENDPOINT,
        aws_access_key_id=settings.S3_ACCESS_KEY_ID,
        aws_secret_access_key=settings.S3_SECRET_ACCESS_KEY,
        region_name=settings.S3_REGION
    )
    
    url = s3_client.generate_presigned_url(
        "put_object",
        Params={"Bucket": settings.BUCKET_NAME, "Key": file_name},
        ExpiresIn=expires_in
    )
    response = s3_client.list_buckets()
    print(response)

    return url
