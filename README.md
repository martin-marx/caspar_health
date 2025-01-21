## Prepare ENV:

### Set up `docker compose`

#### Install `docker compose`
sudo apt-get update  
sudo apt-get install docker-compose-plugin

#### Update `docker compose`
sudo apt-get update
sudo apt-get install docker-compose-plugin

####  Check if `docker compose` is installed
docker compose version

### Set up Airflow

#### Set up local envs 
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env

#### Init the DBs
docker compose up airflow-init

#### Run Airflow
docker compose up

### Set up MinIO



## Use ENV:

### Airflow Creds
user: airflow  
pass: airflow

