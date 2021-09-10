from kafka import KafkaProducer
import json
from data_source import get_text_corpus
import time
import random

local_boostrap_server_address = 'localhost:9092'
cloud_boostrap_server_address1 = "b-1.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092"
cloud_boostrap_server_address2 = "b-2.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092"

def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=[cloud_boostrap_server_address1],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    while 1 == 1:
        n = random.randint(0,9999)
        text_corpus = get_text_corpus(n)
        print(text_corpus)
        producer.send("topic0001", text_corpus)
        time.sleep(2)