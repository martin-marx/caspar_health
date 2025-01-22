import argparse
from schema.schema_enum import SchemaEnum
from pyspark.sql import SparkSession

if __name__ == '__main__':

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-s', '--source', type=str, help='Source of the data', required=True)

    source_arg = parser.parse_args().source

    spark_schema = SchemaEnum.get_schema(source_arg)
    file_path = SchemaEnum.get_file_path(source_arg)

    spark = (SparkSession.builder
             .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")
             #.config("spark.jars", "./jars/hadoop-aws-3.3.4.jar,./jars/aws-java-sdk-bundle-1.12.779.jar, ./jars/postgresql-42.7.0.jar")
             .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000")
             .config("spark.hadoop.fs.s3a.access.key", "datauser")
             .config("spark.hadoop.fs.s3a.secret.key", "password")
             .config("spark.hadoop.fs.s3a.path.style.access", "true")
             .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
             .appName('Data importer').getOrCreate())

    df = spark.read.options(header='True', delimiter=',').schema(spark_schema).csv(f's3a://source/{file_path}')
    print(df)

    (df
     .write.format("jdbc")
     .option("url", "jdbc:postgresql://dwh4:5432/main")
     .option("driver", "org.postgresql.Driver")
     .option("dbtable", source_arg)
     .option("user", "datauser")
     .option("password", "password")
     .mode("append")
     .save())
