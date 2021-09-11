from kafka import KafkaConsumer, KafkaProducer
import os
import json
import uuid
from concurrent.futures import ThreadPoolExecutor


if __name__ == "__main__":
    TOPIC_NAME = "audio"

    KAFKA_SERVER = "localhost:29092"

 
    consumer = KafkaConsumer(
        TOPIC_NAME,
        # to deserialize kafka.producer.object into dict
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    )
    for audio in consumer:
        print("Audio = {}".format(json.loads(audio.value)))
	
