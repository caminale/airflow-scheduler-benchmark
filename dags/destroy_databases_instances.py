import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2018, 10, 30),
    'concurrency': 1,
    'retries': 0
}

with DAG('destroy_databases',
         catchup=False,
         default_args=default_args,
         #schedule_interval=timedelta(1),
         schedule_interval=None,
         ) as dag:
    opr_destroy_terraform = BashOperator(task_id='destroy_terraform',
                                      bash_command='cd /opt/deployment-databases/terraform && terraform destroy -auto-approve')

opr_destroy_terraform
