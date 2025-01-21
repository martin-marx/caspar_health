from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def print_hello():
    print("Hello, Airflow!")

# Определяем DAG
with DAG(
    dag_id="simple_dag",
    description="A simple Airflow DAG",
    schedule_interval="@daily",  # Запускать ежедневно
    start_date=datetime(2025, 1, 1),  # Указать начальную дату
    catchup=False,  # Отключить выполнение пропущенных запусков
) as dag:

    # Определяем задачу
    hello_task = PythonOperator(
        task_id="print_hello",
        python_callable=print_hello,
    )

# Установить порядок задач, если их больше одной
# hello_task >> another_task
