# main_etl.py
from pyspark.sql import SparkSession
from extract import extract_data
from transform import transform_data
from load import load_data

# Setup Spark with PostgreSQL JAR
spark = SparkSession.builder \
    .appName("COVID ETL Pipeline") \
    .config("spark.jars", "postgresql-42.6.0.jar") \
    .getOrCreate()

# Run ETL
df_raw = extract_data(spark)
df_transformed = transform_data(df_raw)
load_data(df_transformed)

# Done
spark.stop()
