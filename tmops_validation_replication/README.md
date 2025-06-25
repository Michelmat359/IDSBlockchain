# Guía de uso

Este directorio contiene un prototipo para replicar la validación del artículo *Implementing Trustworthy Machine Learning Operations in Manufacturing*.

## Instalación

1. Cree un entorno virtual de Python (opcional pero recomendado).
2. Instale las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Archivos principales

- **config.yaml** – Parámetros de pesos, PID y simulación.
- **data_generator.py** – Genera lotes sintéticos de datos.
- **sensitivity.py** – Calcula la sensibilidad combinando aspectos legales, de negocio y privacidad.
- **controller.py** – Implementa un controlador PID para ajustar la precisión del cifrado.
- **he_module.py** – Envoltura simplificada de operaciones de cifrado homomórfico.
- **blockchain_logger.py** – Guarda eventos en `ledger.csv` simulando un blockchain.
- **ids_connector.py** – Valida que la configuración cumpla la política mínima (bits >= 128).
- **ml_pipeline.py** – Pipelines de LSTM, ResNet‑18 y XGBoost para datos cifrados.
- **evaluate_metrics.py** – Cálculo de throughput y latencia.
- **run_experiments.py** – Script principal para ejecutar la simulación.

## Cómo ejecutar el experimento

1. Revise `config.yaml` y ajuste los parámetros si es necesario.
2. Desde este directorio, lance:
   ```bash
   python run_experiments.py
   ```
3. El experimento dura 60 minutos por defecto y genera varios ficheros:
   - `ledger.csv`: registro de eventos.
   - `results.csv`: métricas por paso.
   - `plot_sensitivity_bits.png`, `plot_latency_bits.png`, `plot_accuracy_bits.png`: gráficos de análisis.

Puede detener la ejecución antes de tiempo con `Ctrl+C`; los resultados hasta ese momento quedarán guardados.

