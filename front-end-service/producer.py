from kafka import KafkaProducer
import json
from data_source import get_text_corpus
import time
import random


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    while 1 == 1:
        n = random.randint(0,9999)
        text_corpus = get_text_corpus(n)
        print(text_corpus)
        producer.send("topic0001", text_corpus)
        time.sleep(2)