from kafka import KafkaProducer
import json
import time

# def json_serializer("Wha"):
#     return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer="Simple")

if __name__ == "__main__":
    while 1 == 1:
        producer.send("TestTopic", "Hello world")
        time.sleep(4)