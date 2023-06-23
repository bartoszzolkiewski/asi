# ASI Projekt

## Prerequisites

You have to have pyenv installed and created a virtualenv.
Then install requirements:

```
pip install -r src/requirements.txt
```

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
MLFlow UI will be available at http://127.0.0.1:8888/
Prometheus UI will be available at http://127.0.0.1:9090/
cAdvisor UI will be available at http://127.0.0.1:8080/
```
docker-compose run -d
```

## How to work with DVC

You can download latest version of datasets by running:

```
dvc pull
```

To send changes in datasets:

```
dvc add <target>
dvc push
git add .
git commit -m "<message>"
git push
```
