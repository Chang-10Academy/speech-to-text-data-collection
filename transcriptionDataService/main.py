from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
import os
import sys

sys.path.append(os.path.abspath(os.path.join('../ProducerConsumer')))
from Chang_Consumer import Chang_Consumer


app = FastAPI()


cloud_boostrap_server_address1 = "b-1.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092"
local_boostrap_server_address = 'localhost:9093'
TOPIC_NAME = "test_text_dan"

consumer = Chang_Consumer(broker = cloud_boostrap_server_address1, topic_name=TOPIC_NAME)

@app.get("/text")
def get_text():
    msg = next(consumer.consume())

    result = {"offset": msg.offset, "value": msg.value}
    return result