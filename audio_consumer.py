from kafka import KafkaConsumer, KafkaProducer
import os
import json
import uuid
from concurrent.futures import ThreadPoolExecutor
from scipy.io.wavfile import read, write
import pydub
import io
import boto3

s3 = boto3.resource('s3')


if __name__ == "__main__":
	TOPIC_NAME = "audio"
	consumer = KafkaConsumer(TOPIC_NAME, client_id='d_id', bootstrap_servers=["b-1.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092", 
										    "b-2.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092"],
										     auto_offset_reset='earliest',
										     enable_auto_commit=True)
	for event in consumer:
		event_data = event.value
		print(event_data)
		bytes_wav = bytes()
		byte_io = io.BytesIO(event_data)
		print ("done")
		audio = pydub.AudioSegment.from_raw(byte_io, sample_width=2, frame_rate=22050, channels=1).export("newfile", format='wav')
# 		s3.meta.client.upload_file("newfile","chang-stt-bucket","newfile.wav")
		s3.meta.client.upload_file("newfile","chang-stt-bucket",uuid + ".wav")
		

