FROM python:3.12-slim

# Switch Debian repositories from HTTP to HTTPS
RUN sed -i 's|http://deb.debian.org|https://deb.debian.org|g' /etc/apt/sources.list.d/debian.sources

# Install Java, wget and tar
RUN apt-get update && apt-get install -y \
    openjdk-21-jdk \
    wget \
    tar \
    && rm -rf /var/lib/apt/lists/*

# Java Environment
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Spark Version
ENV SPARK_VERSION=3.5.5

# Download Spark
RUN wget -q https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz \
    && tar -xzf spark-${SPARK_VERSION}-bin-hadoop3.tgz \
    && mv spark-${SPARK_VERSION}-bin-hadoop3 /opt/spark \
    && rm spark-${SPARK_VERSION}-bin-hadoop3.tgz

# Spark Environment
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Working Directory
WORKDIR /app

# Copy files
COPY employee_rdd.py .
COPY employees.csv .

# Run Spark application
CMD ["spark-submit", "employee_rdd.py"]