from kafka import KafkaConsumer
import json

local_boostrap_server_address = 'localhost:9092'
cloud_boostrap_server_address1 = "b-1.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092"
cloud_boostrap_server_address2 = "b-2.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092"

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "topic0001",
        bootstrap_servers=cloud_boostrap_server_address1,
        auto_offset_reset='latest',
        group_id="consumer-group-a")
    print("starting the consumer")
    for msg in consumer:
        print("Registered User = {}".format(json.loads(msg.value)))
