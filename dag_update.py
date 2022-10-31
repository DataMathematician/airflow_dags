from asyncio import tasks
import datetime

from airflow.models import DAG
from airflow.operators.bash import BashOperator

dag = DAG(
    dag_id="dag_puller",
    default_args={"depends_on_past":False},
    start_date="*/5 2 * * *",
    schedule_interval=datetime.datetime(minutes=5),
    catchup=False,
    )

fetch_code = BashOperator(
    task_id="fetch_code",
    bash_command=(
        "cd /airflow/dags &&"
        "git reset --hard origin/master"
    ),
    dag=dag
)