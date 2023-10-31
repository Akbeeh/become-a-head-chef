from datetime import datetime

import app.database.database as db
import app.database.scraping as scraping
from airflow import DAG
from airflow.operators.python import PythonOperator

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
    timezone="UTC",
)

# Define the tasks

# Task 1: Get the recipe of the day
task_1 = PythonOperator(
    task_id="get_recipe_of_the_day",
    python_callable=scraping.get_all_info_recipe,
    dag=dag,
    do_xcom_push=True,
)

# Task 2: Save the recipe of the day
task_2 = PythonOperator(
    task_id="save_recipe_of_the_day",
    python_callable=db.add_recipe,
    op_kwargs={
        "day_theme": task_1.output["day_theme"],
        "date": task_1.output["date"],
        "url": task_1.output["url"],
        "url_image": task_1.output["url_image"],
        "info_recipe": task_1.output["info_recipe"],
    },
    dag=dag,
)

# Task 3: Save locally all the recipes
task_3 = PythonOperator(
    task_id="save_locally_all_recipes",
    python_callable=db.save_table,
    dag=dag,
)

# Define the order of the tasks
task_1 >> task_2 >> task_3
