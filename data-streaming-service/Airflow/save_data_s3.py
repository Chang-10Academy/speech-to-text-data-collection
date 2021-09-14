from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

dag = DAG('S3_data_save_dag', description='DAG to save data in S3',
          schedule_interval='0 12 * * *',
          start_date=datetime(2020, 3, 20), catchup=False)

start_task = DummyOperator(task_id='start_task', dag=dag)

commands = "cd /mnt/10ac-batch-4/all-notebooks/smegnsh_yeruk/speech-to-text-data-collection/data-streaming-service/Spark /data_pipeline.py"

save_data = BashOperator(
    task_id='spark-save-task',
    bash_command=commands,
    dag=dag)

start_task >> save_data