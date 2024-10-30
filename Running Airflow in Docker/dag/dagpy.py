from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'asad',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id = 'test_dag_v6',
    default_args = default_args,
    description = 'This is my test dag',
    start_date = datetime(2024, 10, 20, 2),
    schedule_interval = '@daily',
)as dag:
    task1 = BashOperator(
        task_id = 'test_task',
        bash_command = 'echo this is the test task.'
    )
    task2 = BashOperator(
        task_id = 'second_task',
        bash_command = 'echo I am test task 2 and will run after task 1'
    )
    task3 = BashOperator(
        task_id = 'third_task',
        bash_command = 'echo I am test task 3 and will run after task 1 along with task 2'
    )

    # Task dependencies method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # Task dependencies method 2 - Bitshit operators
    # task1 >> task2
    # task1 >> task3

    # Task dependencies method 3
    task1 >> [task2, task3]




