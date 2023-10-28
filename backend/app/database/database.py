import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

# Help from https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html

# Name of the table
TABLE_NAME = "recipes"


def init_dynamodb():
    """Initialize the service resource"""
    dynamodb = boto3.resource("dynamodb")
    return dynamodb


def check_table_exists():
    """Check if the table exists

    Raises:
        e: The error

    Returns:
        bool: True if the table exists, False otherwise
    """
    try:
        table = init_dynamodb().Table(TABLE_NAME)
        table.table_status
        return True
    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            return False
        else:
            raise e


def create_table() -> None:
    """Create the table"""
    table = init_dynamodb().create_table(
        TableName=TABLE_NAME,
        KeySchema=[
            {
                "AttributeName": "day_theme",
                "KeyType": "HASH",
            },
            {
                "AttributeName": "date",
                "KeyType": "RANGE",
            },
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "day_theme",
                "AttributeType": "S",
            },
            {
                "AttributeName": "date",
                "AttributeType": "S",
            },
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 10,
            "WriteCapacityUnits": 10,
        },
    )
    table.wait_until_exists()


def get_table():
    """Get the table"""
    table = init_dynamodb().Table(TABLE_NAME)
    return table


def delete_table() -> None:
    """Delete the table"""
    table = get_table()
    table.delete()
    table.wait_until_not_exists()


def add_recipe(
    day: str,
    theme: str,
    date: str,
    url: str,
    info_recipe: dict,
) -> None:
    """Add a recipe to the table

    Args:
        day (str): The day of the theme
        theme (str): The theme of the recipe
        date (str): The date added to the table
        url (str): The url of the recipe
        info_recipe (dict): The information of the recipe
    """
    table = get_table()
    table.put_item(
        Item={
            "day_theme": f"{day}_{theme}",
            "date": date,
            "url": url,
            "info_recipe": info_recipe,
        }
    )


def get_recipe(day: str, theme: str, date: str) -> dict:
    """Get a recipe from the table

    Args:
        day (str): The day of the theme
        theme (str): The theme of the recipe
        date (str): The date added to the table

    Returns:
        dict: The recipe
    """
    table = get_table()
    response = table.get_item(
        Key={
            "day_theme": f"{day}_{theme}",
            "date": date,
        }
    )
    return response["Item"]


def get_recipe_by_date(date: str) -> dict:
    """Get a recipe from the table by date

    Args:
        date (str): The date added to the table

    Returns:
        dict: The recipe
    """
    table = get_table()
    response = table.query(
        KeyConditionExpression=Key("date").eq(date),
    )
    return response["Items"][0]


def delete_recipe(day: str, theme: str, date: str) -> None:
    """Delete a recipe from the table

    Args:
        day (str): The day of the theme
        theme (str): The theme of the recipe
        date (str): The date added to the table
    """
    table = get_table()
    table.delete_item(
        Key={
            "day_theme": f"{day}_{theme}",
            "date": date,
        }
    )
