from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    "owner": "asad",
    "retries": 2,
    "retry_delay": timedelta(minutes=2)
}

@dag(dag_id="dag_with_taskflowapi_v2", 
     default_args = default_args,
     description = "Test dag with taskflow api", 
     start_date = datetime(2024, 10, 20, 2), 
     schedule_interval = "@daily")
def hello_world_etl():
    @task(multiple_outputs=True)
    def get_name():
        return {
            "first_name": "Asadullah",
            "last_name": "Khan"
        }
    
    @task()
    def get_age():
        return 25
    
    @task()
    def greet(first_name, last_name, age):
        print(f"Hello this is the greet task. My name is {first_name} {last_name} and my age is {age}")

    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict["first_name"], 
          last_name= name_dict["last_name"], 
          age=age)

greet_dag = hello_world_etl()