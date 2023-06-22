# ASI Projekt

## Overview

This is your new Kedro project, which was generated using `Kedro 0.18.3`.

Take a look at the [Kedro documentation](https://kedro.readthedocs.io) to get started.

## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a [data engineering convention](https://kedro.readthedocs.io/en/stable/faq/faq.html#what-is-data-engineering-convention)
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## How to work with DVC

You can download latest version of datasets by running:

```
dvc pull
```

## How to run MLFlow UI

You can run MLFlow UI with:

```
docker compose run mlflow_server
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
docker compose run kedro_pipeline
```
