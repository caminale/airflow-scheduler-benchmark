import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'k8s',
    'start_date': dt.datetime(2018, 12, 22),
    'concurrency': 1,
    'retries': 0
}

with DAG('create_k8s',
         catchup=False,
         default_args=default_args,
         #schedule_interval=timedelta(1),
         schedule_interval=None,
         ) as dag:

    opr_init_terraform = BashOperator(task_id='init_terraform',
                                      bash_command='cd /opt/gcp-kubernetes-scala-api/k8s-cluster terraform init')

    opr_plan_terraform = BashOperator(task_id='plan_terraform',
                                      bash_command='cd /opt/gcp-kubernetes-scala-api/k8s-cluster && terraform plan -out=terraform.tfplan -input=false')

    opr_sleep = BashOperator(task_id='sleep_me',
                             bash_command='sleep 5')

    opr_apply_terraform =  BashOperator(task_id='apply_terraform',
                                        bash_command='cd /opt/gcp-kubernetes-scala-api/k8s-cluster && terraform apply terraform.tfplan')

opr_init_terraform >> opr_plan_terraform >> opr_sleep >> opr_apply_terraform
