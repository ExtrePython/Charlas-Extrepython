#!/usr/bin/python3

from airflow import DAG

from datetime import datetime, timedelta

from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.subdag_operator import SubDagOperator

from ejemplo_create_subdag import create_dag

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
    "ejemplo_subdag",
    catchup=False,
    default_args=default_args,
    schedule_interval=SCHEDULE_INTERVAL)

subdag1 = SubDagOperator(
    subdag = create_dag(
        "ejemplo_subdag",
        "subdag1",
        default_args,
        SCHEDULE_INTERVAL),
    task_id='subdag1',
    dag=dag)

subdag2 = SubDagOperator(
    subdag = create_dag(
        "ejemplo_subdag",
        "subdag2",
        default_args,
        SCHEDULE_INTERVAL),
    task_id='subdag2',
    dag=dag)

subdag3 = SubDagOperator(
    subdag = create_dag(
        "ejemplo_subdag",
        "subdag3",
        default_args,
        SCHEDULE_INTERVAL),
    task_id='subdag3',
    dag=dag)

subdag1 >> subdag2 >> subdag3
