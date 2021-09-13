# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 08:34:51 2021

@author: Smegn
"""

import json
#from app import db
from sqlalchemy import event
from kafka import KafkaProducer

def send_order_info_to_kafka(mapper, connection, target):
    assert record.id is not None
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    topic_name = 'new_recording'
    order_dict = {"record_id": record.id,
"record_size": record.size,
"record_time_ms": record.time()
}
    producer.send(topic_name, value=json.dumps(order_dict).encode())
    producer.flush()
"""
 event.listens_for() decorator (imported from the sqlalchemy library).
decorator monitors the event when the record about the new record is inserted
 into the database.
 It creates a KafkaProducer instance (which points to the URL where the running
Kafka cluster is located) and specifies the name of the Kafka topic — new_recording
.Then the function creates the body of the message. We want to send 
statistics about the orders to Kafka. That’s why for each order,
 we create the dictionary with information about the recording.
 Then we transform this dictionary into JSON format, encode it, and send it
 to Kafka using the producer’s methods send() and flush().
 To sumup its purpose  is to send information about the created order to the 
 Kafka cluster
 """
 
import time
import threading
import datetime
from kafka import KafkaConsumer
#the consumer (web_requests) and the bootstrap_servers parameter 
#that points to the server where the Kafka cluster is located.
consumer = KafkaConsumer('web_requests',
bootstrap_servers=['localhost:9092'],
auto_offset_reset='earliest',
enable_auto_commit=True,
auto_commit_interval_ms=1000,
consumer_timeout_ms=-1)

"""
create a function which will poll the Kafka cluster once a minute and 
process the messages which Kafka will return. The name of the function is 
fetch_last_min_requests()

The next call of this function should occur (60 seconds from now).Each row will 
have the timestamp in the datetime column as well as the number of requests 
that were processed by the website during the given minute in the requests_num 
column. and If this is not the first execution of the function, it will
 force the consumer to poll the Kafka cluster.Before you can execute it,
 you should run the Kafka cluster.
 """

def fetch_last_min_requests(next_record_in, is_first_execution=False):
    next_record_in += 60
    counter_requests = 0
    if is_first_execution:
        with open('requests.csv','a') as file:
            headers = ["datetime", "requests_num"]
            file.write(",".join(headers))
            file.write('\n')
    else:
        batch = consumer.poll(timeout_ms=100)
    if len(batch) > 0:
        for message in list(batch.values())[0]:
            counter_requests += 1
            with open('requests.csv','a') as file:
                data = [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str(counter_requests)]
                file.write(",".join(data))
                file.write('\n')
    threading.Timer(next_call_in - time.time(),
    fetch_last_minute_requests,
    [next_record_in]).start()