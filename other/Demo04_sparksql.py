from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode

if __name__ == '__main__':
   text_file_path = "D:\code\pythonProject1-pyspark-py37\word.txt"
   spark = SparkSession.builder \
      .appName("PySparkSQLWordCount") \
      .getOrCreate()
   lines_df = spark.read.text(text_file_path)

   words_df = lines_df.select(explode(split(lines_df.value, " ")).alias("word"))
   word_count_df = words_df.groupBy("word").count()

   word_count_df.show()

   spark.stop()



