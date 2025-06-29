# load.py
from pyspark.sql import DataFrame

def load_data(df: DataFrame):
    db_url = "jdbc:postgresql://aws-0-us-east-1.pooler.supabase.com:6543/postgres"
    db_properties = {
        "user": "postgres.ajphevofkloxpdtocooj",
        "password": "fNhC4qLRBdTI3z8k",
        "driver": "org.postgresql.Driver",
        "sslmode": "require"
    }

    df.write.jdbc(url=db_url, table="covid_data", mode="overwrite", properties=db_properties)
    print("Data written to PostgreSQL.")
