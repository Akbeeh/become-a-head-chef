from datetime import datetime

import app.database.database as db
import app.database.scraping as scraping
from airflow.operators.python import PythonOperator

from airflow import DAG


# Special functions that get recipe + save recipe
def get_save_recipe():
    """Get and save the recipe of the day"""
    recipe = scraping.get_all_info_recipe()
    db.add_recipe(
        recipe["day_theme"],
        recipe["date"],
        recipe["url"],
        recipe["url_image"],
        recipe["info_recipe"],
    )


default_args = {
    "owner": "Become a Head Chef",
    "depends_on_past": False,
    "start_date": datetime.today(),
    "email_on_failure": False,
    "email_on_retry": False,
}

# Create the DAG instance
dag = DAG(
    "recipes_dag",
    default_args=default_args,
    description="Get the recipe of the day",
    schedule="0 0 * * *",  # minutes, hour, day of month, month, day of week
)

# Define the tasks

# Task 1: Get the recipe of the day
task_1 = PythonOperator(
    task_id="get_save_recipe_of_the_day",
    python_callable=get_save_recipe,
    dag=dag,
)

# Task 2: Save locally all the recipes
task_2 = PythonOperator(
    task_id="save_locally_all_recipes",
    python_callable=db.save_table,
    dag=dag,
)

# Define the order of the tasks
task_1 >> task_2
