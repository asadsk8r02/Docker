from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'asad',
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

def greet(age, ti):
    first_name = ti.xcom_pull(task_ids ="py_getname", key="first_name")
    last_name = ti.xcom_pull(task_ids ="py_getname", key="last_name")
    age = ti.xcom_pull(task_ids = "py_getage", key="age")
    print(f"hello this is the greet task. My name is {first_name} {last_name} and my age is {age}")

def addition(a,b):
    print('Sum of {} and {} is: {}'.format(a, b, a + b))

def get_name(ti):
    ti.xcom_push(key="first_name", value="Asadullah")
    ti.xcom_push(key="last_name", value="Khan")

def get_age(ti):
    ti.xcom_push(key="age", value=25)

with DAG(
    default_args = default_args,
    dag_id = "test_dag_with_py_v11",
    description = 'This is a test dag with python operator',
    start_date = datetime(2024, 10, 20, 2),
    schedule_interval = '@daily'
) as dag:
    task1 = PythonOperator(
        task_id = "py_greet",
        python_callable = greet,
        # op_kwargs = {"name" : "Asad", "age": "25"}
        op_kwargs = {"age": "25"}
    )
    # task2 = PythonOperator(
    #     task_id = 'py_sum',
    #     python_callable = addition,
    #     op_args = [3, 5]
    #     # op_kwargs={'a': 3, 'b': 5}
    # )
    task3 = PythonOperator(
        task_id = 'py_getname',
        python_callable = get_name
    )
    task4 = PythonOperator(
        task_id = "py_getage",
        python_callable = get_age
    )

    [task3, task4] >> task1