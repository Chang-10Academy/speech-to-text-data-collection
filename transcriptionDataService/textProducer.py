import os
import sys
import pandas as pd
import time



from  TextDataServ import TextDataServ
sys.path.append(os.path.abspath(os.path.join('../ProducerConsumer')))
import random

from Chang_Producer import Chang_Producer

csv_path = str(os.path.abspath(os.path.join('../data/text.csv')))
bucket_name = "chang-stt-bucket"
text_path  = str(os.path.abspath(os.path.join('../data/preprocessed')))
cloud_text_file_name = "chang-amharic-text-final.csv"

cloud_boostrap_server_address1 = "b-1.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092"
local_boostrap_server_address = 'localhost:9093'
TOPIC_NAME = "test_text_dan"

def download_text_from_bucket():
    data_server = TextDataServ(None)
    return data_server.download_text_csv(csv_path, bucket_name, cloud_text_file_name)
    

if __name__ == "__main__":
    if (download_text_from_bucket()):
        print("loading text dataframe")
        
        df = pd.read_csv('../data/text.csv')
        print("dataframe loaded")
        
        texts = df['text'].to_list()
        file_names = df['file_name'].to_list()
        
        p = Chang_Producer(broker = cloud_boostrap_server_address1) 
        p.create_topic(TOPIC_NAME)
        i = 0
        
        while True:
            try:
                
                n = random.randint(0, len(texts))
                value = {"text": texts[n], "label": file_names[n]}
                p.produce(TOPIC_NAME, value, verbose=True)
                i += 1
                
            except:
                print("Something went wrong")
                pass
