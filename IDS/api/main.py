from fastapi import FastAPI
from sqlalchemy import create_engine

app = FastAPI()
DATABASE_URL = "postgresql://admin:admin@db:5432/ids"
engine = create_engine(DATABASE_URL)

@app.get("/")
def read_root():
    return {"message": "Welcome to the International Data System!"}

@app.get("/data")
def get_data():
    with engine.connect() as connection:
        result = connection.execute("SELECT * FROM example_table")
        return {"data": [dict(row) for row in result]}