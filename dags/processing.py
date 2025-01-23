from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.bash import BashOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime

with DAG(
    dag_id="data_processing",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    default_args={
        "owner": "Caspar Health DE team"
    },
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
        conn_id="sparkon", #The connections needs to be created on UI
        verbose=True,
        dag=dag,
    )

    dbt_processing = BashOperator(
        task_id="dbt_processing",
        bash_command="cd /opt/airflow/processing && dbt run",
        trigger_rule=TriggerRule.ALL_DONE #To avoid failing the main pipeline when any of upstreams failed
    )

    dbt_tests = BashOperator(
        task_id="dbt_processing_tests",
        bash_command="cd /opt/airflow/processing && dbt test",
    )

    [steps_import, patients_import, exercises_import] >> dbt_processing >> dbt_tests
