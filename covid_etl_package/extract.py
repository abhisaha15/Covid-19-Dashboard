# extract.py
import requests
import os
from pyspark.sql import SparkSession

def extract_data(spark: SparkSession):
    url = "https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv"
    local_file = "compact_covid_data.csv"
    data_dir = "data"

    os.makedirs(data_dir, exist_ok=True)
    local_path = os.path.join(data_dir, local_file)

    print(f"Downloading {url} to {local_path}...")
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(local_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print("Download complete.")

    df = spark.read.option("header", True).option("inferSchema", True).csv(local_path)
    return df
