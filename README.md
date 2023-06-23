# ASI Projekt

## Quickstart

First place gcp SA .json credentials file in project root, then
to install project locally, run this command:

```
./init.sh
```

This script will build docker images and pull datasets for you.

## Run the pipeline

```
docker-compose run kedro_pipeline kedro run
```

## Run MLFlow UI and deps
MLFlow UI will be available at http://127.0.0.1:8888
Prometheus UI will be available at http://127.0.0.1:9090
```
docker-compose up
```

## Development

Development environment is fully encased in docker container. 
To attatch a shell to the container run:

```
docker compose run kedro_pipeline bash
```

## How to start mlflow ui

```
kedro mlflow ui
```


## How to run your Kedro pipeline
=======
## Dataset changes


After changing the datasets it's important to use DVC to store the new version:

```
dvc add <target>
dvc push
```
to download newest dataset version run:
```
dvc pull or ./init.sh
```
