# Data Engineering: Speech-to-text data collection with Kafka, Airflow, and Spark

After starting your Zookeeper server and Kafka broker, execute the code below

```
kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic audiostore
```
Open two command prompt windows. On the first one, execute the following command to run the producer

```
python producer.py
```
On the second one, execute the following command to run the kafka consumer

```
python consumer.py
```