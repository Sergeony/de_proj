""" A module with a similar DAG to load_movies_from_range_dag,
but sets range to the last day.
"""
from datetime import date, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from jobs.load_movies_from_range import get_movies_from_range
from jobs.common import default_args


with DAG(dag_id="load_latest_movies_dag",
         default_args=default_args,
         schedule_interval="*/10 * * * *",
         catchup=False) as dag:

    task_1 = PythonOperator(
        task_id="load_latest_movies",
        python_callable=get_movies_from_range,
        op_kwargs={"min_date": str(date.today() - timedelta(days=1)),
                   "max_date": str(date.today())})
