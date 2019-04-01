#!/usr/bin/python3

from airflow import DAG

from datetime import datetime, timedelta

from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


SCHEDULE_INTERVAL = timedelta(hours=1)

default_args = {
    "owner": "ExtrePython",
    "depends_on_past": False,
    "start_date": datetime(2019, 3, 29),
    "email": ["my@email.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=10)}

dag = DAG(
    "hola_mundo_3",
    catchup=False,
    default_args=default_args,
    schedule_interval=SCHEDULE_INTERVAL)

start = DummyOperator(
    task_id="start",
    dag=dag)

def saludar(**kwargs):
    saludo = kwargs.get('templates_dict').get('saludo')
    print(saludo)
    return saludo

hola_mundo = PythonOperator(
    task_id="hola_mundo",
    provide_context=True,
    python_callable=saludar,
    templates_dict={'saludo': "hola mundo 👋, ahora es {{ execution_date }}" },
    trigger_rule="all_done",
    dag=dag)

end = DummyOperator(
    task_id="end",
    dag=dag)

start >> hola_mundo >> end
