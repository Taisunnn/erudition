"""
# Users Pipeline
This pipeline will load users data into the database.

"""

# Built-in packages
from datetime import datetime, timedelta

# Pip packages
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

# Custom function
from utilities import pipeline


default_args = {
    "owner": "Tyson",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    "users_dag",
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 3, 8),
    catchup=False,
    tags=["users"],
) as dag:

    print_date = BashOperator(task_id="print_date", bash_command='echo "{{ ds }}"')

    load_users = PythonOperator(
        task_id="load_users",
        python_callable=pipeline,
        op_kwargs={
            "file": "/Users/tyson/new_projects/assignment/sample_data/users.csv"
        },
    )

print_date >> load_users
