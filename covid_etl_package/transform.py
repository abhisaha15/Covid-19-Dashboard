# transform.py
from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def transform_data(df: DataFrame) -> DataFrame:
    # Example: Filter non-null total_cases and recent dates
    return df.select(
        "country", "continent", "date", "total_cases", "new_cases", "total_deaths",
        "new_deaths", "total_vaccinations", "people_vaccinated", "people_fully_vaccinated",
        "positive_rate", "population", "gdp_per_capita"
    ).where(col("date").isNotNull())
