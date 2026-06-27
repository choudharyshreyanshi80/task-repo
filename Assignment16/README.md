# Employee RDD Analysis using PySpark

## Objective

This project processes employee data using PySpark RDDs.

### Operations Performed

1. Sort employees by salary in descending order.
2. Calculate department-wise total salary.
3. Identify the top 3 highest-paid employees.
4. Save the top 3 employees to an output file.

## Dataset

employees.csv

## Technologies Used

- Python 3.12
- Apache Spark 3.5.6
- PySpark
- Docker
- Java 21

## Build Docker Image

```bash
docker build -t employee-rdd .
```

## Run Docker Container

```bash
docker run --rm employee-rdd
```

## Output Location

output/top3_employees
