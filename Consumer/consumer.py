# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 08:14:57 2021

@author: Smegn
"""
from __future__ import print_function
import threading, logging, time
from kafka import KafkaConsumer, KafkaProducer


msg_size = 524288

consumer_stop = threading.Event()

#produce bytes type instead of the str type.
class Consumer(threading.Thread):

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                                 auto_offset_reset='earliest',group_id="consumer-group-a")
        consumer.subscribe(['my-topic'])
        self.valid = 0
        self.invalid = 0
     
        for message in consumer:
            if len(message.value) == msg_size:
                self.valid += 1
            else:
                self.invalid += 1

            if consumer_stop.is_set():
                break

        consumer.close()
def main():
    threads = [
        Consumer()
    ]
    for t in threads:
        t.start()

    time.sleep(10)
    consumer_stop.set()
    print('Messages recived: %d' % threads[0].valid)
    print('Messages invalid: %d' % threads[1].invalid)

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    main()