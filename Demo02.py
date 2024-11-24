from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import findspark


if __name__ == '__main__':
    findspark.init()

    # 创建SparkSession，它是使用PySpark SQL的入口点
    spark = SparkSession.builder.appName("PySparkSQLWordCount").getOrCreate()

    # 读取文本数据，可以是本地文件路径或者分布式存储系统中的路径
    # 假设这里读取本地的一个文本文件，示例文件路径为 "input.txt"，你可根据实际情况替换
    df = spark.read.text("word.txt")

    # 将每一行文本拆分成单词，使用explode函数将数组中的元素展开
    words_df = df.select(F.explode(F.split(df.value, " ")).alias("word"))

    # 对单词进行分组，并计算每个单词的出现次数
    word_count_df = words_df.groupBy("word").count()

    # 展示最终的结果
    word_count_df.show()

    # 停止SparkSession，释放资源
    spark.stop()

