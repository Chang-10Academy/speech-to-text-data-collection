from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

for e in range(10):
    data = {'text': str(e), 'audio' : [e]}
    producer.send('audiostore', value=data)
    sleep(5)