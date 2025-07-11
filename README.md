# tmops_validation_replication

This project provides a lightweight prototype to replicate the experimental validation from the IEEE ACCESS article *"Implementing Trustworthy Machine Learning Operations in Manufacturing"*.

## Requirements

- Python 3.10 or later
- Recommended: create a virtual environment
- Install dependencies:

```bash
pip install -r tmops_validation_replication/requirements.txt
```

## Configuration

All runtime parameters are defined in `tmops_validation_replication/config.yaml`. The main values are:

- `weights`: coefficients for sensitivity calculation
- `pid`: PID controller constants
- `he`: minimum and maximum homomorphic encryption bit lengths
- `simulation`: duration and step size for the experiment run

## Running the experiments

Execute the driver script from the repository root:

```bash
python tmops_validation_replication/run_experiments.py
```

The script generates synthetic data batches, adjusts encryption precision with a PID controller and logs each decision to `ledger.csv`. After completion a `results.csv` file contains per-step statistics and three plots summarising the behaviour of the system. Average latency and bit length are printed to the console.


## Docker usage

An optional Docker setup is available in the `docker` directory. Run:
```bash
docker compose -f docker/docker-compose.yml up --build
```
Results will appear in `results/` after completion.

## Airflow usage

A minimal Airflow environment is provided in the `airflow` directory. Start it with:
```bash
docker compose -f airflow/docker-compose.yml up --build
```
Then open http://localhost:8080 with username `admin` and password `admin` to trigger the **tmops_experiment** DAG.


## Output files

- `ledger.csv`: simulated blockchain log of policy checks
- `results.csv`: latency and bit-length metrics for each time step
- `plot_sensitivity_bits.png`: adaptation of encryption to data sensitivity
- `plot_latency_bits.png`: efficiency-security trade-off
- `plot_accuracy_bits.png`: model accuracy versus encryption precision


## Data folder

A `data/` directory can be added inside `tmops_validation_replication` to store real datasets if desired. The current scripts use only synthetic data for demonstration purposes.

