from time import sleep
from json import dumps
from kafka import KafkaProducer
import random
import logging

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
try:
    text_coll = open('../data/texts/data_3.txt', 'r', encoding="utf8")
except FileNotFoundError:
    logging.error('txt file not found')

texts = list(map(lambda x: x.strip(), text_coll.readlines()))
for e in range(10):
    data = {"transcript": texts[random.randint(0, len(texts)-1)], "sample_rate": 8000, "audio": [0]*10}
    print("produced:", data)
    producer.send('audiostore', value=data)
    sleep(5)
text_coll.close()