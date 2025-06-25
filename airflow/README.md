# Airflow Setup

Este directorio proporciona una configuraci\u00f3n b\u00e1sica para ejecutar las pruebas con Apache Airflow.

## Uso r\u00e1pido

1. Construye e inicia Airflow con MLflow desde la ra\u00edz del proyecto:
    ```bash
    docker compose up --build
    ```
2. Accede a la interfaz web en [http://localhost:8080](http://localhost:8080) con usuario `admin` y contrase\u00f1a `admin`.
3. Ejecuta manualmente el DAG **tmops_experiment** para lanzar el experimento.

Los resultados se guardan en el volumen compartido `results.csv`, `ledger.csv` y las gr\u00e1ficas correspondientes.

