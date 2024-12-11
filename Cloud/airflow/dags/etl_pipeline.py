from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello, World from Airflow!")

with DAG('hello_world_dag', start_date=datetime(2023, 1, 1), schedule_interval=None) as dag:
    task = PythonOperator(
        task_id='say_hello',
        python_callable=hello_world
    )
