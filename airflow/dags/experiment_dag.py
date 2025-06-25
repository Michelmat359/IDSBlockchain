from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

from tmops_validation_replication import run_experiments


def run():
    run_experiments.main()


default_args = {
    "owner": "airflow",
}

with DAG(
    dag_id="tmops_experiment",
    default_args=default_args,
    schedule_interval=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:
    run_task = PythonOperator(
        task_id="run_experiment",
        python_callable=run,
    )




