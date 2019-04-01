#!/usr/bin/python3

from airflow import DAG

from datetime import datetime, timedelta

from airflow.operators.dummy_operator import DummyOperator
from airflow.hooks.postgres_hook import PostgresHook
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
    "ejemplo_sql",
    catchup=False,
    default_args=default_args,
    schedule_interval=SCHEDULE_INTERVAL)

start = DummyOperator(
    task_id="start",
    dag=dag)

def do_anotar(**kwargs):
    asistente = kwargs.get('templates_dict').get('asistente')
    nota = kwargs.get('templates_dict').get('nota')
    query = \
        """
        INSERT INTO asistencia (asistente, nota)
        VALUES ('{}','{}');
        """.format(asistente,nota)

    hook = PostgresHook(postgres_conn_id="extrepython_db")
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

anotar = PythonOperator(
    task_id="anotar",
    provide_context=True,
    python_callable=do_anotar,
    templates_dict={
        'asistente': 'javi',
        'nota': 'puntual'
        },
    trigger_rule="all_done",
    dag=dag)

end = DummyOperator(
    task_id="end",
    dag=dag)

start >> anotar >> end
