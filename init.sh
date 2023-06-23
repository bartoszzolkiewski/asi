#!/bin/bash

export GDRIVE_CREDENTIALS_DATA=$(cat asi-projekt-14079a35e353.json)

if ! grep -q gdrive_service_account_json_file_path ".dvc/config"; then
  echo '    gdrive_service_account_json_file_path='$(pwd)'/asi-projekt-14079a35e353.json' >> .dvc/config
fi

dvc pull data/01_raw/application_data.csv 
dvc pull data/01_raw/columns_description.csv 
dvc pull data/01_raw/previous_application.csv

docker-compose build