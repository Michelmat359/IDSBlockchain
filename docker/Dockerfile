FROM python:3.10-slim
WORKDIR /app
COPY tmops_validation_replication/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
COPY tmops_validation_replication /app/tmops_validation_replication
CMD ["python", "tmops_validation_replication/run_experiments.py"]
