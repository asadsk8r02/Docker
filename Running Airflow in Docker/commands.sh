# Create directory and navigate
mkdir airfflow_docker
cd airflow_docker

# Chekc docker version
docker --version
docker-compose --version

# Donwload docker-compose.yml file and create directories for the airflow.
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml'
mkdir -p ./dags ./logs ./plugins ./config

# Initialize the database
docker compose up airflow-init

# Docker compose
docker compose up -d

# Navigate te http://localhost:8080



# Connect airflow to postgres - Run this in terminal and connect in dbeaver
docker-compose up -d --no-deps --build postgres
