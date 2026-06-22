# Sales Data Analysis Using PySpark DataFrames

## Objective

Process sales data using PySpark DataFrames and Docker.

## Operations Performed

1. Read CSV data into a DataFrame.
2. Sort all products by sales in descending order.
3. Display top 3 highest-selling products.
4. Filter products with sales greater than 80,000.
5. Save filtered results as CSV.

## Dataset

sales.csv

## Technologies Used

* Python 3.12
* Apache Spark 3.5.6
* PySpark DataFrames
* Docker
* OpenJDK 21

## Build Docker Image

```bash
docker build -t sales-app .
```

## Run Docker Container

```bash
docker run --rm sales-app
```

## Output

Filtered records are saved in:

```text
output/high_sales_products
```
