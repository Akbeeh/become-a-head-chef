import boto3
from botocore.exceptions import ClientError

# Help from https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html

# Name of the table
TABLE_NAME = "recipes"

# Get the service resource
dynamodb = boto3.resource("dynamodb")


# Check if the table exists
def check_table_exists():
    try:
        table = dynamodb.Table(TABLE_NAME)
        table.table_status
        return True
    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            return False
        else:
            raise e
