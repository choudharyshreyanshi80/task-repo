from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("salesapp") \
    .getOrCreate()

# Read CSV
df = spark.read.csv(
    "sales.csv",
    header=True,
    inferSchema=True
)

print("Dataset:")
df.show()

# Sort by sales descending
result = df.orderBy(df.sales.desc())

print("\nSorted by Sales:")
result.show()

# Top 3 products
print("\nTop 3 Products:")
top3 = result.limit(3)
top3.show()

# Filter sales > 80000
high_sales = df.filter(df.sales > 80000)

high_sales.coalesce(1) \
    .write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("/app/output/high_sales_product")
print("Filtered products saved successfully.")

spark.stop()