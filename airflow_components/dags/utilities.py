import pandas as pd
from sqlalchemy import create_engine
from airflow.hooks.base import BaseHook


def extract_users(file: str) -> pd.DataFrame:

    print(f"Reading file: {file}...")
    users = pd.read_csv(file)
    print(f"Number of records read: {len(users)}")

    return users


def load_users_to_mysql(users: pd.DataFrame) -> None:

    AIRFLOW_CONN_ID = "first_db"
    TABLE = "users"

    print("Connecting to database...")
    # conn = BaseHook.get_connection(AIRFLOW_CONN_ID)
    # engine = create_engine(f"mysql+pymysql://{conn.login}:{conn.password}@{conn.host}:{conn.port}/first_db")
    engine = create_engine(f"mysql+pymysql://tyson:tyson@localhost:3306/first_db")
    print("Connected to the database!")

    print("Loading users to database...")
    users.to_sql(
        name=TABLE,
        con=engine,
        if_exists="append",
        index=False,
    )
    print("Finished loading users to database!")


def pipeline(file: str):

    users = extract_users(file)
    _ = load_users_to_mysql(users)
