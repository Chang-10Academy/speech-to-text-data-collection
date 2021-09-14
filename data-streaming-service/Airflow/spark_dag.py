from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

dag = DAG('spark_job_dag', description='DAG to trigger pySpark job',
          schedule_interval='0 12 * * *',
          start_date=datetime(2020, 3, 20), catchup=False)

start_task = DummyOperator(task_id='start_task', dag=dag)

commands = """
    cd /mnt/10ac-batch-4/all-notebooks/smegnsh_yeruk/speech-to-text-data-collection/data-streaming-service/Spark fetch_data.py;
    """

fetch_data = BashOperator(
    task_id='spark-task',
    bash_command=commands,
    dag=dag)

start_task >> fetch_data