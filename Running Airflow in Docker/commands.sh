mkdir airfflow_docker
cd airflow_docker

docker --version
docker-compose --version

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml'
mkdir -p ./dags ./logs ./plugins ./config

docker compose up airflow-init

docker compose up -d

# Navigate te http://localhost:8080
