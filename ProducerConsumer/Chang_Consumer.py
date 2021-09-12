from kafka import KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic
import json


class Chang_Consumer:
    
    def __init__(self, broker: str, topic_name: str, auto_offset_reset='latest', group_id="consumer-group-a"):
        self.broker = broker
        self.consumer =KafkaConsumer( topic_name, bootstrap_servers=broker,
                                     auto_offset_reset=auto_offset_reset, group_id=group_id
                                    )
    
    def consume(self):
        for msg in self.consumer:
            print("Registered User = {}".format(json.loads(msg.value)))
            print ("%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition,
                                          msg.offset, msg.key,
                                          msg.value))
        
        
if __name__ == "__main__":
    cloud_boostrap_server_address1 = "b-1.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092"
    local_boostrap_server_address = 'localhost:9093'
    TOPIC_NAME = "test_topic2_dan"
    
    c = Chang_Consumer(broker = cloud_boostrap_server_address1, topic_name=TOPIC_NAME)
    c.consume()

    

        
        

        