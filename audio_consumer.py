from kafka import KafkaConsumer, KafkaProducer
import os
import json
import uuid
from concurrent.futures import ThreadPoolExecutor


if __name__ == "__main__":
	TOPIC_NAME = "audio"
 	consumer = KafkaConsumer('TOPIC_NAME',client_id='d_id',bootstrap_servers=["b-1.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092","b-2.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092"],auto_offset_reset='earliest', enable_auto_commit=True)
    	for event in consumer:
		event_data = event.value
		print(event_data)
	
