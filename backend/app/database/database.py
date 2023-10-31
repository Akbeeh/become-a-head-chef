import calendar
import json
import os
from datetime import date

import boto3
from app.database.scraping import DAY_THEME
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
from dotenv import load_dotenv

# Help from https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html

# Name of the table
TABLE_NAME = "recipes"

load_dotenv()


def _init_dynamodb():
    """Initialize the service resource"""
    dynamodb = boto3.resource(
        service_name="dynamodb",
        region_name="eu-west-3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )
    return dynamodb


def check_table_exists():
    """Check if the table exists

    Raises:
        e: The error

    Returns:
        bool: True if the table exists, False otherwise
    """
    try:
        table = _init_dynamodb().Table(TABLE_NAME)
        table.table_status
        return True
    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            return False
        else:
            raise e


def create_table() -> None:
    """Create the table"""
    table = _init_dynamodb().create_table(
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
    table = _init_dynamodb().Table(TABLE_NAME)
    return table


def save_table() -> None:
    """Save the table locally in JSON format"""
    table = get_table()

    # Scan the table to retrieve all items
    response = table.scan()
    items = response.get("Items", [])

    json_path = "app/database/recipes.json"
    with open(json_path, "w") as json_file:
        json.dump(items, json_file, indent=4)


def delete_table() -> None:
    """Delete the table"""
    table = get_table()
    table.delete()
    table.wait_until_not_exists()


def add_recipe(
    day_theme: str,
    date: str,
    url: str,
    url_image: str,
    info_recipe: dict,
) -> None:
    """Add a recipe to the table

    Args:
        day (str): The day of the theme
        theme (str): The theme of the recipe
        date (str): The date added to the table
        url (str): The url of the recipe
        url_image (str): The url of the image of the recipe
        info_recipe (dict): The information of the recipe
    """
    table = get_table()
    table.put_item(
        Item={
            "day_theme": day_theme,
            "date": date,
            "url": url,
            "url_image": url_image,
            "info_recipe": info_recipe,
        }
    )


def get_recipe(day: str, theme: str, date_str: str) -> dict:
    """Get a recipe from the table

    Args:
        day (str): The day of the theme
        theme (str): The theme of the recipe
        date_str (str): The date added to the table

    Returns:
        dict: The recipe
    """
    table = get_table()
    response = table.get_item(
        Key={
            "day_theme": f"{day}_{theme}",
            "date": date_str,
        }
    )
    return response["Item"]


def get_recipe_by_date(date_str: str) -> dict:
    """Get a recipe from the table by date

    Args:
        date_str (str): The date added to the table

    Returns:
        dict: The recipe
    """
    table = get_table()
    today = calendar.day_name[date.fromisoformat(date_str).weekday()]
    response = table.query(
        KeyConditionExpression=Key("day_theme").eq(
            f"{today}_{DAY_THEME[today].capitalize()}"
        )
        & Key("date").eq(date_str),
    )
    return response["Items"][0]


def delete_recipe(day: str, theme: str, date_str: str) -> None:
    """Delete a recipe from the table

    Args:
        day (str): The day of the theme
        theme (str): The theme of the recipe
        date_str (str): The date added to the table
    """
    table = get_table()
    table.delete_item(
        Key={
            "day_theme": f"{day}_{theme}",
            "date": date_str,
        }
    )
