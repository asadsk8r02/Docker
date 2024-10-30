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
    dag_id = "dag_with_catchup_backfills_v4",
    description = "DAG with catch and backfills",
    start_date = datetime(2024, 10, 20, 2),
    schedule_interval = "@daily",
    catchup=False,
) as dag:
    task1 = BashOperator(
        task_id = "task1",
        bash_command = "echo This is the test task 1."
    )

    task1