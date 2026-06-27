from pyspark.sql import SparkSession
import shutil
import os
 
spark = SparkSession.builder \
    .appName("EmployeeRDDAnalysis") \
    .getOrCreate()

data = spark.sparkContext.textFile("employees.csv")

header = data.first()

employees = data.filter(lambda row: row != header)

employees = employees.map(lambda row: row.split(",")) \
                     .map(lambda x: (
                         int(x[0]),
                         x[1],
                         x[2],
                         int(x[3])
                     ))

print("\n=== Employees Sorted by Salary (Descending) ===")

sorted_employees = employees.sortBy(
    lambda x: x[3],
    ascending=False
)

for emp in sorted_employees.collect():
    print(emp)

print("\n=== Department-wise Total Salary ===")

dept_salary = employees.map(
    lambda x: (x[2], x[3])
).reduceByKey(
    lambda a, b: a + b
)

for dept, total in dept_salary.collect():
    print(f"{dept}: {total}")


top3 = sorted_employees.take(3)

output_path = "output/top3_employees"

if os.path.exists(output_path):
    shutil.rmtree(output_path)

output_rdd = spark.sparkContext.parallelize([
    f"{emp[0]},{emp[1]},{emp[2]},{emp[3]}"
    for emp in top3
])

output_rdd.saveAsTextFile(output_path)

print("\nTop 3 highest-paid employees saved successfully.")

spark.stop()