# Docker Setup

Este directorio permite ejecutar el experimento completo en un contenedor.

## Uso rapido

1. Desde la raiz del repositorio ejecute:
   ```bash
   docker compose -f docker/docker-compose.yml up --build
   ```
2. Al finalizar encontrara `results.csv` y `ledger.csv` en la carpeta `results/`.

El contenedor utiliza el script `tmops_validation_replication/run_experiments.py` y almacena los resultados fuera del contenedor para su consulta.
