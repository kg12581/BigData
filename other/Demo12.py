from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# 创建 SparkSession 对象
spark = SparkSession.builder.appName("DecisionTreeExample").getOrCreate()

# 加载数据
data = spark.read.csv("your_data_path", header=True, inferSchema=True)

# 选择特征列和目标列
features = [col for col in data.columns if col!= "target_column_name"]
assembler = VectorAssembler(inputCols=features, outputCol="features")
data = assembler.transform(data)

# 划分训练集和测试集
(train_data, test_data) = data.randomSplit([0.8, 0.2])

# 创建决策树分类器
dt = DecisionTreeClassifier(labelCol="target_column_name", featuresCol="features")

# 构建管道
pipeline = Pipeline(stages=[dt])

# 训练模型
model = pipeline.fit(train_data)

# 在测试集上进行预测
predictions = model.transform(test_data)

# 评估模型
evaluator = MulticlassClassificationEvaluator(labelCol="target_column_name", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print("Accuracy = ", accuracy)

# 停止 SparkSession
spark.stop()