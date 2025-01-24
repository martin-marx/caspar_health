#!/bin/bash

sudo apt-get update # Update the list of packages
sudo apt-get install docker-compose-plugin # Install Docker Compose

docker build -t airflow_with_deps:1.0 . # Build the image for Apache Airflow

# Download java libs
curl -o aws-java-sdk-bundle-1.12.779.jar https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.779/aws-java-sdk-bundle-1.12.779.jar
curl -o hadoop-aws-3.3.4.jar https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
curl -o postgresql-42.7.0.jar https://repo1.maven.org/maven2/org/postgresql/postgresql/42.7.0/postgresql-42.7.0.jar

mv aws-java-sdk-bundle-1.12.779.jar hadoop-aws-3.3.4.jar postgresql-42.7.0.jar ./components/loader/jars/
