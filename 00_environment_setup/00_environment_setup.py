from pyspark.sql import SparkSession

def main():
    # Create Spark Session
    spark = SparkSession.builder \
        .appName("PySpark VSCode Setup") \
        .getOrCreate()

    # Sample DataFrame
    data = [("James", "Smith"), ("Anna", "Rose"), ("Robert", "Williams")]
    columns = ["FirstName", "LastName"]
    df = spark.createDataFrame(data, columns)

    # Show DataFrame
    df.show()

    # Stop Spark Session
    spark.stop()

if __name__ == "__main__":
    main()