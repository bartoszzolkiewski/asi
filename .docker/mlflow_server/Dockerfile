FROM python:3.10-bullseye

WORKDIR /mlflow/
RUN mkdir store mlflow-artifacts

COPY requirements.txt .
RUN cat requirements.txt
RUN pwd
RUN ls
RUN pip install --no-cache-dir -r requirements.txt && \
  rm requirements.txt

EXPOSE 5000



ENV BACKEND_URI /mlflow/store
ENV ARTIFACT_ROOT /mlflow/mlflow-artifacts

CMD mlflow server --backend-store-uri ${BACKEND_URI} --default-artifact-root ${ARTIFACT_ROOT} --host 0.0.0.0 --port 5000 --serve-artifacts