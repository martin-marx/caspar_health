import argparse
from schema.schema_enum import SchemaEnum
from pyspark.sql import SparkSession

def parse_args():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-s', '--source', type=str, help='Source of the data', required=True)
    parser.add_argument('-sh', '--source_host', type=str, help='Source host', default="http://minio:9000")
    parser.add_argument('-sih', '--sink_host', type=str, help='Sink host', default="dwh4")
    parser.add_argument('-sip', '--sink_port', type=int, help='Sink port', default=5432)
    parser.add_argument('-sid', '--sink_db', type=str, help='Sink DB', default="main")

    return parser.parse_args()

if __name__ == '__main__':

    parsed_args = parse_args()

    spark_schema = SchemaEnum.get_schema(parsed_args.source)
    file_path = SchemaEnum.get_file_path(parsed_args.source)

    spark = (SparkSession.builder
             .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")
             # Next line can be used during local runs
             #.config("spark.jars", "./jars/hadoop-aws-3.3.4.jar,./jars/aws-java-sdk-bundle-1.12.779.jar, ./jars/postgresql-42.7.0.jar")
             .config("spark.hadoop.fs.s3a.endpoint", parsed_args.source_host)
             .config("spark.hadoop.fs.s3a.access.key", "datauser")
             .config("spark.hadoop.fs.s3a.secret.key", "password")
             .config("spark.hadoop.fs.s3a.path.style.access", "true")
             .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
             .appName('Data importer').getOrCreate())

    df = spark.read.options(header='True', delimiter=',').schema(spark_schema).csv(f's3a://source/{file_path}')

    (df
     .write.format("jdbc")
     .option("url", f"jdbc:postgresql://{parsed_args.sink_host}:{parsed_args.sink_port}/{parsed_args.sink_db}")
     .option("driver", "org.postgresql.Driver")
     .option("dbtable", parsed_args.source)
     .option("user", "datauser")
     .option("password", "password")
     .mode("append")
     .save())
