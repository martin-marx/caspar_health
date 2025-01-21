from pyspark.sql.types import StructType, StructField, IntegerType, StringType, TimestampType

patients_schema = StructType([
    StructField("patient_id", IntegerType(), False),
    StructField("first_name", StringType(), True),
    StructField("last_name", StringType(), True),
    StructField("country", StringType(), True)
])

exercises_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("external_id", IntegerType(), True),
    StructField("minutes", IntegerType(), True),
    StructField("completed_at", TimestampType(), True),
    StructField("updated_at", TimestampType(), True)
])


steps_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("external_id", IntegerType(), True),
    StructField("steps", IntegerType(), True),
    StructField("submission_time", TimestampType(), True),
    StructField("updated_at", TimestampType(), True)
])


