from airflow import DAG
from airflow.providers.docker.operators.docker  import DockerOperator
from airflow.operators.docker_operator import DockerOperator
import pendulum

with DAG(
    tags=['data registry'],
    dag_id='Data_Pull',
    start_date=pendulum.datetime(2022,9,1,tz='UTC'),
    schedule_interval='@daily'
) as dag:

    stage1 = DockerOperator(
        task_id = 'stage1',
        image='data_registry_stage1',
        command=["python", "smt.py"],
        network_mode='bridge',
        api_version='auto',
        auto_remove=True,
        docker_url="unix://var/run/docker.sock",
    )
    
    stage2 = DockerOperator(
        task_id = 'stage2',
        image='data_registry_stage2',
        command=["python", "smt.py"],
        network_mode='bridge',
        api_version='auto',
        auto_remove=True,
        docker_url="unix://var/run/docker.sock",
    )

    stage3 = DockerOperator(
        task_id = 'stage3',
        image='data_registry_stage3',
        command=["python", "smt.py"],
        network_mode='bridge',
        api_version='auto',
        auto_remove=True,
        docker_url="unix://var/run/docker.sock",
    )
    
    stage1 >> stage2 >> stage3

