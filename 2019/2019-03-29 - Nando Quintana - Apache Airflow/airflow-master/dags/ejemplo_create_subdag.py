#!/usr/bin/python3

from airflow import DAG

from airflow.operators.dummy_operator import DummyOperator


def create_dag(parent_dag_name, dag_name, default_args, schedule_interval):
    """ """
    sub_dag = DAG(
        '%s.%s' % (parent_dag_name, dag_name),
        default_args=default_args,
        schedule_interval=schedule_interval)

    start = DummyOperator(
        task_id="start",
        dag=sub_dag)

    nothing = DummyOperator(
        task_id="reported",
        dag=sub_dag)

    end = DummyOperator(
        task_id="end",
        dag=sub_dag)

    start >> nothing >> end

    return sub_dag
