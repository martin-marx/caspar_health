FROM apache/airflow:2.10.4
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         openjdk-17-jre-headless \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" apache-airflow-providers-apache-spark==2.1.3
RUN pip install --no-cache-dir dbt-core==1.9.1 dbt-core==1.9.1
RUN pip install --no-cache-dir dbt-postgres==1.9.0 dbt-postgres==1.9.0



