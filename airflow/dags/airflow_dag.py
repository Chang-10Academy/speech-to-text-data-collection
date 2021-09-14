from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator


from random import randint
from datetime import datetime

def consume_data():
    return "data consumed from kafka"

def preprocess_data_with_pyspark():
    consumer_return = ti.xcom_pull(task_ids=[
        'run_consumer'
    ])
    print(consumer_return)
    return 'data preprocessed with pyspark'


with DAG("my_dag", start_date=datetime(2021, 1, 1),
    schedule_interval="@hourly", catchup=False) as dag:

        consume = PythonOperator(
            task_id="run_consumer",
            python_callable=consume_data
        )

        preprocess = PythonOperator(
            task_id="preprocess_data",
            python_callable=preprocess_data_with_pyspark
        )

        consume >> preprocess
