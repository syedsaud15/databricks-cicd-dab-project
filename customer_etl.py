# Databricks notebook source

from pyspark.sql import functions as F

# Sample customer data
data = [
    (1, "Aarav", "Mumbai", 25000),
    (2, "Sara", "Pune", 42000),
    (3, "Rahul", "Delhi", 31000),
    (4, "Ayesha", "Hyderabad", 55000),
    (5, "Kabir", "Bangalore", 48000)
]

columns = ["customer_id", "customer_name", "city", "total_spend"]

df = spark.createDataFrame(data, columns)

# Transformation
customer_summary = (
    df
    .withColumn("customer_name", F.upper(F.col("customer_name")))
    .withColumn(
        "customer_segment",
        F.when(F.col("total_spend") >= 40000, "Premium")
         .otherwise("Standard")
    )
)

customer_summary.show()

print("Customer ETL pipeline completed successfully.")
