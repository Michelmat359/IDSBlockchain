FROM apache/airflow:2.7.1
USER root
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
COPY dags /opt/airflow/dags
COPY ../tmops_validation_replication /opt/airflow/tmops_validation_replication
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
USER airflow
