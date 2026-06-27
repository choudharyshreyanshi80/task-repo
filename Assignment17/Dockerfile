FROM python:3.12-slim

# Install Java
RUN apt-get update && apt-get install -y \
    openjdk-21-jdk \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Java Environment
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Install Spark
ENV SPARK_VERSION=3.5.6

RUN wget -q https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz \
    && tar -xzf spark-${SPARK_VERSION}-bin-hadoop3.tgz \
    && mv spark-${SPARK_VERSION}-bin-hadoop3 /opt/spark \
    && rm spark-${SPARK_VERSION}-bin-hadoop3.tgz

ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Working Directory
WORKDIR /app

# Install Python Packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Project Files
COPY . .

# Automatically Run Application
CMD ["spark-submit", "app.py"]