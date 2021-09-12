from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
import json

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

class Chang_Producer:
    
    def __init__(self, broker: str, client_id: str ="group__1"):
        self.broker = broker
        self.admin_client = KafkaAdminClient(bootstrap_servers=broker, client_id=client_id)
        self.producer = KafkaProducer(bootstrap_servers=[broker],
                         value_serializer=json_serializer)
    
    def get_topics(self):
        
        return self.admin_client.list_topics()
    
    def create_topic(self, topic_name: str, dont_create_if_exist = True, num_partitions=1, replication_factor=2):
        topic_list =  self.admin_client.list_topics()
        if dont_create_if_exist and  topic_name in topic_list:
            print("Topic already exsit")
            return
        
        new_topic = NewTopic(name=topic_name, num_partitions=num_partitions,replication_factor=replication_factor)
        topic_list.append(new_topic)
        self.admin_client.create_topics(new_topics=topic_list, validate_only=False)
        
        return new_topic
    
    def produce(self, topic_name: str, value, verbose=True):
        
        future = self.producer.send(topic_name, value)

        try:
            record_metadata = future.get(timeout=10)
        except KafkaError:
            # Decide what to do if produce request failed...
            log.exception()
            pass
        
        if verbose:
            print("sending")
            print("==============================")
            print ("topic", record_metadata.topic)
            print ("value", value)
            print ("partition", record_metadata.partition)
            print ("offset", record_metadata.offset)
            print()
                  
if __name__ == "__main__":
    cloud_boostrap_server_address1 = "b-1.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092"
    local_boostrap_server_address = 'localhost:9093'
    TOPIC_NAME = "test_topic2_dan"
    
    p = Chang_Producer(broker = cloud_boostrap_server_address1) 

    p.create_topic(TOPIC_NAME)
    
    
    for i in range(5):
        p.produce(TOPIC_NAME, i)
    

        
        

        