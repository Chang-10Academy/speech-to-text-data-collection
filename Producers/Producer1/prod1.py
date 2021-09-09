# from kafka import KafkaProducer
import os
import json
from sys import path
from dataProd1 import readData
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


# producer = KafkaProducer(bootstrap_servers=['192.168.0.10:9092'],
#                          value_serializer=json_serializer)
path  = str(os.path.abspath(os.path.join('../../data/preprocessed')))
addFactor = 10
n = 0
sfiles = 0
efiles = 10
sentence = []
if __name__ == "__main__":
    while efiles < 9999:
        n = n + 1
        print(readData(path,sfiles,efiles)[len(readData(path,sfiles,efiles)) -1])
        print('....................................................')
        sfiles = n * addFactor  + sfiles
        efiles = n * addFactor  + efiles
        # producer.send("registered_user", registered_user)
        time.sleep(2)