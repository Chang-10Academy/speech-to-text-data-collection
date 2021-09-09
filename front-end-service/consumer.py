from kafka import KafkaConsumer
import json


if __name__ == "__main__":
    consumer = KafkaConsumer(
        "topic0001",
        bootstrap_servers='localhost:9092',
        auto_offset_reset='latest',
        group_id="consumer-group-a")
    print("starting the consumer")
    for msg in consumer:
        print("Registered User = {}".format(json.loads(msg.value)))
