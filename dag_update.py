from asyncio import tasks
import datetime

from airflow.models import DAG
from airflow.operators.bash import BashOperator

dag = DAG(
    dag_id="dag_puller",
    default_args={"depends_on_past":False},
    start_date=datetime.datetime(2022,1,1),
    schedule_interval="*/5 * * * *",
    catchup=False,
    )

fetch_code = BashOperator(
    task_id="fetch_code",
    bash_command=(
        "apt-get update && "
        "apt-get install -y git && "
        "git config --global user.name 'TestAirflowUser' && "
        "git config --global user.email 'Bloodjanp@gmail.com' && "
        "cd /opt/airflow/dags && "
        "git pull origin master &&"
        #"git init && "
        #"git remote add origin https://github.com/DataMathematician/airflow_dags.git && "
        "git reset --hard origin/master "
    ),
    dag=dag
)