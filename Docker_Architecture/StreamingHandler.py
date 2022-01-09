import findspark
findspark.init()

from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


conf = SparkConf().setAppName("positions").setMaster('local')
sc = SparkContext.getOrCreate(conf=conf)
ssc = StreamingContext(sc, 5)
data = KafkaUtils.createDirectStream(ssc, topics=["positions"], kafkaParams={"metadata.broker.list":"localhost:9092"})

print(data)

ssc.start()
ssc.awaitTermination()