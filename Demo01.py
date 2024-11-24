from pyspark.sql import SparkSession
import findspark

if __name__ == '__main__':
    findspark.init()

    spark = SparkSession.builder \
        .appName("Python Spark SQL basic example") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
    # spark is an existing SparkSession
    # df = spark.read.json("examples/src/main/resources/people.json")
    df = spark.read.csv("D:\code\pythonProject1-pyspark-py37\word.txt")
    # Displays the content of the DataFrame to stdout
    # df.
    df.show()
    # +----+-------+
    # | age|   name|
    # +----+-------+
    # |null|Michael|
    # |  30|   Andy|
    # |  19| Justin|

    # 将每一行文本拆分成单词
    words = df.flatMap(lambda line: line.split(" "))

    # 为每个单词创建一个键值对，键为单词，值为1，表示该单词出现了1次
    word_pairs = words.map(lambda word: (word, 1))

    # 根据单词作为键进行聚合操作，将相同单词的计数相加
    word_counts = word_pairs.reduceByKey(lambda x, y: x + y)

    # 收集结果并打印，将分布式计算的结果收集到驱动程序中以便查看
    for (word, count) in word_counts.collect():
        print(f"{word}: {count}")

    # 关闭SparkContext，释放资源
    spark.stop()

