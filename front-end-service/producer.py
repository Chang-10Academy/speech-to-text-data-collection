import pandas as pd
import random
import math, time
from kafka import KafkaProducer
import json

local_boostrap_server_address = 'localhost:9092'
cloud_data_path = '/mnt/10ac-batch-4/all-data/transcriptions/Amharic_transcriptions/Clean_Amharic.txt'
cloud_csv_file_data_path = '/mnt/10ac-batch-4/all-data/transcriptions/Chang_transcriptions_csv/processed.csv'
cloud_data_lake_path = '/mnt/10ac-batch-4/all-data/Chang/'


def json_serializer(data):
    return json.dumps(data).encode("utf-8")
 
producer = KafkaProducer(bootstrap_servers=[local_boostrap_server_address],
                         value_serializer=json_serializer)




def get_text_corpus():
    df = pd.read_csv(cloud_csv_file_data_path)
    while True:
        n = random.randint(0,483)
        data = df.iloc[n]["sentence"]
        print(data)
        producer.send("topic0001", {'data': data})
        time.sleep(1)


if __name__ == "__main__":
    get_text_corpus()