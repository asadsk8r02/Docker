from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "asad",
    "retries": 2,
    "retry_delay": timedelta(minutes=2)
}

with DAG(
    default_args = default_args,
    dag_id = "dag_with_cron_expression_v3",
    description = "DAG with cron expression",
    start_date = datetime(2024, 10, 20, 2),
    schedule_interval = "0 * * * *", # use this website https://crontab.guru/
    # catchup=True, # True is default so its okay not to write this.
) as dag:
    task1 = BashOperator(
        task_id = "task1",
        bash_command = "echo This is the test task 1 with cron expression."
    )

    task1