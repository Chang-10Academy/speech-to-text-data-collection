from kafka import KafkaProducer
import json
from audioData import get_Audio
import time


def json_serializer(data):
    return json.dumps(data.decode(errors = 'ignore')).encode('utf-8','ignore')


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                        #  value_serializer=lambda m: dumps(m).encode('utf-8')
                        value_serializer=json_serializer
                         )

if __name__ == "__main__":
    while 1 == 1:
        audio = get_Audio()
        producer.send("x", audio)
        time.sleep(20)
