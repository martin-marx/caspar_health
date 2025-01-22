from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_args = {
    "owner": "Caspar Health DE team",
    "depends_on_past": False,
    "retries": 0,
}

with DAG(
    dag_id="data_processing",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    steps_import = SparkSubmitOperator(
        task_id="steps_import",
        application="/usr/local/airflow/include/runner.py",
        application_args=["-s", "steps"],
        jars='/usr/local/airflow/include/jars/hadoop-aws-3.3.4.jar,/usr/local/airflow/include/jars/aws-java-sdk-bundle-1.12.779.jar,/usr/local/airflow/include/jars/postgresql-42.7.0.jar',
        name="steps_import_job",
        conn_id="sparkon",
        verbose=True,
        dag=dag,
    )

    patients_import = SparkSubmitOperator(
        task_id="patients_import",
        application="/usr/local/airflow/include/runner.py",
        application_args=["-s", "patients"],
        jars='/usr/local/airflow/include/jars/hadoop-aws-3.3.4.jar,/usr/local/airflow/include/jars/aws-java-sdk-bundle-1.12.779.jar,/usr/local/airflow/include/jars/postgresql-42.7.0.jar',
        name="patients_import_job",
        conn_id="sparkon",
        verbose=True,
        dag=dag,
    )

    exercises_import = SparkSubmitOperator(
        task_id="exercises_import",
        application="/usr/local/airflow/include/runner.py",
        application_args=["-s", "exercises"],
        jars='/usr/local/airflow/include/jars/hadoop-aws-3.3.4.jar,/usr/local/airflow/include/jars/aws-java-sdk-bundle-1.12.779.jar,/usr/local/airflow/include/jars/postgresql-42.7.0.jar',
        name="exercises_import_job",
        conn_id="sparkon",
        verbose=True,
        dag=dag,
    )

    end = DummyOperator(task_id='end')

    [steps_import, patients_import, exercises_import] >> end
