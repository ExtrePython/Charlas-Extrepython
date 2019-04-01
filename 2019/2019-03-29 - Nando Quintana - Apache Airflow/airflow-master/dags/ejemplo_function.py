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
    "ejemplo_function",
    catchup=False,
    default_args=default_args,
    schedule_interval=SCHEDULE_INTERVAL)

start = DummyOperator(
    task_id="start",
    dag=dag)

def saludar_task(task_id, saludo, dag):
    """ """
    def saludar(**kwargs):
        saludo = kwargs.get('templates_dict').get('saludo')
        print(saludo)
        return saludo

    operator = PythonOperator(
        task_id=task_id,
        provide_context=True,
        python_callable=saludar,
        templates_dict={'saludo': saludo },
        trigger_rule="all_done",
        dag=dag)

    return operator

saludo_1 = saludar_task(
    task_id="saludo_1",
    saludo="hola 1 👋",
    dag=dag)

saludo_2 = saludar_task(
    task_id="saludo_2",
    saludo="hola 2 👋",
    dag=dag)

saludo_3 = saludar_task(
    task_id="saludo_3",
    saludo="hola 3 👋",
    dag=dag)

end = DummyOperator(
    task_id="end",
    dag=dag)

start >> saludo_1 >> saludo_2 >> saludo_3 >> end
