import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://admin:admin@db:5432/ids"
engine = create_engine(DATABASE_URL)

def process_data():
    # Example: Load data from a CSV and insert into the database
    data = pd.read_csv("example_data.csv")
    data.to_sql("example_table", engine, if_exists="replace", index=False)

if __name__ == "__main__":
    process_data()
